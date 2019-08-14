# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
from contextlib import ExitStack
from pathlib import Path
from typing import Union, List, Sequence

from .. import LOG
from ..model.types_store import PackageStore
from ..util.dar import TemporaryDar, parse_dalf, DarFile
from ..util.path_util import pathify


class LocalDarRepository:
    def __init__(self):
        self._context = ExitStack()
        self._dar_paths = []  # type: List[Path]
        self._files = set()
        self.store = PackageStore.empty()

    def _add_source(self, path: Path) -> None:
        ext = path.suffix.lower()

        if ext == '.daml':
            dar_create_start_time = time.time()
            dar_paths = self._context.enter_context(TemporaryDar(path))
            self.add_source(*dar_paths)
            LOG.debug('Compiled a dar in % seconds.', time.time() - dar_create_start_time)

        elif ext == '.dalf':
            dalf_package = parse_dalf(path.read_bytes())
            self._dar_paths.append(path)
            self.store.register_all(dalf_package)

        elif ext == '.dar':
            dar_parse_start_time = time.time()
            dar = self._context.enter_context(DarFile(path))
            dar_package = dar.read_metadata()
            self._dar_paths.append(path)
            self.store.register_all(dar_package)
            dar_parse_end_time = time.time()
            LOG.debug('Parsed a dar in %s seconds.', dar_parse_end_time - dar_parse_start_time)

        else:
            LOG.error('Unknown extension: %s', ext)
            raise ValueError(f'Unknown extension: {ext}')

    def add_source(self, *files: Union[str, Path]) -> None:
        """
        Add a source file (either a .daml file, .dalf file, or a .dar file).

        Attempts to add the same file more than once will be ignored.

        :param files: Files to add to the archive.
        """
        for file in files:
            path = pathify(file).resolve(strict=True)
            if path not in self._files:
                self._files.add(path)
                self._add_source(path)

    def get_daml_archives(self) -> Sequence[Path]:
        return self._dar_paths

    def __enter__(self):
        """
        Does nothing.
        """
        self._context.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Delete all managed resources in the reverse order that they were created.
        """
        self._context.__exit__(exc_type, exc_val, exc_tb)
