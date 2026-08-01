import os
import shutil
import sys

# Console output contains emoji; Windows defaults to cp1252, which cannot
# encode them.
sys.stdout.reconfigure(encoding="utf-8")

ROSTER = [
    "Zenthos",
    "Melancholia",
    "Sylas",
    "Brutus",
    "Lyra",
    "Vesper",
    "Ignacia",
    "Nereus"
]

PICTURES_DIR = os.path.expanduser("~/Pictures")
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VOICE_DIR = os.path.join(PROJECT_DIR, "voice_samples")
CHARACTERS_DIR = os.path.join(PROJECT_DIR, "characters")

def setup_character_directories():
    print("--- Organizing 8-Character Subdirectories ---")
    
    # 1. Ensure ~/Pictures/<Character>/ subdirectories exist
    for char in ROSTER:
        pic_char_dir = os.path.join(PICTURES_DIR, char)
        os.makedirs(pic_char_dir, exist_ok=True)
        print(f"📁 Picture Asset Directory: {pic_char_dir}")

    # 2. Ensure project characters/<Character>/ subdirectories exist
    for char in ROSTER:
        proj_char_dir = os.path.join(CHARACTERS_DIR, char)
        os.makedirs(proj_char_dir, exist_ok=True)
        
        # Sub-folders for dialogue scripts, audio recordings, and 3D models
        os.makedirs(os.path.join(proj_char_dir, "audio"), exist_ok=True)
        os.makedirs(os.path.join(proj_char_dir, "sprites"), exist_ok=True)
        os.makedirs(os.path.join(proj_char_dir, "models_3d"), exist_ok=True)
        print(f"📁 Project Asset Directory: {proj_char_dir}")

if __name__ == "__main__":
    setup_character_directories()
