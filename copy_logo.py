import os
import glob
import shutil

brain_dir = "/Users/rodrigolabastida/.gemini/antigravity/brain/a08dd62c-d153-43cf-9553-7b83392016e5"
target_logo = "/Users/rodrigolabastida/Documents/COMECOT/logo.jpeg"

# Find all media files
media_files = glob.glob(os.path.join(brain_dir, "media__*.jpg"))

if media_files:
    # Sort by modification time (newest last)
    media_files.sort(key=os.path.getmtime)
    newest_media = media_files[-1]
    
    # Copy to workspace
    shutil.copy2(newest_media, target_logo)
    print(f"Successfully copied {newest_media} to {target_logo}")
else:
    print("No media files found.")
