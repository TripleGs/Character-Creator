#Imports for GUI
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Imports for menus
from Menus.startingMenu import Starting_Menu
from Menus.nameMenu import Name_Menu
from Menus.aboutMenu import About_Menu
from Menus.settingsMenu import Settings_Menu
from Menus.selectMenu import Select_Menu
from Menus.classMenu import Class_Menu
from Menus.backgroundMenu import Background_Menu
from Menus.statsMenu import Stats_Menu
from Menus.raceMenu import Race_Menu
from Menus.subclassMenu import Subclass_Menu
from Menus.equipmentMenu import Equipment_Menu
from Menus.shoppingMenu import Shopping_Menu
from Menus.subraceMenu import Subrace_Menu
from Menus.raceFeatureMenu import Race_Feature_Menu

#Imports for character management
from character import Character

#Child class to customize application
class Window(QMainWindow):

    #Defines window features
    def __init__(self):
        super().__init__()

        #Keeps track of previous screen
        self.previous_screen = 'None'
        
        #Creates character
        self.character = Character()
        
        #Sets Window Title/Size
        self.setWindowTitle('D&D Character Creator (1.0)')
        self.setStyleSheet('background-color: lightgrey;')
        self.window_width = self.width()
        self.window_height = self.height()

        #Font for the window
        self.cold_font = QFont("Modius 'Frigid'",20)
        self.fire_font = QFont('Open Flame', 20)
        self.default_font = QFont('Pirata One', 20)
        self.active_font = self.default_font

        #Sets Border Colors
        self.default_bordercolor = 'border :2px solid #000000; color: black'
        self.fire_bordercolor = 'border :2px solid #000000; color: darkred'
        self.cold_bordercolor = 'border :2px solid #FFFFFF; color: white'
        self.active_bordercolor = self.default_bordercolor

        #Sets Colors
        self.default_color = 'color: black;'
        self.fire_color = 'color: darkred;'
        self.cold_color = 'color: white;'
        self.active_color = self.default_color
        
        #Creates character creation menu
        self.create_starting_menu()

    #Sets window size
    def set_size(self, w, h):
        self.window_width = int(w/4)
        self.window_height = int(h/4)
        self.setFixedSize(QSize(int(self.window_width),int(self.window_height)))

    #Sets Fire Theme
    def set_fire_theme(self):
        self.active_font = self.fire_font
        self.setStyleSheet('background-color: red; color: darkred')
        self.active_bordercolor = self.fire_bordercolor
        self.active_color = self.fire_color
        self.create_settings_menu()

    #Sets Ice Theme
    def set_ice_theme(self):
        self.active_font = self.cold_font
        self.setStyleSheet('background-color: darkcyan; color: white')
        self.active_bordercolor = self.cold_bordercolor
        self.active_color = self.cold_color
        self.create_settings_menu()
        
    #Sets Default Theme
    def set_default_theme(self):
        self.active_font = self.default_font
        self.setStyleSheet('background-color: lightgrey; color: black')
        self.active_bordercolor = self.default_bordercolor
        self.active_color = self.default_color
        self.create_settings_menu()

    def find(self, location, filename, text, index = 0):
        list_needed = []
        with open(location+'/'+filename, 'r+') as file:
            for line in file:
                if line.startswith(text):
                    if index == 0:
                        line = line.split(': ')
                        list_needed = (line[1].split(', '))
                        list_needed[-1] = list_needed[-1].split('\n')
                        list_needed[-1] = list_needed[-1][0]
                    else:
                        line = line.split(': ')
                        line[index] = line[index].split('\n')
                        list_needed = line[index][0]
                        
        return list_needed

    #Creates and loads character selection menu
    def create_character_selection_menu(self):

        self.select_menu = Select_Menu(self)
        self.select_menu.create()

    #Creates and loads settings menu
    def create_settings_menu(self):

        self.settings_menu = Settings_Menu(self)
        self.settings_menu.create()

    #Creates and loads about menu
    def create_about_menu(self):

        self.about_menu = About_Menu(self)
        self.about_menu.create()

    #Creates the starting menu
    def create_starting_menu(self):

        self.starting_menu = Starting_Menu(self)
        self.starting_menu.create()

    #Creates the name tab for the character creation menu
    def create_name_menu(self):

        self.name_menu = Name_Menu(self)
        self.name_menu.create()
        
    #Creates the class tab for the character creation menu
    def create_class_menu(self):

        self.class_menu = Class_Menu(self)
        self.class_menu.create()

    #If the level is qualifies the character for an archetype
    def create_subclass_menu(self):

        self.subclass_menu = Subclass_Menu(self)
        self.subclass_menu.create()
        
    #Creates the background tab for the character creation menu
    def create_background_menu(self):

        self.background_menu = Background_Menu(self)
        self.background_menu.create()
        
    #Creates the race tab for character creation menu
    def create_race_menu(self):

        self.race_menu = Race_Menu(self)
        self.race_menu.create()

    #Creates the stats menu
    def create_stats_menu(self):

        self.stats_menu = Stats_Menu(self)
        self.stats_menu.create()

    #Creates the race feature menu
    def create_race_feature_menu(self):

        self.race_feature_menu = Race_Feature_Menu(self)
        self.race_feature_menu.create()

    #Creates the subrace selection menu
    def create_subrace_menu(self):

        self.subrace_menu = Subrace_Menu(self)
        self.subrace_menu.create()
    
        
#Creates app and gets screen dimensions
app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
        
#Creates the widget to be our window and stores screen dimensions
window = Window()
window.set_size(1000,2000)

#Shows the window
window.show()

#Starts the event loop
app.exec()
