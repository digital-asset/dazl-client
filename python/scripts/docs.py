#!/usr/bin/env pipenv run python3
# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import socketserver
import sys
import tarfile
from argparse import ArgumentParser
from threading import Thread

from dataclasses import dataclass, replace
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from tempfile import mkdtemp
from typing import Optional, Sequence

from sphinx.cmd.build import main as sphinx_build_main


DAZL_ROOT = Path(__file__).expanduser().resolve().parent.parent


@dataclass(frozen=True)
class DocumentationBuildArguments:
    working_directory: 'Path'
    sphinx_build_args: 'Sequence[str]'
    output_directory: 'Path'
    output_file: 'Optional[Path]'
    output_format: 'str'
    archive_format: 'Optional[str]'


def main(argv: 'Sequence[str]'):
    if len(argv) == 1:
        print('Usage: scripts/docs.py build')
        sys.exit(1)

    cmd = argv[1]
    os.chdir(DAZL_ROOT)

    argp = ArgumentParser()
    argp.add_argument('--format', '-f', default='html')
    argp.add_argument('--output-path', '-o', default=os.getenv('DAZL_DOCS_OUT', str(DAZL_ROOT / 'dist' / 'documentation')))
    argp.add_argument('--theme', default=os.getenv('DAZL_DA_THEME'))
    argp.add_argument('--dry-run', action='store_true')

    args = argp.parse_args(argv[2:])

    dba = parse_arguments(
        output_path=Path(args.output_path) if args.output_path else None,
        output_format=args.format,
        theme_path=Path(args.theme) if args.theme else None)

    if cmd == 'build':
        if not args.output_path:
            print('Either the --output-path command-line parameter or the DAZL_DOCS_OUT variable are required')
            sys.exit(2)
        if not args.dry_run:
            build_docs(dba)
        else:
            print('Would have run the equivalent of:')
            print(f'    cd {dba.working_directory} && \\')
            print(f'      sphinx-build {" ".join(dba.sphinx_build_args)}')
            if dba.archive_format:
                print(f'      tar cfz docs.tgz')
    elif cmd == 'server':
        run_server(dba, 7337)
    

def parse_arguments(output_path: 'Path', output_format: 'str', theme_path: 'Optional[Path]') -> 'DocumentationBuildArguments':
    if len(output_path.suffixes) == 0:
        is_tgz = False
    elif len(output_path.suffixes) == 1:
        is_tgz = output_path.suffixes[0] == '.tgz'
    else:
        is_tgz = (output_path.suffixes[-1] == '.tgz') or \
                 (output_path.suffixes[-2:] == ['.tar', '.gz'])
    
    if is_tgz:
        output_directory = Path(mkdtemp())
        output_file = output_path
        archive_format = 'gz'
    else:
        output_directory = output_path
        output_file = None
        archive_format = None

    return DocumentationBuildArguments(
        working_directory=DAZL_ROOT,
        sphinx_build_args=['-b', output_format, 'docs', str(output_directory)],
        output_directory=output_directory,
        output_file=output_file,
        output_format=output_format,
        archive_format=archive_format)


def build_docs(args: 'DocumentationBuildArguments'):
    os.chdir(str(args.working_directory))
    sphinx_build_main(list(args.sphinx_build_args))
    if args.output_file:
        args.output_file.parent.mkdir(exist_ok=True)
        try:
            args.output_file.unlink()
        except FileNotFoundError:
            pass
        with tarfile.open(args.output_file, f'x:{args.archive_format}') as t:
            t.add(args.output_directory, arcname='documentation')
    print(f'Wrote {args.output_file}.')


def run_server(args: 'DocumentationBuildArguments', port: 'int'):
    import time
    from watchdog.events import FileSystemEventHandler, LoggingEventHandler
    from watchdog.observers import Observer as WatchdogObserver

    # when in server mode, serve files up from the file system as-is, no archiving
    replaced_args = replace(args, archive_format=None)

    build_docs(replaced_args)

    class docs_update_handler(FileSystemEventHandler):
        def on_any_event(self, event):
            print('handling an event...')
            if not event.is_directory:
                build_docs(replaced_args)

    observer = WatchdogObserver()
    observer.schedule(LoggingEventHandler(), str('dazl'), recursive=True)
    observer.schedule(LoggingEventHandler(), str('docs'), recursive=True)
    observer.schedule(docs_update_handler(), str('dazl'), recursive=True)
    observer.schedule(docs_update_handler(), str('docs'), recursive=True)
    observer.start()

    d = {}

    def run_http_server():
        with socketserver.TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
            d['httpd'] = httpd
            httpd.serve_forever()

    t = Thread(target=run_http_server)
    t.start()

    print(f"Watching for changes in {replaced_args.output_directory} and Serving at port {port}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    d['httpd'].shutdown()


if __name__ == '__main__':
    main(sys.argv)
