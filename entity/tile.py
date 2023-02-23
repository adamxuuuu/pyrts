import pygame
from enum import Enum
from pygame.sprite import Sprite

from util.spritesheet import SpriteSheet
from util.constants import *


class TileType(Enum):
    BLACK_8x8 = (0, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    GRASS_8x8 = (TILE_SIZE_SMALL, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    GRASS_32x32 = (12*TILE_SIZE_SMALL, 20*TILE_SIZE_SMALL,
                   TILE_SIZE_LARGE, TILE_SIZE_LARGE)
    GRASS_FLOWER_8x8 = (2*TILE_SIZE_SMALL, 0, TILE_SIZE_SMALL, TILE_SIZE_SMALL)
    WATER = (0, TILE_SIZE_SMALL, TILE_SIZE_SMALL, TILE_SIZE_SMALL)


class Tile(Sprite):
    def __init__(self, x, y, tt: TileType, ss: SpriteSheet):
        Sprite.__init__(self)
        self.xx = 3
        self.yy = 6
        self.image = ss.image_at(tt.value)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # def __init__(self, x, y):
    #     Sprite.__init__(self)
    #     self.xx = 3
    #     self.yy = 6
    #     self.image = SS.image_at((0, 0, 32, 32))
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (x, y)


def test():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tile Demo')

    # Create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    tiles = pygame.sprite.Group()
    tt = TileType.GRASS_32x32
    for y in range(0, 600, tt.value[3]):
        for x in range(0, 800, tt.value[2]):
            tile = Tile(x, y, tt)
            tiles.add(tile)
            background.blit(tile.image, tile.rect)

    clock = pygame.time.Clock()
    # game loop
    running = True
    while running:

        # check for events (keyboard, mouse, etc.)
        for event in pygame.event.get():

            # check if the user closed the window
            if event.type == pygame.QUIT:

                # if so, end the game loop
                running = False

        # update all game logic here

        # draw/render
        # Blit everything to the screen
        screen.blit(background, (0, 0))

        # after drawing everything, flip the display
        pygame.display.flip()

        # run at 60 fps
        clock.tick(60)

    # quit pygame and close the window when done
    pygame.quit()
