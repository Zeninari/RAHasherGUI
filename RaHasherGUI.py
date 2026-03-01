import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import sys
from tkinterdnd2 import DND_FILES, TkinterDnD

systems = dict(s.split('|') for s in """
Nintendo Game Boy|GB
Nintendo Game Boy Advance|GBA
Nintendo Game Boy Color|GBC
Nintendo NES/Famicom|NES
Nintendo SNES/Super Famicom|SNES
Nintendo 64|N64
Nintendo GameCube|GC
Nintendo DS|DS
Nintendo DSi|DSi
Nintendo Pokemon Mini|MINI
Nintendo Virtual Boy|VB
Game & Watch|G&W
Famicom Disk System|FDS
Nintendo 3DS|3DS
Nintendo Wii|Wii
Nintendo Wii U|WiiU
Sony PlayStation|PS1
Sony PlayStation 2|PS2
Sony PlayStation Portable|PSP
Atari 2600|2600
Atari 7800|7800
Atari Jaguar|JAG
Atari Jaguar CD|JCD
Atari Lynx|Lynx
Atari 5200|5200
Atari ST|AST
Sega SG-1000|SG1K
Sega Master System|SMS
Sega Game Gear|GG
Sega Genesis/Mega Drive|MD
Sega Sega CD|SCD
Sega 32X|32X
Sega Saturn|SAT
Sega Dreamcast|DC
Sega Pico|Pico
NEC PC Engine/TurboGrafx-16|PCE
NEC PC Engine CD/TurboGrafx-CD|PCCD
NEC PC-8000/8800|80/88
NEC PC-FX|PC-FX
NEC PC-6000|PC-6000
NEC PC-9800|9800
SNK Neo Geo CD|NGCD
SNK Neo Geo Pocket|NGP
3DO Interactive Multiplayer|3DO
Amstrad CPC|CPC
Apple II|A2
Arcade|ARC
Arcadia 2001|A2001
Arduboy|ARD
ColecoVision|CV
Elektor TV Games Computer|ELEK
Fairchild Channel F|CHF
Intellivision|INTV
Interton VC 4000|VC4000
Magnavox Odyssey 2|MO2
Mega Duck|DUCK
MSX|MSX
Uzebox|UZE
Vectrex|VECT
Watara Supervision|WSV
WASM-4|WASM4
WonderSwan|WS
Amiga|Amiga
Cassette Vision|ECV
Super Cassette Vision|ESCV
Commodore 64|C64
FM Towns|FMTowns
Nokia N-Gage|N-Gage
Oric|Oric
Philips CD-i|CD-i
Sharp X1|X1
Sharp X68000|X68K
Thomson TO8|TO8
TI-83|TI83
TIC-80|TIC-80
VIC-20|VIC-20
Zeebo|Zeebo
ZX81|ZX81
ZX Spectrum|ZXS
DOS|DOS
Xbox|Xbox
""".strip().splitlines())

# Definitions for RAHasherGUI
BASE_DIR = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) \
    else os.path.dirname(os.path.abspath(__file__))

def browse_file():
    if path := filedialog.askopenfilename():
        selected_file.set(path); file_entry.xview_moveto(1)

def drop(event):
    if os.path.isfile(path := event.data.strip('{}')):
        selected_file.set(path); file_entry.xview_moveto(1)

def get_rahasher_path():
    paths = [os.path.join(BASE_DIR, "RAHasher.exe")]
    if getattr(sys, "frozen", False):
        paths.append(os.path.join(sys._MEIPASS, "RAHasher.exe"))
    return next((p for p in paths if os.path.exists(p)), None)
HASHER_PATH = get_rahasher_path()

def run_hasher():
    if not (file_path := selected_file.get()):
        return messagebox.showerror("Error", "Please select a ROM file.")

    if not HASHER_PATH:
        return messagebox.showerror("Error", "RAHasher.exe not found.")

    result = subprocess.run([HASHER_PATH, systems[system_dropdown.get()], file_path], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result.stdout)

# Application Window Setup
root = TkinterDnD.Tk()
root.title("RAHasher GUI")
root.geometry("400x350")
root.resizable(False, False)
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)
ICON_PATH = os.path.join(getattr(sys, "_MEIPASS", BASE_DIR), "RA.ico")
root.iconbitmap(ICON_PATH)
selected_file = tk.StringVar()

#Application Window Layout
ttk.Label(root, text="Select System:").pack(pady=(15, 5))
system_dropdown = ttk.Combobox(root, values=list(systems.keys()), state="readonly", width=50)
system_dropdown.pack()
system_dropdown.current(0)
ttk.Button(root, text="Browse ROM File", command=browse_file).pack(pady=10)
file_entry = ttk.Entry(root, textvariable=selected_file)
file_entry.pack(fill='x', padx=15)
output_box = tk.Text(root, height=8, width=42)
output_box.pack(pady=10)
ttk.Button(root, text="Hash", command=run_hasher).pack()
root.mainloop()