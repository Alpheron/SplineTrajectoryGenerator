import pygame

from visualizer.utils import scaled_value


class Point:
    def __init__(self, x, y, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           [scaled_value(x, isRelative=True), scaled_value(y, isRelative=True, isHeight=True)], 10)
