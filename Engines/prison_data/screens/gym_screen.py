import os

class GymScreen:
    def __init__(self, prison_cell):
        self.name = 'Prison Gym'
        self.prison_cell = prison_cell

    def get_description(self):
        return 'You are at the ' + self.name + '.' + os.linesep + \
               self.prison_cell.player.get_description() + os.linesep + \
               'You are at the gym entrance. It is full of muscular inmates pumping iron.' + os.linesep + \
               'Many faces turn to you with questioning impressions. Some are rather aggressive.'

    def get_options(self):
        if self.authority_too_low():
            return self.receive_beating()
        return self.get_stronger()

    def register_option(self, option):
        return {
            'get_beaten': self.prison_cell,
            'back_to_cell': self.prison_cell
        }.get(option, self)

    def receive_beating(self):
        print('The men here despise you. You barely set your foot inside, and several goons materialized nearby.')
        print('"- Who do you think you are, coming here?" - asked one of them through his teeth.')
        print('You tried to fight back, but was quickly overpowered by a sheer number of them.')
        print('That sure did hurt - both physically and mentally.')
        self.prison_cell.player.health -= 10
        return [['get_beaten', 'Crawl back to your cell to heal injuries..']]

    def get_stronger(self):
        print('You have spent the rest of the day working out with different kinds of weights.')
        print('You feel rather exhausted, but in a good way. Your strength has increased.')
        self.prison_cell.player.strength += 1
        return [['back_to_cell', 'Get back to your cell']]

    def authority_too_low(self):
        return self.prison_cell.player.authority < -30
