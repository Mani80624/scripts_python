# Dir move with module shutil
import shutil
# Import create modules
from move_dir import move_dir
from paths import Paths
from regex import Regex

# Create a news instances of Paths and Regex
paths = Paths()
regex = Regex()

# Create the lists of regex aplication
regex.listas()

# Move orige directories to destine directories.
# Calc-Test and Training
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Ca_trai_LEFT, 
         list_elements=regex.Ca_tr_p_left)
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Ca_trai_RIGHT, 
         list_elements=regex.Ca_tr_p_right)
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Ca_test_LEFT, 
         list_elements=regex.Ca_tes_p_left)
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Ca_test_RIGHT, 
         list_elements=regex.Ca_tes_p_right)

# Mass-Test and Training
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Mass_trai_LEFT, 
         list_elements=regex.Ma_tr_p_left)
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Mass_trai_RIGHT, 
         list_elements=regex.Ma_tr_p_right)
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Mass_test_LEFT, 
         list_elements=regex.Ma_te_p_left)
move_dir(path_orige=paths.path_orige, path_destine=paths.destine_path_Mass_test_RIGHT, 
         list_elements=regex.Ma_te_p_right)