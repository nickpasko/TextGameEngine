import os
import random


class PlayerPerson:
    def __init__(self, name):
        self.name = name
        self.strength = random.randint(1, 10)
        self.agility = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.dexterity = random.randint(1, 10)
        self.money = random.randint(50, 150)

    def get_description(self):
        return 'Your strength is ' + str(self.strength) + os.linesep + \
               'Your agility is ' + str(self.agility) + os.linesep + \
               'Your dexterity is ' + str(self.dexterity) + os.linesep + \
               'Your intelligence is ' + str(self.intelligence) + os.linesep + \
                'You have ' + str(self.money) + ' gold on you.'
