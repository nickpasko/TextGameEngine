import os
import random

from Engines.prison_data.screens.game_over_screen import GameOverScreen


class NormalCellScreen:
    def __init__(self, name, player, game_context):
        self.name = name
        self.player = player
        self.game_context = game_context

    def get_description(self):
        return 'You are at the ' + self.name + '.' + os.linesep + \
               self.game_context.get_description() + os.linesep + \
               self.player.get_description() + os.linesep + \
               'This cell is ok, your stay here should be bitter but bearable.'

    def get_options(self):
        if self.game_context.days_left == 0:
            return [['quit', 'You did yur term. Time to bail out.']]
        options = []
        if self.game_context.get_weekday() == 1 or self.game_context.get_weekday() == 3 or self.game_context.get_weekday() == 5:
            options.append(['workout', 'Work out at the gym'])
        if self.game_context.get_weekday() == 2 or self.game_context.get_weekday() == 4 or self.game_context.get_weekday() == 6:
            options.append(['study', 'Study at the library'])
        if self.game_context.get_weekday() == 7:
            options.append(['pray', 'Pray at the local chapel'])
        options.append(['eat', 'Eat at the prison cantine'])
        options.append(['work', 'Work where the guards tell you to'])
        return options

    def register_option(self, option):
        self.game_context.tick_day()
        if option == 'workout':
            self.player.strength += 1
            print('You have become stronger.')
            return self
        if option == 'study':
            self.player.intelligence += 1
            print('You have become smarter.')
            return self
        if option == 'pray':
            print('You have brought peace to your soul.')
            return self
        if option == 'eat':
            print('You have restored some of your health.')
            return self
        if option == 'work':
            money = random.randint(1, 10)
            self.player.money += money
            print('You have earned a little money: ', money, '.')
            return self
        if option == 'quit':
            return GameOverScreen(True, self.player, 'Your term is over!')
