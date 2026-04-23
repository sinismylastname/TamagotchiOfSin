import subprocess
import sys
import os

# Configuration
LCSC_ID = sys.argv[1]
LIB_PATH = "../hardware/libs"

def fetch():
    # Example command: easyeda2kicad --id C12345 --output ../hardware/libs
    try:
        subprocess.run([
            "easyeda2kicad", 
            "--id", LCSC_ID, 
            "--output", LIB_PATH,
            "--overwrite"
        ], check=True)
        print(f"Successfully ported {LCSC_ID} to local libs.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch()