from pathlib import Path
class Paths:
    """This class store the directories paths"""
    def __init__(self):
        # Path orige
        self.path_orige = Path('C:/Users/ma-nu/Downloads/carpeta_origen')

    def destinePath(self, particular_path):
        destine_path = Path(f'C:/Users/ma-nu/Downloads/carpeta_destino/{particular_path}')
        return destine_path

        
