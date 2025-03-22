# Regular expression module
import re
# Modules locals
from listar_carpeta import listar_carpetas
from paths import Paths

class Regex:
    """This class store attributes of regular expression"""
    def __init__(self):
        """Initialize of attributes"""
        # Atributes Calc
        self.Ca_trai_p_LEFT = re.compile(r'^Calc-Training.*LEFT_CC$')
        self.Ca_trai_p_RIGHT = re.compile(r'^Calc-Training.*RIGHT_CC$')
        self.Ca_test_p_LEFT = re.compile(r'^Calc-Test.*LEFT_CC$')
        self.Ca_test_p_RIGHT = re.compile(r'^Calc-Test.*RIGHT_CC$')

        # Atrivutes Mass
        self.Mass_trai_p_LEFT = re.compile(r'^Mass-Training.*LEFT_CC$')
        self.Mass_trai_p_RIGHT = re.compile(r'^Mass-Training.*RIGHT_CC$')
        self.Mass_test_p_LEFT = re.compile(r'^Mass-Test.*LEFT_CC$')
        self.Mass_test_p_RIGHT = re.compile(r'^Mass-Test.*RIGHT_CC$')
        self.paths = Paths()

    def listas(self, regular_expresion):
        """This function is used for create lists in regex (regular expression)"""
        # Origin Path list
        folders = listar_carpetas(self.paths.path_orige)
        lista_regular = [folder for folder in folders if regular_expresion.match(folder)]
        
        return lista_regular