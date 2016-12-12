import os

from Engines.prison_data.screens.game_over_screen import GameOverScreen


class NormalCellScreen:
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def get_description(self):
        return 'You are at the ' + self.name + '.' + os.linesep + \
               self.player.get_description() + os.linesep + \
               'This cell is ok, your stay here should be bitter but bearable.'

    def get_options(self):
        return [['wait', 'Sit down at the nearest opening, wary for all possible problems.']
                ]

    def register_option(self, option):
        return {
            0: GameOverScreen(True, 10)
        }.get(option, self)
