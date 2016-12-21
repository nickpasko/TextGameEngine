import os

from Engines.prison_data.screens.bad_cell_screen import BadCellScreen
from Engines.prison_data.screens.game_over_screen import GameOverScreen


class EscapeScreen:
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def get_description(self):
        return 'You are trying to escape the prison!' + os.linesep + \
            self.player.get_description() + os.linesep + \
            'You have to decide quickly!'

    def get_options(self):
        return [['sprint', 'Try to sprint pass the guards, while dodging them'],
                   ['brawl', 'Brawl with the guards, wrecking havoc'],
                   ['trick', 'Trick the guards and slip away']]

    def register_option(self, option):
        return {
            'sprint': GameOverScreen(True, 0, "dodging all the guards and running away")
                if self.player.agility >= 7 and self.player.dexterity >= 7
                else BadCellScreen("Bad Cell for attempted runaway", self.player),
            'brawl': GameOverScreen(True, 0, 'smashing the nearest guard forcing your way out')
                if self.player.strength >= 8 and self.player.dexterity >= 5
                else BadCellScreen("Bad Cell for attempted assault", self.player),
            'trick': GameOverScreen(True, 0, 'throwing in a bunch of gold to make guards look away, while silently slipping out the front door')
                if self.player.intelligence >= 5 and self.player.dexterity >= 8 and self.player.money >= 75
                else BadCellScreen("Bad Cell for attempted runaway", self.player),
        }.get(option, self)
