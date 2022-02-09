import pygame as pg
import sys
from board import Board
from settings import *


class ChessAI:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(SCREEN_RES)
        pg.display.set_caption("Chess")

        self.board = Board(self.screen)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            self.screen.fill((255, 0, 0))
            self.board.draw_board()
            pg.display.flip()


if __name__ == '__main__':
    ChessAI()
