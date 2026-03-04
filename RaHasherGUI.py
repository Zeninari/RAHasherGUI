import json
import glob
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import sys
from tkinterdnd2 import DND_FILES, TkinterDnD

# Filling Out These Systems WAS A PAIN!! (Worth It Tho)
systems = {
    "Nintendo Game Boy": {"code": "GB", "extensions": [".gb"]},
    "Nintendo Game Boy Advance": {"code": "GBA", "extensions": [".gba"]},
    "Nintendo Game Boy Color": {"code": "GBC", "extensions": [".gbc"]},
    "Nintendo NES/Famicom": {"code": "NES", "extensions": [".nes", ".unif", ".unf", ".bin", ".rom", ".fds"]},
    "Nintendo SNES/Super Famicom": {"code": "SNES", "extensions": [".smc", ".fig", ".sfc", ".swc", ".bs", ".st", ".bml", ".rom", ".gd3", ".gd7", ".dx2", ".bsx"]},
    "Nintendo 64": {"code": "N64", "extensions": [".z64", ".n64", ".v64", ".bin", ".u1", ".ndd"]},
    "Nintendo GameCube": {"code": "GC", "extensions": [".gcm", ".iso", ".gcz", ".ciso", ".wbfs", ".rvz", ".dol"]},
    "Nintendo DS": {"code": "DS", "extensions": [".nds", ".ids", ".bin"]},
    "Nintendo DSI": {"code": "DSi", "extensions": [".nds", ".dsi", ".bin"]},
    "Nintendo Pokemon Mini": {"code": "MINI", "extensions": [".min"]},
    "Nintendo Virtual Boy": {"code": "VB", "extensions": [".vb", ".vboy", ".bin"]},
    "Game & Watch": {"code": "G&W", "extensions": [".mgw"]},
    "Famicom Disk System": {"code": "FDS", "extensions": [".fds"]},
    "Nintendo 3DS": {"code": "3DS", "extensions": [".3ds", ".app", ".cxi", ".cci", ".3dsx"]},
    "Nintendo Wii": {"code": "Wii", "extensions": [".gcm", ".iso", ".gcz", ".ciso", ".wbfs", ".rvz", ".dol", ".wad"]},
    "Nintendo Wii U": {"code": "WiiU", "extensions": [".wud", ".wux", ".wua"]},
    "Sony PlayStation": {"code": "PS1", "extensions": [".bin", ".cue", ".img", ".mdf", ".pbp", ".toc", ".cbn", ".m3u", ".ccd", ".chd", ".iso", ".gz"]},
    "Sony PlayStation 2": {"code": "PS2", "extensions": [".chd", ".cue", ".iso", ".isz", ".cso", ".gz"]},
    "Sony PlayStation Portable": {"code": "PSP", "extensions": [".iso", ".cso", ".pbp", ".prx"]},
    "Atari 2600": {"code": "2600", "extensions": [".a26", ".bin", ".zip"]},
    "Atari 7800": {"code": "7800", "extensions": [".a78", ".bin"]},
    "Atari Jaguar": {"code": "JAG", "extensions": [".j64", ".jag", ".rom", ".abs", ".cof", ".bin", ".prg"]},
    "Atari Jaguar CD": {"code": "JCD", "extensions": [".cue", ".cdi", ".zip"]},
    "Atari Lynx": {"code": "Lynx", "extensions": [".lnx", ".lyx", ".o"]},
    "Atari 5200": {"code": "5200", "extensions": [".xfd", ".atr", ".atx", ".cdm", ".cas", ".bin", ".a52", ".xex", ".zip"]},
    "Atari ST": {"code": "AST", "extensions": [".st", ".msa", ".zip", ".stx", ".dim", ".ipf"]},
    "Sega SG-1000": {"code": "SG1K", "extensions": [".sg", ".bin", ".zip"]},
    "Sega Master System": {"code": "SMS", "extensions": [".sms", ".bin", ".rom"]},
    "Sega Game Gear": {"code": "GG", "extensions": [".gg", ".bin", ".rom"]},
    "Sega Genesis/Mega Drive": {"code": "MD", "extensions": [".md", ".gen", ".bin", ".sg", ".smd", ".zip"]},
    "Sega Sega CD": {"code": "SCD", "extensions": [".chd", ".cue", ".iso", ".m3u"]},
    "Sega 32X": {"code": "32X", "extensions": [".32x", ".smd", ".bin", ".md", ".zip"]},
    "Sega Saturn": {"code": "SAT", "extensions": [".cue", ".chd", ".ccd", ".mds", ".iso", ".zip", ".m3u"]},
    "Sega Dreamcast": {"code": "DC", "extensions": [".lst", ".bin", ".dat", ".zip"]},
    "Sega Pico": {"code": "Pico", "extensions": [".md"]},
    "NEC PC Engine/TurboGrafx-16": {"code": "PCE", "extensions": [".pce", ".bin", ".zip"]},
    "NEC PC Engine CD/TurboGrafx-CD": {"code": "PCCD", "extensions": [".cue", ".ccd", ".chd", ".toc", ".m3u"]},
    "NEC PC-8000/8800": {"code": "80/88", "extensions": [".d88", ".u88", ".m3u"]},
    "NEC PC-FX": {"code": "PC-FX", "extensions": [".chd", ".cue", ".ccd", ".toc"]},
    "NEC PC-6000": {"code": "PC-6000", "extensions": []},
    "NEC PC-9800": {"code": "9800", "extensions": [".d98", ".zip", ".98d", ".fdi", ".fdd", ".2hd", ".tfd", ".d88", ".88d", ".hdm", ".xdf", ".dup", ".cmd", ".hdi", ".thd", ".nhd", ".hdd", ".hdn", ".cue", ".m3u"]},
    "SNK Neo Geo CD": {"code": "NGCD", "extensions": [".cue", ".iso", ".chd"]},
    "SNK Neo Geo Pocket": {"code": "NGP", "extensions": [".neo"]},
    "3DO Interactive Multiplayer": {"code": "3DO", "extensions": [".iso", ".chd", ".cue"]},
    "Amstrad CPC": {"code": "CPC", "extensions": [".dsk", ".sna", ".tap", ".cdt", ".voc", ".m3u", ".cpr", ".kcr", ".zip"]},
    "Apple II": {"code": "A2", "extensions": [".nib", ".do", ".po", ".dsk", ".woz", ".m3u", ".zip"]},
    "Arcade": {"code": "ARC", "extensions": [".zip"]},
    "Arcadia 2001": {"code": "A2001", "extensions": [".bin", ".zip", ".7z"]},
    "Arduboy": {"code": "ARD", "extensions": [".hex", ".arduboy"]},
    "ColecoVision": {"code": "CV", "extensions": [".bin", ".col", ".rom", ".zip"]},
    "Elektor TV Games Computer": {"code": "ELEK", "extensions": [".zip", ".7z"]},
    "Fairchild Channel F": {"code": "CHF", "extensions": [".bin", ".chf", ".zip"]},
    "Intellivision": {"code": "INTV", "extensions": [".int", ".bin", ".rom"]},
    "Interton VC 4000": {"code": "VC4000", "extensions": [".bin", ".zip"]},
    "Magnavox Odyssey 2": {"code": "MO2", "extensions": [".bin", ".zip", ".7z"]},
    "Mega Duck": {"code": "DUCK", "extensions": [".bin", ".zip", ".7z"]},
    "MSX": {"code": "MSX", "extensions": [".rom", ".ri", ".mx1", ".mx2", ".col", ".dsk", ".cas", ".sg", ".sc", ".m3u"]},
    "Uzebox": {"code": "UZE", "extensions": [".uze"]},
    "Vectrex": {"code": "VECT", "extensions": [".vec", ".bin", ".zip"]},
    "Watara Supervision": {"code": "WSV", "extensions": [".sv", ".zip", ".7z"]},
    "WASM-4": {"code": "WASM4", "extensions": [".wasm"]},
    "WonderSwan": {"code": "WS", "extensions": [".ws", ".wsc", ".pc2"]},
    "Amiga": {"code": "Amiga", "extensions": [".iso", ".cue", ".lha", ".chd"]},
    "Cassette Vision": {"code": "ECV", "extensions": [".bin", ".zip"]},
    "Super Cassette Vision": {"code": "ESCV", "extensions": [".bin", ".zip"]},
    "Commodore 64": {"code": "C64", "extensions": [".d64", ".d6z", ".d71", ".d7z", ".d80", ".d81", ".d82", ".d8z", ".g64", ".g6z", ".g41", ".g4z", "x64", ".x6z", ".nib", ".nbz", ".d2m", ".d4m"]},
    "FM Towns": {"code": "FMTowns", "extensions": [".m3u", ".d88", ".d77", ".xdf", ".cue", ".iso", ".game", ".cd", ".chd"]},
    "Nokia N-Gage": {"code": "N-Gage", "extensions": [".ngage", ".symbian"]},
    "Oric": {"code": "Oric", "extensions": [".dsk", ".tap"]},
    "Philips CD-i": {"code": "CD-i", "extensions": [".chd", ".cue", ".iso"]},
    "Sharp X1": {"code": "X1", "extensions": [".dx1", ".zip", ".2d", ".2hd", ".tfd", ".d88", ".88d", ".hdm", ".xdf", ".dup", ".cmd"]},
    "Sharp X68000": {"code": "X68K", "extensions": [".dim", ".img", ".d88", ".88d", ".hdm", ".dup", ".2hd", ".xdf", ".hdf", ".cmd", ".m3u"]},
    "Thomson TO8": {"code": "TO8", "extensions": [".fd", ".sap", ".k7", ".rom", ".m7", ".m5"]},
    "TI-83": {"code": "TI83", "extensions": [".rpk", ".zip"]},
    "TIC-80": {"code": "TIC-80", "extensions": [".tic"]},
    "VIC-20": {"code": "VIC-20", "extensions": [".vic"]},
    "Zeebo": {"code": "Zeebo", "extensions": []},
    "ZX81": {"code": "ZX81", "extensions": [".tzx", ".tap", ".z80", ".rzx", ".scl", ".trd"]},
    "ZX Spectrum": {"code": "ZXS", "extensions": [".tzx", ".tap", ".z80", ".rzx", ".scl", ".trd"]},
    "DOS": {"code": "DOS", "extensions": [".zip", ".dosz", ".exe", ".com", ".bat", ".iso", ".cue", ".ins", ".img", ".ima", ".vhd", ".jrc", ".tc", ".m3u", ".m3u8", ".conf"]},
    "Xbox": {"code": "Xbox", "extensions": [".iso"]}
}

# Definitions for RAHasherGUI
BASE_DIR = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) \
    else os.path.dirname(os.path.abspath(__file__))
HASH_CACHE_DIR = os.path.join(BASE_DIR, "hash_cache")

def browse_file():
    if path := filedialog.askopenfilename():
        selected_file.set(path)
        file_entry.xview_moveto(1)
        filter_system_dropdown(path)

def drop(event):
    if os.path.isfile(path := event.data.strip('{}')):
        selected_file.set(path)
        file_entry.xview_moveto(1)
        filter_system_dropdown(path)

def filter_system_dropdown(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    filtered_systems = [name for name, info in systems.items() if file_ext in info.get("extensions", [])]
    if not filtered_systems:
        filtered_systems = list(systems.keys())
    
    system_dropdown['values'] = filtered_systems
    if filtered_systems:
        system_dropdown.current(0)

def get_rahasher_path():
    paths = [os.path.join(BASE_DIR, "RAHasher.exe")]
    if getattr(sys, "frozen", False):
        paths.append(os.path.join(sys._MEIPASS, "RAHasher.exe"))
    return next((p for p in paths if os.path.exists(p)), None)
HASHER_PATH = get_rahasher_path()

def run_hasher():
    file_path = selected_file.get()
    if not file_path:
        return messagebox.showerror("Error", "Please select a ROM file.")

    if not HASHER_PATH:
        return messagebox.showerror("Error", "RAHasher.exe not found.")

    result = subprocess.run(
        [HASHER_PATH, systems[system_dropdown.get()]["code"], file_path], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

    hash_value = result.stdout.strip()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"Hash: {hash_value}\n\n")

    if not os.path.isdir(HASH_CACHE_DIR):
        return output_box.insert(tk.END, "No hash cache found.\n")

    matches_found = False

    for json_file in glob.glob(os.path.join(HASH_CACHE_DIR, "*.json")):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue

        if hash_value in data:
            for entry in data[hash_value]:
                rom_name = entry.get("rom", "Unknown")
                dump_data = entry.get("dat") or "No Data Found"
                json_name = os.path.basename(json_file)
                dump_name = json_name.replace(".json", "").replace("_", " ")
                output_box.insert(tk.END, f"Match found:\n")
                output_box.insert(tk.END, f"  Dump: {dump_name}\n")
                output_box.insert(tk.END, f"  ROM: {rom_name}\n")
                output_box.insert(tk.END, f"  Data: {dump_data}\n\n")
                matches_found = True

    if not matches_found:
        output_box.insert(tk.END, "No matches found in cached JSONs.\n")

# Application Window Setup
root = TkinterDnD.Tk()
root.title("RAHasher GUI")
root.geometry("550x455")
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
output_frame = ttk.Frame(root)
output_frame.place(x=15, y=150, width=520, height=260)
output_box = tk.Text(output_frame)
output_box.grid(row=0, column=0, sticky='nsew')
v_scroll = ttk.Scrollbar(output_frame, orient='vertical', command=output_box.yview)
v_scroll.grid(row=0, column=1, sticky='ns')
output_box.configure(yscrollcommand=v_scroll.set)
output_frame.grid_rowconfigure(0, weight=1)
output_frame.grid_columnconfigure(0, weight=1)
ttk.Button(root, text="Hash", command=run_hasher).place(x=238, y=420)
root.mainloop()
