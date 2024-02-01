#Imports
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Manages the name creation menu
class Select_Menu:

    def __init__(self, window):

        #Loads GUI window
        self.window = window
        
        #Creates frame
        self.select_character_menu = QWidget()
        self.select_character_menu_layout = QVBoxLayout()

        dir_list = os.listdir('./Characters')
        for file in dir_list:
            if '.txt' in file:
                self.button = QPushButton(file)
                self.button.setFont(self.window.active_font)
                self.button.setCheckable(True)
                self.button.clicked.connect(self.makechar)
                self.button.setStyleSheet(self.window.active_bordercolor)
                self.select_character_menu_layout.addWidget(self.button,2)
            
        #Adds buttons
        #--BACKBUTTONS--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.window.create_starting_menu)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.select_character_menu_layout.addWidget(self.backbutton,2)

        #Updates menu
        self.select_character_menu.setLayout(self.select_character_menu_layout)

    #Creates the menu
    def create(self):
        self.window.setCentralWidget(self.select_character_menu)

    #Displays Character Info
    def makechar(self):
        #Need to add a section that scans the file for all
        #of the info and stores it to character
        #To do this it will find the file based on the buttons text
        print(self.button.text())
        self.window.create_stats_menu()
        
