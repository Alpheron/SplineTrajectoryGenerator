import sys
import time

import pygame

from neural_network.pose import Pose2D
from visualizer.field import Field
from visualizer.point import Point
from visualizer.robot import Robot
from visualizer.utils import SCREEN_DIM


class Main:

    def __init__(self, startPose, endPose):
        self.started = False
        self.startPose = startPose
        self.endPose = endPose
        self.screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])
        self.robot = Robot(screen=self.screen)
        self.field = Field(screen=self.screen)
        self.testPose = Pose2D()
        pygame.init()
        self.mainLoop()

    def updateRobot(self, pose):
        self.screen.blit(self.robot.rotate(-pose.getTheta()), self.robot.move(pose.getX(), -pose.getY()))

    def createPoints(self):
        startPoint = Point(self.startPose.getX(), -self.startPose.getY(), self.screen)
        endPoint = Point(self.endPose.getX(), -self.endPose.getY(), self.screen)
        return startPoint, endPoint

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
            self.createPoints()
            self.updateRobot(self.startPose)
            time.sleep(2)
            pygame.display.update()


if __name__ == '__main__':
    window = Main(Pose2D(-36, 0, 40), Pose2D(56, 37, 42))
