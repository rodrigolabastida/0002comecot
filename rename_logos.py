import os
import shutil
import unicodedata
import re

download_dir = "/Users/rodrigolabastida/Documents/COMECOT/downloaded_logos/Logo del medio (File responses)"
target_dir = "/Users/rodrigolabastida/Documents/COMECOT/logos"

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

# The mapping from the specific file names downloaded to the canonical media names.
# Based on the gdown output strings:
mapping = {
    "telemedios": "TELEMEDIOS",
    "pixel 3000": "1b3e85", 
    "índice media": "39E9A7AA", 
    "noticias mr": "ccf00b7b",
    "dt noticias": "E1366F4A",
    "gentetlx": "GenteTlx",
    "cobertura nacional": "IMG_7563",
    "¿qué pasa tlaxcala?": "IMG_8405",
    "la bestia política": "IMG-20260422-WA0252 - Edgar García", 
    "línea de contraste": "IMG-20260422-WA0252 - Viridiana",
    "el regional": "LOGO  EL REGIONAL",
    "agencia informativa": "Logo Agencia Informativa",
    "385 grados": "logo con 385",
    "estilo tlax": "logo Estilo",
    "generación press": "Screenshot_2026-04-22",
    "tlaxcala digital": "TLAXCALA Digital",
    "tv red tlaxcala": "tv red",
    "tv zacatelco": "ZACATELCO SIN FONDO"
}

if not os.path.exists(download_dir):
    print("Download directory not found.")
    exit(1)

downloaded_files = os.listdir(download_dir)

for target_name, match_str in mapping.items():
    slug = slugify(target_name)
    # find file
    matched_file = None
    for f in downloaded_files:
        if match_str.lower() in f.lower():
            matched_file = f
            break
            
    if matched_file:
        ext = matched_file.split('.')[-1].lower()
        if ext not in ['jpg', 'jpeg', 'png', 'gif']:
            ext = 'png' # default fallback
            
        src = os.path.join(download_dir, matched_file)
        dest = os.path.join(target_dir, f"{slug}.{ext}")
        shutil.copy2(src, dest)
        print(f"Mapped {matched_file} -> {dest}")
    else:
        print(f"Warning: Could not find match for {target_name} (using key '{match_str}')")

# Then run original generate_cards but allowing the new extensions.
