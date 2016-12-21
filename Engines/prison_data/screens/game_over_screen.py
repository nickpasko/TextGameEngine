import os


class GameOverScreen:
    def __init__(self, alive, term, escape_reason=''):
        self.alive = alive
        self.term = term
        self.escape_reason = escape_reason

    def get_description(self):
        if not self.alive:
            return 'You are dead!'
        message = ''
        if self.term == 0:
            message += 'You have successfully escaped the prison by ' + self.escape_reason + '!'
        else:
            message += 'You will probablyleave the prison in ' + str(self.term) + ' years.'
        return message

    def get_options(self):
        return [['quit', 'Game Over.']]

    def register_option(self, option):
        return {
            'quit': GameOverScreen(self.alive, self.term)
        }.get(option, self)
