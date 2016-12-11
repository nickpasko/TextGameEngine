from Engines.default_engine import DefaultEngine
from Engines.xogame_engine import XoGameEngine
from Runnable.game import Game

engines = [DefaultEngine(), XoGameEngine()]

def main(argv=0):
    print('Select game engine:')
    i = 0
    for engine in engines:
        print(str(i), ': ', engine.get_engine_name())
        i += 1
    print()
    engine_num = input()
    engine = engines[int(engine_num)]
    game = Game()
    game.run(engine)

main()
