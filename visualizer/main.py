import sys

import pygame

from neural_network.pose import Pose2D
from visualizer.field import Field
from visualizer.robot import Robot
from visualizer.utils import SCREEN_DIM


class Main:

    def __init__(self):
        self.started = False
        self.screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])
        self.robot = Robot()
        self.field = Field()
        self.testPose = Pose2D(5, 6, 7)
        pygame.init()
        self.mainLoop()

    def updateRobot(self, pose):
        self.robot.setPosition(Pose2D(pose.x, pose.y, pose.theta))

    def quitLoopConditional(self):
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
            self.quitLoopConditional()
            self.screen.fill([255, 255, 255])
            self.screen.blit(self.field.image, self.field.rect)
            self.screen.blit(self.robot.image, self.robot.rect)
            self.updateRobot(self.testPose.random())
            pygame.display.update()


if __name__ == '__main__':
    window = Main()
