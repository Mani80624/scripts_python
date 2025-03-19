# Dir move with module shutil
import shutil
# Module for evite conflics with Paths
from pathlib import Path

def move_dir(path_orige,path_destine, list_elements):
    for folder in list_elements:
        root_path = Path(f'C:/Users/ma-nu/Downloads/carpeta_origen/{folder}')
        # Method move for move directories
        shutil.move(root_path, path_destine)