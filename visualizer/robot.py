from math import degrees

import pygame

from visualizer.utils import load_image, scaled_value


class Robot(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(18, '/home/tinku/SplineTrajectoryGenerator/visualizer/assets/Robot.png')
        self.rect = self.image.get_rect()
        self.rect.center = [400, 400]
        self.screen = screen

    def move(self, x, y):
        newRobotRect = tuple([scaled_value(x, isRelative=True), scaled_value(y, isRelative=True)])
        print(scaled_value(x, isRelative=True))
        print(scaled_value(y, isRelative=True))
        return newRobotRect

    def rotate(self, angle):
        rot_image = pygame.transform.rotate(self.image, degrees(angle))
        rot_rect = rot_image.get_rect()
        rot_image = rot_image.subsurface(rot_rect).copy()
        rot_rect.clamp(self.screen.get_rect())
        # print(self.screen.get_rect())
        return rot_image
