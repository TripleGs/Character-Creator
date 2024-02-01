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
        self.label = QLabel(f'{self.window.character.name}\n{self.window.character.clas}')
        self.stats_screen_layout.addWidget(self.label)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.window.create_starting_menu)
        self.stats_screen_layout.addWidget(self.backbutton)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.window.create_race_menu)
        self.stats_screen_layout.addWidget(self.nextbutton)

        #Adds widgets
        self.stats_screen.setLayout(self.stats_screen_layout)

    #Creates the class menu
    def create(self):
        self.window.setCentralWidget(self.stats_screen)
