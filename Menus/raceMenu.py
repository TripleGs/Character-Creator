#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Class Menu
class Race_Menu:
    
    def __init__(self, window):

        #Loads window data
        self.window = window
            
        #Creates frame
        self.race_screen = QWidget()
        self.race_screen_layout = QGridLayout()

        #Creates widgets
        #--RACEDROPBOX--
        self.raceselection = QComboBox()
        self.raceselection.addItems(self.window.find('5eInfo', 'Options', 'Race Options'))
        self.raceselection.setFont(self.window.active_font)
        self.raceselection.setStyleSheet(self.window.active_bordercolor)
        self.raceselection.setCurrentText(self.window.character.race)
        self.race_screen_layout.addWidget(self.raceselection,2,2,2,21,Qt.AlignTop)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.back)
        self.race_screen_layout.addWidget(self.backbutton,3,1,1,5)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.next)
        self.race_screen_layout.addWidget(self.nextbutton,3,19,1,5)
        #--LABEL--
        self.label = QLabel('Choose your Race')
        self.label.setFont(self.window.active_font)
        self.label.setStyleSheet(self.window.active_color)
        self.race_screen_layout.addWidget(self.label,1,1,1,23,Qt.AlignHCenter)
        
        self.race_screen.setLayout(self.race_screen_layout)

    #Creates the class menu
    def create(self):
        
        #Updates the screen
        self.window.setCentralWidget(self.race_screen)

    #Manages back button
    def back(self):
        self.grab_data()
        if self.window.previous_screen == 'Subclass Menu':
            self.window.create_subclass_menu()
        elif self.window.previous_screen == 'Class Menu':
            self.window.create_class_menu()
        self.window.previous_screen = 'Race Menu'

    #Manages next button
    def next(self):
        self.grab_data()
        self.window.previous_screen = 'Race Menu'
        self.window.create_subrace_menu()

    #Grabs data
    def grab_data(self):
        self.window.character.race = self.raceselection.currentText()
