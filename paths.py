from pathlib import Path
class Paths:
    """This class store the directories paths"""
    def __init__(self):
        # Path orige
        self.path_orige = Path('C:/Users/ma-nu/Downloads/carpeta_origen')
        # Path destine Calc
        self.destine_path_Ca_trai_LEFT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/CALC/TRAINING/LEFT')
        self.destine_path_Ca_trai_RIGHT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/CALC/TRAINING/RIGHT')
        self.destine_path_Ca_test_LEFT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/CALC/TEST/LEFT')
        self.destine_path_Ca_test_RIGHT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/CALC/TEST/RIGHT')
        # Path destine Mass
        self.destine_path_Mass_trai_LEFT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/MASS/TRAINING/LEFT')
        self.destine_path_Mass_trai_RIGHT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/MASS/TRAINING/RIGHT')
        self.destine_path_Mass_test_LEFT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/MASS/TEST/LEFT')
        self.destine_path_Mass_test_RIGHT = Path('C:/Users/ma-nu/Downloads/carpeta_destino/MASS/TEST/RIGHT')

        
