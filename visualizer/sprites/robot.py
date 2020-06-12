from math import degrees

import pygame

from visualizer.sprites.trail import Trail
from visualizer.utilities.utils import load_image, scaled_value


class Robot(pygame.sprite.Sprite):

    def __init__(self, trajectory, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(18, '/home/tinku/SplineTrajectoryGenerator/visualizer/assets/Robot.png')
        self.transFormImage = None
        self.rect = self.image.get_rect()
        self.rect.center = [400, 400]
        self.trajectory = trajectory
        self.trailList = []
        self.screen = screen
        self.Trail = Trail(self.trailList, self.screen)

    def move(self, x, y):
        newRobotRect = self.transFormImage.get_rect()
        newRobotRect.center = tuple([scaled_value(x, isRelative=True), scaled_value(y, isRelative=True)])
        constrainedRect = newRobotRect.clamp(self.screen.get_rect())
        return constrainedRect

    def rotate(self, angle):
        rot_image = pygame.transform.rotate(self.image, degrees(angle))
        rot_rect = rot_image.get_rect()
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.transFormImage = rot_image
        return rot_image

    def updateRobot(self, pose):
        self.screen.blit(self.rotate(-pose.getTheta()), self.move(pose.getX(), -pose.getY()))
        self.trailList.append(pose)

    def drawRobotAndTrail(self, counter):
        try:
            self.updateRobot(self.trajectory[counter])
            self.Trail.createTrail()
        except IndexError:
            self.updateRobot(self.trajectory[-1])
            self.Trail.createTrail()
