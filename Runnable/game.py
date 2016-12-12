def cls():
    print("\n" * 100)
    # os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        pass

    def run(self, engine):
        result = ['', '']
        while True:
            cls()
            print(result[1])
            print(engine.get_description())
            options = engine.get_options()
            for i, option in enumerate(options):
                print(str(i), ': ', option[1])
            print('choose option:')
            user_option = int(input(':'))
            selected_option = options[user_option]
            result = engine.register_option([user_option, selected_option[0]])

            if result[0] == 'quit':
                print(engine.get_description())
                print(result[1])
                break
