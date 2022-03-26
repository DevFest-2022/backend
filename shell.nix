with (import <nixpkgs> {});
mkShell {
  nativeBuildInputs = [
	python39
	python39Packages.flask
  ];
}

