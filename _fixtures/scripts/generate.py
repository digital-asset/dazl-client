#!/usr/bin/env python3.8
from pathlib import Path
from shutil import rmtree
from _util import SdkVersion


FIXTURES_DIR = Path(__file__).absolute().parent.parent


def generate(sdk_version: 'SdkVersion'):
    src = FIXTURES_DIR / 'templates'
    target = FIXTURES_DIR / 'target' / str(sdk_version)
    if target.exists():
        rmtree(str(target))
    target.mkdir(parents=True, exist_ok=True)
    artifact_dar = FIXTURES_DIR / 'archives' / str(sdk_version) / 'Test.dar'

    for src_daml_file in src.glob('**/*.daml'):
        target_daml_file = target / src_daml_file.relative_to(src)
        target_daml_file.parent.mkdir(parents=True, exist_ok=True)
        
        src_daml_file.link_to(target_daml_file)

    (target / 'daml.yaml').write_text(f'''
sdk-version: {sdk_version}
name: Test
source: daml/LibraryModules.daml
version: 1.0.0
dependencies: []
'''.lstrip())

    (target / 'build.sh').write_text(f'''
#!/bin/sh

mkdir -p {artifact_dar.parent}
(cd {target} && daml build -o {artifact_dar})
'''.lstrip())
    (target / 'build.sh').chmod(0o755)

    print(f'Wrote template version for {sdk_version} in {target}.')


def main():
    import sys
    version_str = sys.argv[1]
    version = SdkVersion.parse(version_str)
    if version is not None:
        generate(version)
    else:
        print(f'Could not parse {version_str!r} as a version')
        sys.exit(1)


if __name__ == '__main__':
    main()
