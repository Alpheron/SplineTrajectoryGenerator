import numpy as np
import pygame

from visualizer.utilities.utils import scaled_value, SCREEN_DIM


class Trail:
    def __init__(self, pose, screen):
        self.length = 2
        pygame.draw.circle(screen, (184, 255, 255),
                           [np.clip((scaled_value(pose.getX(), isRelative=True)), (-SCREEN_DIM + self.length),
                                    (SCREEN_DIM - self.length))
                               , np.clip(scaled_value(-pose.getY(), isRelative=True), (-SCREEN_DIM + self.length),
                                         (SCREEN_DIM - self.length))],
                           self.length)
