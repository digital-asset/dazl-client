{
  openjdk,
  stdenv,
  unzip,
}:

stdenv.mkDerivation rec {
  pname = "daml";
  version = "2.10.4";
  buildInputs = [ unzip ];
  src = builtins.fetchurl (if stdenv.isDarwin then {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/daml-sdk-${version}-macos.tar.gz";
    sha256 = "0cgkf2s40sbhc3fh3gy427kc2xykf24c4rhapdq4r2p82b7srjib";
  } else {
    url = "https://github.com/digital-asset/daml/releases/download/v${version}/daml-sdk-${version}-linux.tar.gz";
    sha256 = "03w8zfs9j5dx4hrf0lm19jsbfhvsimqb8wba5az1f6s3qd776j4r";
  });
  dontUnpack = true;
  buildPhase = ''
    mkdir daml
    tar xzf $src -C daml --strip-components 1
    patchShebangs .
  '';
  installPhase = ''
    cd daml
    DAML_HOME=$out ./install.sh
  '';
  propagatedBuildInputs = [ openjdk ];
  preFixup = ''
    mkdir -p $out/nix-support
    echo export DAML_HOME=$out > $out/nix-support/setup-hook
    echo export DAML_SDK_VERSION=${version} >> $out/nix-support/setup-hook
  '';
}
