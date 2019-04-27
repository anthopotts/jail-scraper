with import <nixpkgs> {};

stdenv.mkDerivation rec {

  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };

  buildInputs = [
    python3
    python36Packages.pip
    python36Packages.virtualenv
    python36Packages.setuptools
  ];

  shellHook = ''
    SOURCE_DATE_EPOCH=$(date +%s)
    virtualenv --no-setuptools env
    export PATH=$PWD/env/bin:$PATH
    pip install -r requirements.txt
  '';
}
