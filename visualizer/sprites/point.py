import numpy as np
import pygame

from visualizer.utilities.utils import SCREEN_DIM
from visualizer.utilities.utils import scaled_value


class Point:
    def __init__(self, trajectory, screen):
        self.trajectory = trajectory
        self.screen = screen
        self.length = 10

    def createPoints(self):
        startPoint = self.draw(self.trajectory[0].getX(), -self.trajectory[0].getY())
        endPoint = self.draw(self.trajectory[-1].getX(), -self.trajectory[-1].getY())
        return startPoint, endPoint

    def draw(self, x, y):
        point = pygame.draw.circle(self.screen, (255, 0, 0),
                                   [np.clip((scaled_value(x, isRelative=True)), (-SCREEN_DIM + self.length),
                                            (SCREEN_DIM - self.length))
                                       , np.clip(scaled_value(y, isRelative=True), (-SCREEN_DIM + self.length),
                                                 (SCREEN_DIM - self.length))],
                                   self.length)
        return point
