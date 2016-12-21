import os

from Engines.prison_data.screens.game_over_screen import GameOverScreen


class GoodCellScreen:
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def get_description(self):
        return 'You are at the ' + self.name + '.' + os.linesep + \
               self.player.get_description() + os.linesep + \
               'This cell is rather good, so your stay here should be fine.'

    def get_options(self):
        return [['wait', 'Lay down on your couch and wait out your term in comparative comfort.']
                ]

    def register_option(self, option):
        return {
            'wait': GameOverScreen(True, 10)
        }.get(option, self)
