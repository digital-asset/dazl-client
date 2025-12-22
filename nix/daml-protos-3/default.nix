{
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml-protos";
  version = "3.4.9";
  buildInputs = [ unzip ];
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/protobufs-${version}.zip";
    sha256 = "1mky05mrd0pm6z0zk1vq3pwbn5p5sj53nzij7i4910zrn2m0wfzh";
  };
  dontUnpack = true;
  buildPhase = ''
    unzip $src
  '';

  # Copy all Daml protos from 3.4.9, including Daml-LF and Ledger API
  installPhase = ''
    mkdir -p "$out"
    cp -R "protos-${version}/com" "$out/"
  '';
}
