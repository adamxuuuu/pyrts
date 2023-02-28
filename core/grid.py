from util.constants import *
from util.spritesheet import SpriteSheet
from entity.tile import Tile, TileType

import pygame

class Grid():

    def __init__(self):
        # Create screen
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('RTS Game')

        # Load spritesheet
        self.SS = SpriteSheet(
            "sprites/environment/MASGrassLand/Dawnbringer-16/MAS-Tileset-DB.png")
        self.grid = {}
        self.tiles = pygame.sprite.Group()

        # Create background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()

        for y in range(0, 600, TILE_SIZE_LARGE):
            for x in range(0, 800, TILE_SIZE_LARGE):
                t = Tile(x, y, TileType.GRASS_32x32, self.SS)
                self.tiles.add(t)
                self.grid[(x, y)] = []
        
        # Blit everything to the screen
        self.background.blits([(spr.image, spr.rect) for spr in self.tiles.sprites()])
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def draw(self, gos):
        gos.clear(self.screen, self.background)
        gos.draw(self.screen)

    def get_coord(self, x, y) -> list:
        return self.grid.get((x, y))
    
    def set_coord(self, x, y, obj):
        tp = self.grid.get((x, y))
        tp.append(obj)


