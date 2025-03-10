# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import base64
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Optional
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
    def canton_2(cls, version: str) -> Self:
        file_name = f"canton-open-source-{version}.zip"
        url = f"https://github.com/digital-asset/canton/releases/download/v{version}/{file_name}"
        return cls(url=url, file_name=file_name)

    @classmethod
    def daml_protos(cls, version: str) -> Self:
        file_name = f"protobufs-{version}.zip"
        if "snapshot" in version:
            # snapshot versions are unfortunately not discoverable by version number alone
            # TODO: might be time to retire this machinery and start pulling down files a different way
            url = "https://github.com/digital-asset/daml/releases/download/v3.2.0-snapshot.20241106.0/protobufs-3.2.0-snapshot.20241031.13398.0.vf95d2607.zip"
        else:
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

    def remote_md5(self) -> Optional[bytes]:
        """
        Make a HEAD request for this Source's data, and retrieve its MD5.
        """
        response = request.urlopen(request.Request(self.url, method="HEAD"))
        try:
            if response.code == 200:
                md5_base64 = response.headers["Content-MD5"]
                return base64.b64decode(md5_base64) if md5_base64 is not None else None
            else:
                raise RuntimeError(f"when trying to fetch {self.url}, got a {response.code}")
        finally:
            response.close()


@dataclass(frozen=True)
class DownloadPaths:
    canton_2_zip: Path
    daml_2_protos_zip: Path
    daml_3_protos_zip: Path


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


def download_dependencies(
    daml_2_sdk_version: str, daml_3_sdk_version: str, to: Path
) -> DownloadPaths:
    canton_2 = Source.canton_2(daml_2_sdk_version)
    daml_2_protos = Source.daml_protos(daml_2_sdk_version)
    daml_3_protos = Source.daml_protos(daml_3_sdk_version)

    paths = DownloadPaths(
        canton_2_zip=to / canton_2.file_name,
        daml_2_protos_zip=to / daml_2_protos.file_name,
        daml_3_protos_zip=to / daml_3_protos.file_name,
    )

    downloaders = [
        Downloader(canton_2, paths.canton_2_zip),
        Downloader(daml_2_protos, paths.daml_2_protos_zip),
        Downloader(daml_3_protos, paths.daml_3_protos_zip),
    ]

    console = Console()
    console.print("[yellow]Downloading dependencies...")

    for downloader in downloaders:
        if existing_hash := downloader.source.existing_file_md5(to):
            actual_hash = downloader.source.remote_md5()
            if actual_hash is None:
                console.print(
                    f"    [yellow]{downloader.source.file_name} exists, but the remote did not return an MD5 hash; assuming the local file is good..."
                )
                continue
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
