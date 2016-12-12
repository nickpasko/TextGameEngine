from Engines.default_engine import DefaultEngine
from Engines.xogame_engine import XoGameEngine
from Runnable.game import Game

engines = [DefaultEngine(), XoGameEngine()]

def main(argv=0):
    print('Select game engine:')
    for i, engine in enumerate(engines):
        print(str(i), ': ', engine.__doc__)
    print()
    engine_num = input()
    engine = engines[int(engine_num)]
    game = Game()
    game.run(engine)

main()
