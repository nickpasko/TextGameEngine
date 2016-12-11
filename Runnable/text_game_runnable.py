from Engine.engine_api import GameEngine
from Runnable.game import Game


def main(argv=0):
    engine = GameEngine()
    game = Game()
    game.run(engine)

main()
