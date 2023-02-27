from util.constants import *
from entity.tile import Tile, TileType

import pygame

class Grid():

    def __init__(self, SS, background):
        self.grid = {}
        self.tiles = pygame.sprite.Group()

        for y in range(0, 600, TILE_SIZE_LARGE):
            for x in range(0, 800, TILE_SIZE_LARGE):
                t = Tile(x, y, TileType.GRASS_32x32, SS)
                self.tiles.add(t)
                self.grid[(x, y)] = []
                background.blit(t.image, t.rect)

    def get_coord(self, x, y) -> list:
        return self.grid.get((x, y))
    
    def set_coord(self, x, y, obj):
        tp = self.grid.get((x, y))
        tp.append(obj)


