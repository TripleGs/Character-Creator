#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Manages the name creation menu
class Subrace_Menu:

    def __init__(self, window):

        #Loads window data
        self.window = window

        #Creates frame
        self.subrace_screen = QWidget()
        self.subrace_screen_layout = QGridLayout()

        #Creates widgets
        #--RACESELECTION--
        self.sub_race_selection = QComboBox()
        self.sub_race_selection.addItems(self.window.find('5eInfo/Race', self.window.character.race, 'Subrace Options'))
        self.sub_race_selection.setFont(self.window.active_font)
        self.sub_race_selection.setStyleSheet(self.window.active_bordercolor)
        self.sub_race_selection.setCurrentText(self.window.character.subrace)
        self.subrace_screen_layout.addWidget(self.sub_race_selection,2,2,2,21,Qt.AlignTop)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.back)
        self.subrace_screen_layout.addWidget(self.backbutton,3,1,1,5)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.next)
        self.subrace_screen_layout.addWidget(self.nextbutton,3,19,1,5)
        #--LABEL--
        self.label = QLabel('Choose your Race')
        self.label.setFont(self.window.active_font)
        self.label.setStyleSheet(self.window.active_color)
        self.subrace_screen_layout.addWidget(self.label,1,1,1,23,Qt.AlignHCenter)
        
        self.subrace_screen.setLayout(self.subrace_screen_layout)
        
    #Creates the menu
    def create(self):

        #Updates the screen
        self.window.setCentralWidget(self.subrace_screen)

    #Manages back button
    def back(self):
        self.grab_data()
        self.window.create_race_menu()
        self.window.previous_screen = 'Subrace Menu'

    #Manages next button
    def next(self):
        self.grab_data()
        self.window.previous_screen = 'Subrace Menu'
        self.window.create_background_menu()

    #Grabs data
    def grab_data(self):
        self.window.character.subrace = self.sub_race_selection.currentText()
