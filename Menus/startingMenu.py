#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Starting_Menu():

    def __init__(self, window):

        #Loads GUI data
        self.window = window

        #Resets character data
        self.window.character.res()
        
        #Creates frame
        self.starting_menu = QWidget()
        self.starting_menu_layout = QGridLayout()

        #--HOLDERS--
        self.holderleft = QWidget()
        self.starting_menu_layout.addWidget(self.holderleft,1,1,1,3)
        self.holderright = QWidget()
        self.starting_menu_layout.addWidget(self.holderright,7,3,1,3)
        #--TITLE--
        self.titlelabel = QLabel('D&D 5E Character Creator')
        self.titlelabel.setWordWrap(True)
        self.titlelabel.setFont(self.window.active_font)
        self.titlelabel.setAlignment(Qt.AlignCenter)
        self.titlelabel.setStyleSheet(self.window.active_color)
        self.starting_menu_layout.addWidget(self.titlelabel,2,2,1,3)
        #--SELECTBUTTON--
        self.selectbutton = QPushButton('Select Character')
        self.selectbutton.setFont(self.window.active_font)
        self.selectbutton.setCheckable(True)
        self.selectbutton.clicked.connect(self.window.create_character_selection_menu)
        self.selectbutton.setStyleSheet(self.window.active_bordercolor)
        self.starting_menu_layout.addWidget(self.selectbutton,3,2,1,3)
        #--CREATEBUTTON--
        self.createbutton = QPushButton('Create Character')
        self.createbutton.setFont(self.window.active_font)
        self.createbutton.setCheckable(True)
        self.createbutton.clicked.connect(self.window.create_name_menu)
        self.createbutton.setStyleSheet(self.window.active_bordercolor)
        self.starting_menu_layout.addWidget(self.createbutton,4,2,1,3)
        #--SETTINGSBUTTON--
        self.settingsbutton = QPushButton('Settings')
        self.settingsbutton.setFont(self.window.active_font)
        self.settingsbutton.setCheckable(True)
        self.settingsbutton.clicked.connect(self.window.create_settings_menu)
        self.settingsbutton.setStyleSheet(self.window.active_bordercolor)
        self.starting_menu_layout.addWidget(self.settingsbutton,5,2,1,3)
        #--ABOUTBUTTON--
        self.aboutbutton = QPushButton('About')
        self.aboutbutton.setFont(self.window.active_font)
        self.aboutbutton.setCheckable(True)
        self.aboutbutton.clicked.connect(self.window.create_about_menu)
        self.aboutbutton.setStyleSheet(self.window.active_bordercolor)
        self.starting_menu_layout.addWidget(self.aboutbutton,6,2,1,3)

        #Sets layout and sets menu
        self.starting_menu.setLayout(self.starting_menu_layout)
        
    #Creates the starting window
    def create(self):
        self.window.setCentralWidget(self.starting_menu)
