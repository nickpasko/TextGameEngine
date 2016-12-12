import os

from Engines.prison_data.screens.bad_cell_screen import BadCellScreen
from Engines.prison_data.screens.escape_screen import EscapeScreen
from Engines.prison_data.screens.good_cell_screen import GoodCellScreen
from Engines.prison_data.screens.normal_cell_screen import NormalCellScreen


class PrisonEntranceScreen:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.bribe_sum = 100

    def get_description(self):
        return 'You are at the' + self.name + '.' + os.linesep + \
               self.player.get_description() + os.linesep + \
               'What shall you do?'

    def get_options(self):
        return [['escape', 'Try to escape!'],
                ['bribe', 'Bribe the guard'],
                ['proceed', 'Proceed silently to your cell']]

    def register_option(self, option):
        return {
            0: EscapeScreen("Prison Entrance, trying to escape", self.player),
            1: GoodCellScreen("Good Cell for prison guard friends", self.player)
                if self.player.money > self.bribe_sum
                else BadCellScreen("Bad Cell for attempted bribery", self.player),
            2: NormalCellScreen('Normal Cell', self.player)
        }.get(option, self)
