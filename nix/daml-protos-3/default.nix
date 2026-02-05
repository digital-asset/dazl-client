{
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml-protos";
  version = "3.4.10";
  buildInputs = [ unzip ];
  src = builtins.fetchurl {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/protobufs-${version}.zip";
    sha256 = "0w4qqvsm439ayf4mwmyj8hnn84pzh76bq24v22fkaydk73zx1c0g";
  };
  dontUnpack = true;
  buildPhase = ''
    unzip $src
  '';

  # the only protobufs from the Daml 3.x package that we care about are Daml LF
  installPhase = ''
    mkdir -p "$out/com/digitalasset/daml/lf"
    cp -R "protos-${version}/com/digitalasset/daml/lf/archive" "$out/com/digitalasset/daml/lf/archive"
  '';
}
