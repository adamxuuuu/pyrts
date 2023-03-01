import random
import pygame
from pygame.locals import *

from entity.dummy import Dummy
from core.gameworld import GameWorld
from util.constants import *


class Game:

    def __init__(self):
        # Set up the game window
        pygame.init()
        self.gameworld = GameWorld()

        # Create game objects
        self.balls = pygame.sprite.Group()
        for _ in range(10):
            _b = Dummy(random.randrange(10, 790), random.randrange(10, 590))
            self.balls.add(_b)

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
        self.gameworld.draw(self.balls)
        pygame.display.flip()
