import sys

import pygame

from neural_network.pose import Pose2D
from visualizer.field import Field
from visualizer.point import Point
from visualizer.robot import Robot
from visualizer.utils import SCREEN_DIM


class Main:

    def __init__(self):
        self.started = False
        self.screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])
        self.robot = Robot()
        self.field = Field()
        self.testPose = Pose2D()
        pygame.init()
        self.mainLoop()

    def updateRobot(self, pose):
        self.robot.setPosition(Pose2D(pose.getX(), pose.getyY(), pose.getTheta()))

    def createPoints(self, startPose, endPose):
        startPoint = Point(startPose.getX(), startPose.getY(), self.screen)
        print(startPose.getX())
        print(startPose.getY())
        print("---------------------")
        endPoint = Point(endPose.getX(), endPose.getY(), self.screen)
        print(endPose.getX())
        print(endPose.getY())
        print("---------------------")

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
            self.createPoints(Pose2D(-36, 0), Pose2D(36, 1))
            pygame.display.update()


if __name__ == '__main__':
    window = Main()
