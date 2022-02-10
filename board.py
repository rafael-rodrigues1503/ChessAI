import pygame as pg
from piece import Piece
from itertools import product
from settings import *


class Board:

    def __init__(self, screen):
        self.screen = screen
        self.fen = START_FEN
        self.tiles = [[0 for _ in range(8)] for _ in range(8)]

    def convert_fen(self):
        symbol_dict = {
            'k': Piece().king, 'p': Piece().pawn, 'n': Piece().knight,
            'b': Piece().bishop, 'r': Piece().rook, 'q': Piece().queen
        }
        fen_board = self.fen.split()[0]
        x, y = 0, 7

        for char in fen_board:
            if char == '/':
                x = 0
                y -= 1
            elif char.isnumeric():
                x += int(char)
            else:
                piece_color = Piece().white if char.isupper() else Piece().black
                piece_type = symbol_dict[char.lower()]
                self.tiles[7 - y][x] = piece_color | piece_type
                x += 1

    def draw_board(self):
        for y, x in product(range(8), range(8)):

            # Draw Tile
            tile_rect = pg.Rect(TILE_LENGTH * x, TILE_LENGTH * y, TILE_LENGTH, TILE_LENGTH)
            tile_color = COLORS["LightTile"] if not (x + y) % 2 else COLORS["DarkTile"]
            pg.draw.rect(self.screen, tile_color, tile_rect)

            # Draw Piece
            if self.tiles[y][x]:
                png = PIECES_PNG[self.tiles[y][x]]
                png_rect = png.get_rect()
                png_rect.center = tile_rect.center
                self.screen.blit(png, png_rect)
