import shutil
import tarfile
import zipfile
from .config import GOOGLE_RPC_STATUS_PROTO, DAML_LF_JAR, LEDGER_API_TGZ, fetch_urls, CONFIG
from .util import copy, download, remainder


def fetch():
    """
    Fetch Protobuf definitions for DAML-LF, the Ledger API, and other protobuf files required
    for Ledger API clients.
    """
    download_dir = CONFIG.directories.download
    download_dir.mkdir(parents=True, exist_ok=True)

    protos_dir = CONFIG.directories.protos
    if protos_dir.exists():
        shutil.rmtree(protos_dir)

    for file_path, url in fetch_urls.items():
        download(url, download_dir / file_path)

    copy(src=download_dir / GOOGLE_RPC_STATUS_PROTO,
         dest=protos_dir / 'google/rpc/status.proto')

    with tarfile.open(download_dir / LEDGER_API_TGZ) as tar:
        for tarinfo in tar:
            if tarinfo.isfile():
                p = remainder(tarinfo.name, './grpc-definitions/')
                if p is not None:
                    with tar.extractfile(tarinfo) as from_:
                        copy(src=from_, dest=protos_dir / p)

    with zipfile.ZipFile(download_dir / DAML_LF_JAR) as jar:
        for name in jar.namelist():
            p = remainder(name, 'daml-lf/archive/')
            if p is not None:
                with jar.open(name) as from_:
                    copy(src=from_, dest=protos_dir / p)
