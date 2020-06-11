import numpy as np
import pygame

from visualizer.utils import scaled_value, SCREEN_DIM


class Trail:
    def __init__(self, x, y, screen):
        self.length = 10
        pygame.draw.circle(screen, (255, 85, 0),
                           [np.clip((scaled_value(x, isRelative=True)), (-SCREEN_DIM + self.length),
                                    (SCREEN_DIM - self.length))
                               , np.clip(scaled_value(y, isRelative=True), (-SCREEN_DIM + self.length),
                                         (SCREEN_DIM - self.length))],
                           self.length)
