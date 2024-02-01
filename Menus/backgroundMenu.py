#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Class Menu
class Background_Menu:
    
    def __init__(self, window):

        #Loads GUI Data
        self.window = window

        #Creates frame
        self.background_screen = QWidget()
        self.background_screen_layout = QGridLayout()

        #Creates widgets
        #--LABEL--
        self.label = QLabel('Choose your Background')
        self.label.setFont(self.window.active_font)
        self.label.setStyleSheet(self.window.active_color)
        self.background_screen_layout.addWidget(self.label,1,1,1,23,Qt.AlignHCenter)
        #--BACKGROUNDSELECTION--
        self.backgroundselection = QComboBox()
        self.backgroundselection.addItems(self.window.find('5eInfo', 'Options', 'Background Options'))
        self.backgroundselection.setFont(self.window.active_font)
        self.backgroundselection.setStyleSheet(self.window.active_bordercolor)
        self.backgroundselection.setCurrentText(self.window.character.background)
        self.background_screen_layout.addWidget(self.backgroundselection,2,2,2,21,Qt.AlignTop)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.back)
        self.background_screen_layout.addWidget(self.backbutton,3,1,1,5)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.next)
        self.background_screen_layout.addWidget(self.nextbutton,3,19,1,5)

        #Adds widgets
        self.background_screen.setLayout(self.background_screen_layout)

    #Creates the class menu
    def create(self):

        #Updates screen
        self.window.setCentralWidget(self.background_screen)

    #Manages next button
    def next(self):
        self.grab_data()
        self.window.previous_screen = 'Background Menu'
        self.window.create_stats_menu()
        

    #Manages back button
    def back(self):
        self.grab_data()
        self.window.previous_screen = 'Background Menu'
        self.window.create_race_menu()

    #Grabs data
    def grab_data(self):
        self.window.character.background = self.backgroundselection.currentText()
