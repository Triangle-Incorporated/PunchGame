{ pkgs }: {
    deps = [
      pkgs.python
      pkgs.python3
	  pkgs.python39Packages.tkinter
    ];
}