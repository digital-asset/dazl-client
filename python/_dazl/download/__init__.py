# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import base64
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Optional, Sequence
from urllib import request

from rich.console import Console
from rich.progress import Progress

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

__all__ = ["download_dependencies"]


@dataclass(frozen=True)
class Source:
    file_name: str
    url: str

    @classmethod
    def all(cls, version: str) -> Sequence[Self]:
        return [cls.canton(version), cls.daml_protos(version)]

    @classmethod
    def canton(cls, version: str) -> Self:
        file_name = f"canton-open-source-{version}.zip"
        url = f"https://github.com/digital-asset/canton/releases/download/v{version}/{file_name}"
        return cls(url=url, file_name=file_name)

    @classmethod
    def daml_protos(cls, version: str) -> Self:
        file_name = f"protobufs-{version}.zip"
        url = f"https://github.com/digital-asset/daml/releases/download/v{version}/{file_name}"
        return cls(url=url, file_name=file_name)

    def existing_file_md5(self, to: Path) -> Optional[bytes]:
        import hashlib

        path = to / self.file_name
        if path.exists() and path.is_file():
            md5_hash = hashlib.md5()
            with path.open("rb") as f:
                while chunk := f.read(4096):
                    md5_hash.update(chunk)
            return md5_hash.digest()
        else:
            return None

    def remote_md5(self) -> bytes:
        """
        Make a HEAD request for this Source's data, and retrieve its MD5.
        """
        response = request.urlopen(request.Request(self.url, method="HEAD"))
        try:
            if response.code == 200:
                md5_base64 = response.headers["Content-MD5"]
                return base64.b64decode(md5_base64)
            else:
                raise RuntimeError(f"when trying to fetch {self.url}, got a {response.code}")
        finally:
            response.close()


@dataclass(frozen=True)
class DownloadPaths:
    canton_zip: Path
    daml_protos_zip: Path


class Downloader:
    def __init__(self, source: Source, output_path: Path):
        self.source = source
        self.output_path = output_path

    def download(self, progress: Progress) -> None:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        with request.urlopen(self.source.url) as response:
            task = progress.add_task("[cyan]" + self.source.file_name, total=response.length)
            with self.output_path.open("wb") as file:
                while chunk := response.read(4096):
                    file.write(chunk)
                    progress.update(task, advance=len(chunk))


def download_dependencies(sdk_version: str, to: Path) -> DownloadPaths:
    canton = Source.canton(sdk_version)
    daml_protos = Source.daml_protos(sdk_version)

    paths = DownloadPaths(
        canton_zip=to / canton.file_name, daml_protos_zip=to / daml_protos.file_name
    )

    downloaders = [
        Downloader(canton, paths.canton_zip),
        Downloader(daml_protos, paths.daml_protos_zip),
    ]

    console = Console()
    console.print("[yellow]Downloading dependencies...")

    for downloader in downloaders:
        if existing_hash := downloader.source.existing_file_md5(to):
            actual_hash = downloader.source.remote_md5()
            if existing_hash == actual_hash:
                console.print(f"    [green]{downloader.source.file_name} already cached")
                continue
            else:
                console.print(
                    f"    [red]{downloader.source.file_name} exists, but failed MD5 check"
                )
        else:
            console.print(f"    [yellow]{downloader.source.file_name} downloading...")

        with Progress() as progress:
            downloader.download(progress)

    return paths
