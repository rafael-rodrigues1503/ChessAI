import pygame as pg
from itertools import product
from settings import *


class Board:

    def __init__(self, screen):
        self.screen = screen
        self.matrix = [
            ['RD', 'ND', 'BD', 'QD', 'KD', 'BD', 'ND', 'RD'],
            ['PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD'],
            ['',  '',  '',  '',  '',  '',  '',  ''],
            ['',  '',  '',  '',  '',  '',  '',  ''],
            ['',  '',  '',  '',  '',  '',  '',  ''],
            ['',  '',  '',  '',  '',  '',  '',  ''],
            ['PL', 'PL', 'PL', 'PL', 'PL', 'PL', 'PL', 'PL'],
            ['RL', 'NL', 'BL', 'QL', 'KL', 'BL', 'NL', 'RL'],
        ]

    def draw_board(self):
        for y, x in product(range(8), range(8)):
            tile_rect = pg.Rect(TILE_LENGTH * x, TILE_LENGTH * y, TILE_LENGTH, TILE_LENGTH)
            tile_color = COLORS["LightTile"] if not (x + y) % 2 else COLORS["DarkTile"]
            pg.draw.rect(self.screen, tile_color, tile_rect)

            if self.matrix[y][x]:
                png = PIECES[self.matrix[y][x]]
                png_rect = png.get_rect()
                png_rect.center = tile_rect.center
                self.screen.blit(png, png_rect)
