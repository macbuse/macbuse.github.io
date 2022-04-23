

[forward search for texlab](https://github.com/latex-lsp/texlab/blob/master/docs/previewing.md)

See also [repo](https://github.com/f3fora/nvim-texlabconfig)


The SyncTeX feature of Evince requires communication via D-Bus. In order to use it from the command line, install the evince-synctex script.

* the dbus package for python was hard to install
* [follow this](https://stackoverflow.com/questions/60444193/cant-install-dbus-python-on-ubuntu-with-python3-8)
* there is a gotcha with a typo but then this should work

pip3 install --user https://github.com/efoerster/evince-synctex/archive/master.zip


There are other configs 
- .latexmkrc $pdf_previewer [values](https://mg.readthedocs.io/latexmk.html)
- .config/zathurarc 

