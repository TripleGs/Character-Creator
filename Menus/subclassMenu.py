#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Manages the name creation menu
class Subclass_Menu:

    def __init__(self, window):

        #Loads window data
        self.window = window

        #Creates frame
        self.subclass_menu = QWidget()
        self.subclass_menu_layout = QGridLayout()

        #Adds buttons
        #--LABEL--
        self.label = QLabel('Choose your Subclass')
        self.label.setFont(self.window.active_font)
        self.label.setStyleSheet(self.window.active_color)
        self.subclass_menu_layout.addWidget(self.label,1,1,1,23,Qt.AlignHCenter)
        #--SUBCLASS SELECTION--
        self.subclassselection = QComboBox()
        self.subclassselection.addItems(self.window.find('5eInfo/Class',self.window.character.clas,'Subclass Options'))
        self.subclassselection.setFont(self.window.active_font)
        self.subclassselection.setStyleSheet(self.window.active_bordercolor)
        self.subclassselection.setCurrentText(self.window.character.subclass)
        self.subclass_menu_layout.addWidget(self.subclassselection,2,2,2,21,Qt.AlignTop)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.next)
        self.subclass_menu_layout.addWidget(self.nextbutton,3,19,1,5)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.back)
        self.subclass_menu_layout.addWidget(self.backbutton,3,1,1,5)

        #Updates menu
        self.subclass_menu.setLayout(self.subclass_menu_layout)

    #Creates the menu
    def create(self):
        
        self.window.setCentralWidget(self.subclass_menu)

    #Manages back button
    def back(self):
        self.grab_data()
        self.window.previous_screen = 'Subclass Menu'
        self.window.create_class_menu()
        
    #Manages next button
    def next(self):
        self.grab_data()
        self.window.previous_screen = 'Subclass Menu'
        self.window.create_race_menu()
        
    #Collects data
    def grab_data(self):
        self.window.character.subclass = self.subclassselection.currentText()
        
        
