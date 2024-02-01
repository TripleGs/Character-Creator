#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
    
#Manages the name creation menu
class Name_Menu:

    def __init__(self, window):

        #Defines the window
        self.window = window
        
        #Creates the frame
        self.name_screen = QWidget()
        self.name_screen_layout = QGridLayout()

        #Creates widgets
        #--TEXT--
        self.label = QLabel('Enter your name')
        self.label.setWordWrap(True)
        self.label.setFont(self.window.active_font)
        self.label.setStyleSheet(self.window.active_color)
        self.name_screen_layout.addWidget(self.label,2,1,1,23,Qt.AlignHCenter)
        #--ENTRYBOX--
        self.entrybox = QLineEdit()
        self.entrybox.setFont(self.window.active_font)
        self.entrybox.setText(self.window.character.name)
        self.entrybox.setStyleSheet(self.window.active_bordercolor)
        self.name_screen_layout.addWidget(self.entrybox,3,2,2,21,Qt.AlignTop)
        #--BACKBUTTON--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.back)
        self.name_screen_layout.addWidget(self.backbutton,4,1,1,5)
        #--NEXTBUTTON--
        self.nextbutton = QPushButton('Next')
        self.nextbutton.setFont(self.window.active_font)
        self.nextbutton.setStyleSheet(self.window.active_bordercolor)
        self.nextbutton.setCheckable(True)
        self.nextbutton.clicked.connect(self.next)
        self.name_screen_layout.addWidget(self.nextbutton,4,19,1,5)

        self.name_screen.setLayout(self.name_screen_layout)

    #Creates the menu
    def create(self):

        #Updates the screen
        self.window.setCentralWidget(self.name_screen)

    #Manages next button
    def next(self):
        self.grab_data()
        self.window.previous_screen = 'Name Menu'
        self.window.create_class_menu()

    #Manages back button
    def back(self):
        self.grab_data()
        self.window.previous_screen = 'Name Menu'
        self.window.create_starting_menu()


    #Grabs data
    def grab_data(self):
        self.window.character.name = self.entrybox.text()
        
