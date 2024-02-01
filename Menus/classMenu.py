#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Class Menu
class Class_Menu:

    def __init__(self, window):

        #Loads GUI Data
        self.window = window

        #Creates the widgets for menu
        self.class_screen = QWidget()
        self.class_screen_layout = QGridLayout()

        #Create widgets
        #--CLASSSELECTION--
        self.classselection = QComboBox()
        self.classselection.addItems(self.window.find('5eInfo','Options','Class Options'))
        self.classselection.setFont(self.window.active_font)
        self.classselection.setStyleSheet(self.window.active_bordercolor)
        self.classselection.setCurrentText(self.window.character.clas)
        self.class_screen_layout.addWidget(self.classselection,2,9,2,14,Qt.AlignTop)
        #--LEVELSELECTION--
        self.levelselection = QComboBox()
        self.levelselection.addItems(self.window.find('5eInfo','Options','Level Options'))
        self.levelselection.setFont(self.window.active_font)
        self.levelselection.setStyleSheet(self.window.active_bordercolor)
        self.levelselection.setCurrentText(self.window.character.level)
        self.class_screen_layout.addWidget(self.levelselection,2,2,2,7,Qt.AlignTop)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.back)
        self.class_screen_layout.addWidget(self.backbutton,3,1,1,5)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.next)
        self.class_screen_layout.addWidget(self.nextbutton,3,19,1,5)
        #--MENULABEL--
        self.label = QLabel('Choose your Class')
        self.label.setFont(self.window.active_font)
        self.label.setStyleSheet(self.window.active_color)
        self.class_screen_layout.addWidget(self.label,1,1,1,23,Qt.AlignHCenter)
        
        self.class_screen.setLayout(self.class_screen_layout)

    #Creates the class menu
    def create(self):

        #Updates screen
        self.window.setCentralWidget(self.class_screen)

    #Manages next button
    def next(self):
        self.grab_data()
        self.window.previous_screen = 'Class Menu'
        
        #Checks the level
        if int(self.levelselection.currentText()) >= int(self.window.find('5eInfo/Class',self.window.character.clas, 'Subclass Level', 1)):
            self.window.create_subclass_menu()
        else:
            self.window.character.subclass = ''
            self.window.create_race_menu()

    #Manages back button
    def back(self):
        self.grab_data()
        self.window.previous_screen = 'Class Menu'
        self.window.create_name_menu()

    #Grabs data
    def grab_data(self):
        self.window.character.clas = self.classselection.currentText()
        self.window.character.level = self.levelselection.currentText()
    
            

