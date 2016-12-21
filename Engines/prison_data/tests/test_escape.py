from Engines.prison_data.player_person import PlayerPerson
from Engines.prison_data.screens.bad_cell_screen import BadCellScreen
from Engines.prison_data.screens.escape_screen import EscapeScreen
from Engines.prison_data.screens.game_over_screen import GameOverScreen



def test_agile_dextrous_should_escape():
    """Option 0: outrun. Should succeed."""
    agile_dextrous_person = PlayerPerson("Agile and dextrous Person")
    agile_dextrous_person.agility = 10
    agile_dextrous_person.dexterity = 10
    escape_screen = EscapeScreen("Escape zone", agile_dextrous_person)
    result_screen = escape_screen.register_option(0)
    return result_screen.__class__ == GameOverScreen(True, 0).__class__


def test_slow_clumsy_should_fail():
    """Option 0: outrun. Should fail."""
    slow_clumsy_person = PlayerPerson("Slow and clumsy Person")
    slow_clumsy_person.agility = 1
    slow_clumsy_person.dexterity = 1
    escape_screen = EscapeScreen("Escape zone", slow_clumsy_person)
    result_screen = escape_screen.register_option(0)
    return result_screen.__class__ == BadCellScreen("Bad Cell", slow_clumsy_person).__class__


def test_strong_dextrous_should_escape():
    """Option 1: brawl. Should succeed."""
    strong_dextrous_person = PlayerPerson("Strong and agile Person")
    strong_dextrous_person.strength = 10
    strong_dextrous_person.dexterity= 10
    escape_screen = EscapeScreen("Escape zone", strong_dextrous_person)
    result_screen = escape_screen.register_option(1)
    return result_screen.__class__ == GameOverScreen(True, 0).__class__


def test_weak_clumsy_should_fail():
    """Option 1: brawl. Should fail."""
    weak_clumsy_person = PlayerPerson("Weak and clumsy Person")
    weak_clumsy_person.strength = 1
    weak_clumsy_person.dexterity = 1
    escape_screen = EscapeScreen("Escape zone", weak_clumsy_person)
    result_screen = escape_screen.register_option(1)
    return result_screen.__class__ == BadCellScreen("Bad Cell", weak_clumsy_person).__class__


def test_clever_stealthy_wealthy_should_escape():
    """Option 2: feint. Should succeed."""
    clever_stealthy_person = PlayerPerson("Clever and stealthy Person with some Money")
    clever_stealthy_person.intelligence = 10
    clever_stealthy_person.dexterity = 10
    clever_stealthy_person.money = 100
    escape_screen = EscapeScreen("Escape zone", clever_stealthy_person)
    result_screen = escape_screen.register_option(2)
    return result_screen.__class__ == GameOverScreen(True, 0).__class__


def test_stupid_clumsy_should_fail():
    """Option 2: feint. Should fail."""
    stupid_clumsy_person = PlayerPerson("Weak and clumsy Person")
    stupid_clumsy_person.intelligence = 1
    stupid_clumsy_person.dexterity = 1
    stupid_clumsy_person.money = 0
    escape_screen = EscapeScreen("Escape zone", stupid_clumsy_person)
    result_screen = escape_screen.register_option(2)
    return result_screen.__class__ == BadCellScreen("Bad Cell", stupid_clumsy_person).__class__


print("test_strong_dextrous_should_escape: ", test_agile_dextrous_should_escape())
print("test_slow_clumsy_should_fail: ", test_slow_clumsy_should_fail())
print("test_strong_dextrous_should_escape: ", test_strong_dextrous_should_escape())
print("test_weak_clumsy_should_fail: ", test_weak_clumsy_should_fail())
print("test_clever_stealthy_wealthy_should_escape: ", test_clever_stealthy_wealthy_should_escape())
print("test_stupid_clumsy_should_fail: ", test_stupid_clumsy_should_fail())
