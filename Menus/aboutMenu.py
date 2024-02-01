#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Manages the name creation menu
class About_Menu:

    def __init__(self, window):

        #GUI Window
        self.window = window
        
        #Defines menu
        self.about_menu = QWidget()
        self.about_menu_layout = QVBoxLayout()
        
        #Creates/adds text
        self.about_text = QLabel('Created by: Joseph A. Goss\n'+
                                 'Hello, I a freshmen Computer Data Science student and'+
                                 'creator of this app.')
        self.about_text.setWordWrap(True)
        self.about_text.setFont(self.window.active_font)
        self.about_menu_layout.addWidget(self.about_text)

        #Creates/adds buttons
        #--BACKBUTTONS--
        self.backbutton = QPushButton('Back')
        self.backbutton.setFont(self.window.active_font)
        self.backbutton.setCheckable(True)
        self.backbutton.clicked.connect(self.window.create_starting_menu)
        self.backbutton.setStyleSheet(self.window.active_bordercolor)
        self.about_menu_layout.addWidget(self.backbutton)

        #Creates the layout
        self.about_menu.setLayout(self.about_menu_layout)

    #Creates the menu
    def create(self):
        self.window.setCentralWidget(self.about_menu)
        
