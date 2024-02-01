#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Manages the name creation menu
class Equipment_Menu:

    def __init__(self, window):

        self.window = window

        self.equipment_options = self.window.find('5eInfo', self.window.character.clas, 'Starting Equipment')
        
    #Creates the menu
    def create(self):
        self.window.setCentralWidget(self.create_character_menu)
        
