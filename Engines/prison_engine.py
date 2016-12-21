from Engines.prison_data.player_person import PlayerPerson
from Engines.prison_data.screens.prison_entrance_screen import PrisonEntranceScreen


class PrisonEngine:
    """SR2-like Prison game engine"""

    # engine members
    def __init__(self):
        self.current_screen = PrisonEntranceScreen("Prison Entrance", PlayerPerson("Qwerty Uiop"))

    def get_description(self):
        return self.current_screen.get_description()

    def get_options(self):
        return self.current_screen.get_options()

    def register_option(self, option):
        if option[1] == 'quit':
            return ['quit', 'Game Over.']
        new_screen = self.current_screen.register_option(option[1])
        self.current_screen = new_screen
        return ['', '']

        # internal mambers
