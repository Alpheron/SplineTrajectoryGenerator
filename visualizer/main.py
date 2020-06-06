import sys

import pygame

from neural_network.pose import Pose2D
from visualizer.field import Field
from visualizer.robot import Robot
from visualizer.utils import SCREEN_HEIGHT


class Main:
    started = False
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_HEIGHT])
    robot = Robot()

    def __init__(self):
        self.createBackground()
        self.mainLoop()

    def updateRobot(self, pose):
        # noinspection PyGlobalUndefined
        global robot
        robot.update(Pose2D(pose.x, pose.y, pose.theta))

    def createBackground(self):
        field = Field([0, 0])
        return field

    def quitLoop(self):
        # noinspection PyGlobalUndefined
        global started
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                started = False
                pygame.quit()
                sys.exit()

    def mainLoop(self):
        # noinspection PyGlobalUndefined
        global started
        started = True
        while started:
            self.quitLoop()


if __name__ == '__main__':
    window = Main()
