from typing import List, Sequence, Tuple, Union, overload

from pygame.sprite import Sprite
from pygame.math import Vector2
import math

from util.loader import load_png


class Dummy(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_png('gameobjects/Ice.png')
        # screen = get_surface()
        # self.area = screen.get_rect()
        self.dest = Vector2(x, y)
        self.rect.center = (x, y)
        self.speed = 0.3  # pix per milis

    def update(self, dt):
        newpos = self.__calcnewpos__(dt)
        if newpos:
            self.rect = newpos

    def __calcnewpos__(self, dt):
        if not self.dest or self.dest.distance_to(Vector2(self.rect.center)) < 3.:
            return None
        rads = math.atan2(self.dest.y - self.rect.centery,
                          self.dest.x - self.rect.centerx)
        rads %= 2 * math.pi
        (dx, dy) = (self.speed * math.cos(rads), self.speed * math.sin(rads))
        return self.rect.move(dx * dt, dy * dt)

    def moveto(self, pos: Vector2):
        self.dest = pos

    def moveto(self, x: float, y: float):
        self.dest = Vector2(x, y)

    def moveto(self, pos: Tuple):
        self.dest = Vector2(pos)
