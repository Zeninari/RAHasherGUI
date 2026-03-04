# ![RAHasherGUI](RA.ico) RAHasherGUI

![Python](https://img.shields.io/badge/python-3.x-blue) ![License](https://img.shields.io/badge/license-MIT-green)  

⚠️ **Warning:** RAHasherGUI is a **GUI wrapper for the RetroAchievements Hasher** created by [LeXofLeviafan](https://github.com/LeXofLeviafan/RAHasher). This GUI only provides a convenient interface for you to interact with. this isn't meant to entirely replace the tool, only make it easier to use.  

## Overview

RAHasherGUI is a **lightweight Python GUI** that simplifies using RAHasher:

- Drag & drop ROM files directly onto the window.  
- Select your system from a dropdown.  
- Quickly hash your ROMs with a single click.
- If you build the cache, also shows if theres any supported RA hashes (Achievements)  

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

## NEW v1.2 Features:
| Feature | Description |
|---------|-------------|
| Bigger Window | Makes it easier to view things |
| Better System Management | Now automatically selects relevant systems to the chosen file |
| Automatic Hash Reading Support | If you have the cache downloaded, It will show if it has RA |
| Scrollbar | The window now autoscrolls and has a scrollbar on the side |

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
Or:
pyinstaller RAHasherGUI.spec

To compile the caching program run:
pyinstaller --onefile --icon=RA.ico "BuildRAHasherGUICache.py"
Or:
pyinstaller BuildRAHasherCache.spec
```

⚠️ **Note:** RAHasher is **NOT** included in this repository. Download the official RAHasher from the original repository: https://github.com/LeXofLeviafan/RAHasher/releases

⚠️ **Note** RA Hashes is **NOT** included in this repository. they are downloaded from the official RA Hashes repository using my tool: https://github.com/RetroAchievements/RAHashes


## Usage

1. Launch RAHasherGUI.
2. Browse for a ROM file, type/paste in the file path, or drag & drop it into the window.
3. Select your system from the dropdown. they are now filtered by the extention of the ROM
4. Click **Hash** to generate the hash output.
5. If you downloaded the RA cache using my tool, It will also put the RA data into the output
6. (Optional) Override RAHasher by placing a version of `RAHasher.exe` next to the GUI executable.

⚠️ **Note:** This GUI does not check Whether or not the rom selected is being computed with the correct hashing algorithm. for example, if you calculate a gameboy ROM with the gameboy advance algarthm it will compute (from RAHasher) and then display the wrong hash. if using v1.2 then make sure your roms arent the wrong extention, otherwise the above still applies.

## Bug Reports

Found a bug or crash? Please **open an issue** in this repository with steps to reproduce it.

## License

This GUI is **MIT licensed**.  
RAHasher is maintained separately by its original authors.

## Credits

- RAHasher by [LeXofLeviafan](https://github.com/LeXofLeviafan/RAHasher)  
- GUI Wrapper by Zeninari
