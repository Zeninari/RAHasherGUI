import os
import json
import requests
import zipfile
import tempfile
import shutil
import re

REPO_ZIP_URL = "https://github.com/RetroAchievements/RAHashes/archive/refs/heads/master.zip"
CACHE_DIR = "hash_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def download_repo_zip(url):
    print("Downloading RAHashes repo...")
    r = requests.get(url, stream=True, timeout=30)
    r.raise_for_status()
    
    tmp_zip = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    with open(tmp_zip.name, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded to {tmp_zip.name}")
    return tmp_zip.name

def extract_zip(zip_path):
    tmp_dir = tempfile.mkdtemp()
    print(f"Extracting to {tmp_dir}...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(tmp_dir)
    return tmp_dir

def parse_and_build_cache(extracted_path):
    print("Parsing repo and building per-system JSON files...")
    
    base_folder = os.path.join(extracted_path, os.listdir(extracted_path)[0])
    
    for root, dirs, files in os.walk(base_folder):
        txt_files = [f for f in files if f.endswith(".txt")]
        if not txt_files:
            continue
        
        system_name = os.path.basename(root)
        system_code = system_name.replace(" ", "_")

        system_index = {}

        for txt_file in txt_files:
            file_path = os.path.join(root, txt_file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("\t")
                    if len(parts) < 2:
                        parts = line.split()
                    if len(parts) < 2:
                        continue

                    hash_candidate = parts[0].lower()
                    if not re.fullmatch(r"[0-9a-f]{32}", hash_candidate):
                        continue

                    rom_name = parts[1]
                    dat_type = parts[2] if len(parts) > 2 else ""

                    entry = {"rom": rom_name, "dat": dat_type}

                    if hash_candidate not in system_index:
                        system_index[hash_candidate] = []

                    if entry not in system_index[hash_candidate]:
                        system_index[hash_candidate].append(entry)

        json_path = os.path.join(CACHE_DIR, f"{system_code}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(system_index, f, indent=2)
        print(f"Saved cache for system: {system_name} -> {json_path}")

def main():
    try:
        zip_path = download_repo_zip(REPO_ZIP_URL)
        extracted_path = extract_zip(zip_path)
        parse_and_build_cache(extracted_path)
        print("All per-system JSONs are built successfully!")
    finally:
        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(extracted_path):
            shutil.rmtree(extracted_path)
        print("Temporary files cleaned up.")

if __name__ == "__main__":
    main()