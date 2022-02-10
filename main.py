import pygame as pg
import sys
from board import Board
from settings import *


class ChessAI:

    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_RES)
        self.board = Board(self.screen)

    def run_game(self):
        pg.init()
        pg.display.set_caption("Chess")

        # Game Loop
        while True:

            # Close Button
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            self.board.convert_fen()
            self.board.draw_board()

            pg.display.flip()


if __name__ == '__main__':
    ChessAI().run_game()
