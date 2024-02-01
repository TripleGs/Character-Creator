#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Manages the name creation menu
class Settings_Menu:

    def __init__(self, window):

        #Loads GUI Window info
        self.window = window
        
        #Creates frame
        self.settings_menu = QWidget()
        self.settings_menu_layout = QVBoxLayout()

        #Adds buttons
        #--FIRETHEME--
        self.firethemebutton = QPushButton('Fire Theme')
        self.firethemebutton.setFont(self.window.active_font)
        self.firethemebutton.setCheckable(True)
        self.firethemebutton.clicked.connect(self.window.set_fire_theme)
        self.firethemebutton.setStyleSheet(self.window.active_bordercolor)
        self.settings_menu_layout.addWidget(self.firethemebutton)
        #--ICETHEME--
        self.icethemebutton = QPushButton('Ice Theme')
        self.icethemebutton.setFont(self.window.active_font)
        self.icethemebutton.setCheckable(True)
        self.icethemebutton.clicked.connect(self.window.set_ice_theme)
        self.icethemebutton.setStyleSheet(self.window.active_bordercolor)
        self.settings_menu_layout.addWidget(self.icethemebutton)
        #--DEFAULTTHEME--
        self.defaultthemebutton = QPushButton('Default Theme')
        self.defaultthemebutton.setFont(self.window.active_font)
        self.defaultthemebutton.setCheckable(True)
        self.defaultthemebutton.clicked.connect(self.window.set_default_theme)
        self.defaultthemebutton.setStyleSheet(self.window.active_bordercolor)
        self.settings_menu_layout.addWidget(self.defaultthemebutton)
        #--BACKBUTTONS--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.window.create_starting_menu)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.settings_menu_layout.addWidget(self.backbutton)

        #Updates menu
        self.settings_menu.setLayout(self.settings_menu_layout)

    #Creates the menu
    def create(self):
        self.window.setCentralWidget(self.settings_menu)
        
