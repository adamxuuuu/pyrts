from enum import Enum
from pygame.sprite import Sprite

from util.spritesheet import SpriteSheet
from util.constants import *


class TileType(Enum):
    """tile_name = (x, y, x_offset, y_offset)"""
    BLACK_8x8 = (0, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    GRASS_8x8 = (TILE_SIZE_SMALL, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    GRASS_16x16 = (TILE_SIZE_SMALL, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    GRASS_32x32 = (12*TILE_SIZE_SMALL, 20*TILE_SIZE_SMALL,
                   TILE_SIZE_LARGE, TILE_SIZE_LARGE)
    GRASS_FLOWER_8x8 = (2*TILE_SIZE_SMALL, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    WATER = (0, TILE_SIZE_SMALL, TILE_SIZE_SMALL, TILE_SIZE_SMALL)

class Tile(Sprite):

    # Load spritesheet
    SS: SpriteSheet = SpriteSheet(
        "sprites/environment/MASGrassLand/Dawnbringer-16/MAS-Tileset-DB.png")

    def __init__(self, x, y, tt: TileType):
        Sprite.__init__(self)
        self.image = self.SS.image_at(tt.value)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
