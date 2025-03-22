# Dir move with module shutil
import shutil
# Import create modules
from move_dir import move_dir
from paths import Paths
from regex import Regex

# Create a news instances of Paths and Regex
paths = Paths()
regex = Regex()

dict_paths = {
            'CALC/TRAINING/LEFT':regex.listas(regex.Ca_trai_p_LEFT), 
            'CALC/TRAINING/RIGHT':regex.listas(regex.Ca_trai_p_RIGHT), 
            'CALC/TEST/LEFT':regex.listas(regex.Ca_test_p_LEFT), 
            'CALC/TEST/RIGHT':regex.listas(regex.Ca_test_p_RIGHT), 
            'MASS/TRAINING/LEFT': regex.listas(regex.Mass_trai_p_LEFT), 
            'MASS/TRAINING/RIGHT': regex.listas(regex.Mass_trai_p_RIGHT),
            'MASS/TEST/LEFT': regex.listas(regex.Mass_test_p_LEFT), 
            'MASS/TEST/RIGHT': regex.listas(regex.Mass_test_p_RIGHT),
}

for destine, other_re in dict_paths.items():
    move_dir(path_orige=paths.path_orige, path_destine=paths.destinePath(destine),
             list_elements=other_re)
