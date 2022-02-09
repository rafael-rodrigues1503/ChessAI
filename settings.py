import os
from pygame.image import load


os.chdir('./pieces')

TILE_LENGTH = 64
SCREEN_RES = (TILE_LENGTH * 8, TILE_LENGTH * 8)
PIECES = {os.path.splitext(file)[0]: load(file) for file in os.listdir()}
COLORS = {
    "LightTile": (202, 224, 202),
    "DarkTile": (68, 94, 68),
    "ThreatenedTile": (172, 11, 11),
    "MoveTile": (77, 221, 171)
}
