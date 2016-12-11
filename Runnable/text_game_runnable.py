import os

from Engine.engine_api import GameEngine


def cls():
    print("\n" * 100)
    # os.system('cls' if os.name == 'nt' else 'clear')


def main(argv=0):
    engine = GameEngine()
    result = ['', '']
    while True:
        cls()
        print(result[1])
        description = engine.get_description()
        print(description)
        options = engine.get_options()
        i = 1
        for option in options:
            print(str(i), ': ', option[1])
            i += 1
        print('choose option (1, 2, 3):')
        option = input(':')
        result = engine.register_option(option)

        if result[0] == 'quit':
            break


main()
