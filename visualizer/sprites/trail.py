import numpy as np
import pygame

from visualizer.utilities.utils import scaled_value, SCREEN_DIM


class Trail:
    def __init__(self, trailList, screen):
        self.length = 3
        self.trailList = trailList
        self.screen = screen

    def drawSingularTrail(self, pose):
        pygame.draw.circle(self.screen, (184, 255, 255),
                           [np.clip((scaled_value(pose.getX(), isRelative=True)), (-SCREEN_DIM + self.length),
                                    (SCREEN_DIM - self.length))
                               , np.clip(scaled_value(-pose.getY(), isRelative=True), (-SCREEN_DIM + self.length),
                                         (SCREEN_DIM - self.length))],
                           self.length)

    def createTrail(self):
        x = 0
        while x < len(self.trailList):
            self.drawSingularTrail(self.trailList[x])
            x += 1
