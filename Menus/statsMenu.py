#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Class Menu
class Stats_Menu:
    
    def __init__(self, window):
        
        #Loads GUI Data
        self.window = window

        #Creates frame
        self.stats_screen = QWidget()
        self.stats_screen_layout = QVBoxLayout()

        #Creates widgets
        #--STATS--
        self.label = QLabel(f'{self.window.character}')
        self.stats_screen_layout.addWidget(self.label)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.window.create_starting_menu)
        self.stats_screen_layout.addWidget(self.backbutton)
        #--SAVEBUTTON--
        self.savebutton = QPushButton('Save')
        self.savebutton.setFont(self.window.active_font)
        self.savebutton.setCheckable(True)
        self.savebutton.clicked.connect(self.save_character)
        self.savebutton.setStyleSheet(self.window.active_bordercolor)
        self.stats_screen_layout.addWidget(self.savebutton)

        #Adds widgets
        self.stats_screen.setLayout(self.stats_screen_layout)

    #Creates the class menu
    def create(self):

        #Updates Screen
        self.window.setCentralWidget(self.stats_screen)

        #Sets current screen as previous screen
        self.window.previous_screen = 'Stats Menu'
        
    #Saves the file
    def save_character(self):
        filename = 'Characters/'+self.window.character.name + '.txt'
        with open(filename, 'a+') as file:
            file.write(f'{self.window.character}')
