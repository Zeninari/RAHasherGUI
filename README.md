# ![RAHasherGUI](RA.ico) RAHasherGUI

![Python](https://img.shields.io/badge/python-3.x-blue) ![License](https://img.shields.io/badge/license-MIT-green)  

⚠️ **Warning:** RAHasherGUI is a **GUI wrapper for the RetroAchievements Hasher** created by [LeXofLeviafan](https://github.com/LeXofLeviafan/RAHasher). This GUI only provides a convenient interface for you to interact with. this isn't meant to entirely replace the tool, only make it easier to use.  

## Overview

RAHasherGUI is a **lightweight Python GUI** that simplifies using RAHasher:

- Drag & drop ROM files directly onto the window.  
- Select your system from a dropdown.  
- Quickly hash your ROMs with a single click.  

This release is bundled with **RAHasher Version 1.8.2** for the V1 release.

> Note: The original RAHasher code belongs to its authors. This GUI does **not modify RAHasher**, it only wraps it for convenience.  

## Features

| Feature | Description |
|---------|-------------|
| Typing/Pasting | Direct input for the path to your ROM |
| File Selection | Selection of the ROM via the file browser|
| Drag & Drop | Allows for Dragging and Droping ROM files directly into the GUI |
| System Selection | Easily select your console from a dropdown list, Ordered by the original RAHasher Order |
| Embedded Hasher | Uses The Embeded RAHasher version **1.8.2** by default. |
| Hasher Override | Place a `RAHasher.exe` next to the GUI to override the bundled version. |

---

## Requirements

- Python 3.x  
- `tkinter` (usually included with Python)  
- `tkinterdnd2` (install via `pip install tkinterdnd2`)  

---

## Installation & Running from Source

Clone the repository:

```bash
git clone https://github.com/yourusername/RAHasherGUI.git
cd RAHasherGUI

To compile a standalone executable with PyInstaller:
pyinstaller --onefile --icon=RA.ico --add-data "RA.ico;." --add-binary "RAHasher.exe;." --noconsole "RAHasherGUI.py"
```

⚠️ **Note:** RAHasher is **NOT** included in this repository. Download the official RAHasher from the original repository: https://github.com/LeXofLeviafan/RAHasher/releases


## Usage

1. Launch RAHasherGUI.
2. Select your system from the dropdown.
3. Browse for a ROM file, type/paste in the file path, or drag & drop it into the window.
4. Click **Hash** to generate the hash output.
5. (Optional) Override RAHasher by placing a version of `RAHasher.exe` next to the GUI executable.

⚠️ **Note:** This GUI does not check Whether or not the rom selected is being computed with the correct hashing algorithm. for example, if you calculate a gameboy ROM with the gameboy advance algarthm it will compute (from RAHasher) and then display the wrong hash.

## Bug Reports

Found a bug or crash? Please **open an issue** in this repository with steps to reproduce it.

## License

This GUI is **MIT licensed**.  
RAHasher is maintained separately by its original authors.

## Credits

- RAHasher by [LeXofLeviafan](https://github.com/LeXofLeviafan/RAHasher)  
- GUI Wrapper by Zeninari
