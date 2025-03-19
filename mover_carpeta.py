# Dir move with module shutil
import shutil
# Module for evite conflics with Paths
from pathlib import Path

# Paths orige and destine
destine_path = Path('C:\\Users\ma-nu\Downloads\carpeta_destino')
root_path = Path(f'C:\\Users\ma-nu\Downloads\carpeta_origen\carpeta mover 1')

# Method move for move directories
shutil.move(root_path, destine_path)

