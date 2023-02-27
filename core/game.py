import random
import pygame
from pygame.locals import *
from pygame.math import Vector2

from entity.ball import Ball
from entity.tile import Tile, TileType
from core.grid import Grid
from util.constants import *
from util.spritesheet import SpriteSheet


class Game:

    def __init__(self):
        # Set up the game window
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('RTS Game')

        SS = SpriteSheet(
            "sprites/environment/MASGrassLand/Dawnbringer-16/MAS-Tileset-DB.png")

        # Create background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        grid = Grid(SS, self.background)

        # Create game objects
        self.balls = pygame.sprite.Group()
        for _ in range(100):
            _b = Ball(random.randrange(10, 790), random.randrange(10, 590))
            self.balls.add(_b)

        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        # Set up the clock
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.dt = 0

        # End
        self.running = True

    def run(self):
        # Main game loop
        while self.running:

            self.__event__()

            self.__tick__()

            self.__render__()

            # Limit frame rate
            self.dt = self.clock.tick(self.FPS)

        pygame.quit()

    def __event__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    for b in self.balls.sprites():
                        b.moveto(event.pos)

    def __tick__(self):
        self.balls.update(self.dt)

    def __render__(self):
        self.balls.clear(self.screen, self.background)
        self.balls.draw(self.screen)
        pygame.display.flip()
