# RAHasherGUI
GUI for The Retro Achivements Hasher By LeXofLeviafan

The Original App Is Stored Here: https://github.com/LeXofLeviafan/RAHasher/releases

I wanted to make a simple gui to go along with the app, and it is bundled with RAHasher Version 1.8.2 for the V1 release. the original code still belongs to the original authors that made them, this is just a simple python gui to make using it easier.
also you can overwrite the version of RAHasher by placing the EXE next to my EXE. if RAHasher.exe exists, it will use that version of RAHasher instead of the one embeded into the GUI. if you find any bugs or crashes do send an issue report to me.

To compile from source run pyinstaller --onefile --icon=RA.ico --add-data "RA.ico;." --add-binary "RAHasher.exe;." --noconsole "RAHasherGUI.py" keep in mind RAHasher is not contained within this repository, check the original repository for RAHasher
