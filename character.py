#Manages the character
class Character:
    
    def __init__(self):
        self.name = ''
        self.clas = ''
        self.background = ''
        self.race = ''
        self.subclass = ''
        self.level = ''
        self.inventory = ''
        self.subrace = ''

    def res(self):
        self.name = ''
        self.subclass = ''
        self.clas = ''
        self.background = ''
        self.race = ''
        self.level = ''
        self.inventory = ''
        self.subrace = ''

    def __str__(self):
        return f'Name: {self.name}\nClasses: {self.clas}\nRace: {self.race}\nBackground: {self.background}'
