import os


class DefaultEngine:
    def get_engine_name(self):
        return 'Default engine showcasing the basic logic'

    def get_description(self):
        return 'You are at the big house. There is a huge door, ornamented with steel figurines of dwarfes.' \
               + os.linesep + 'What shall you do?'

    def get_options(self):
        options = [['kick', 'Kick the door out!'], ['yell', 'Yell at the door in hope someone shall hear'],
                   ['quit', 'quit this stupid game']]
        return options

    def register_option(self, option):
        return {
            0: ['no_effect', 'Door does not bulge.'],
            1: ['no effect', 'No one seems to hear.'],
            2: ['quit', 'You give up and go away.']
        }.get(option[0], ['unknown', 'Whaaat?'])

    def __init__(self):
        return
