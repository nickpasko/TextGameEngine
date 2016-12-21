import os

from Engines.prison_data.screens.game_over_screen import GameOverScreen


class BadCellScreen:
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def get_description(self):
        return 'You are at the ' + self.name + '.' + os.linesep + \
               self.player.get_description() + os.linesep + \
               'This cell is awful, overcrowded with lots of sick people - both in terms of health and attitude.'

    def get_options(self):
        return [['wait', 'Prepare to rot here.']
                ]

    def register_option(self, option):
        return {
            'wait': GameOverScreen(True, 15)
        }.get(option, self)
