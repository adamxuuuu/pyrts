from util.constants import *
from util.spritesheet import SpriteSheet
from entity.tile import Tile, TileType

import pygame


class GameWorld():

    def __init__(self) -> None:

        self._gui = _GUI()

        self.grid = {}
        self.tiles = pygame.sprite.Group()

        for y in range(0, WINDOW_HEIGHT, TILE_SIZE_LARGE):
            for x in range(0, WINDOW_WIDTH, TILE_SIZE_LARGE):
                t = Tile(x, y, TileType.GRASS_32x32, self.ss)
                self.tiles.add(t)
                self.grid[(x, y)] = []

        # Blit everything to the screen
        self._gui.background.blits([(spr.image, spr.rect)
                                    for spr in self.tiles.sprites()])
        self._gui.draw()

    def draw(self, gos: pygame.sprite.Group):
        gos.clear(self._gui.screen, self._gui.background)
        gos.draw(self._gui.screen)

    def get_coord(self, x, y):
        return self.grid.get((x, y))

    def set_coord(self, x, y, obj):
        tp = self.grid.get((x, y))
        tp.append(obj)


class _GUI():

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('RTS Game')

    def __init__(self):
        # Create background
        self.background = pygame.Surface(self.SCREEN.get_size())
        self.background = self.background.convert()

    def draw(self):
        self.SCREEN.blit(self.background, (0, 0))
        pygame.display.flip()
