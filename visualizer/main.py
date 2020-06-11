import sys
from math import radians, degrees

import pygame

from neural_network.pose import Pose2D
from visualizer.point import Point
from visualizer.utils import DEFAULT_STEP_SIZE


class Main:

    def __init__(self, startPose, endPose):
        self.started = False
        self.startPose = startPose
        self.endPose = endPose
        # self.screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])
        # self.robot = Robot(screen=self.screen)
        # self.field = Field(screen=self.screen)
        # self.poseList = []
        # self.calculatePoses()
        self.calculateHeading()
        # pygame.init()
        # self.mainLoop()

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

    def calculatePoses(self):
        rateOfX = (self.endPose.getX() - self.startPose.getX()) / DEFAULT_STEP_SIZE
        rateOfY = (self.endPose.getY() - self.startPose.getY()) / DEFAULT_STEP_SIZE
        x = 0
        while x < DEFAULT_STEP_SIZE:
            x += 1
            pose = Pose2D(self.startPose.getX() + (x * rateOfX), self.startPose.getY() + (x * rateOfY),
                          self.startPose.getTheta())
            print("Pose: " + str(pose.getX()) + ", " + str(pose.getY()) + ", " + str(pose.getTheta()))
            self.poseList.append(pose)

    def calculateHeading(self):
        changeTheta = radians(self.startPose.getTheta()) - degrees(self.endPose.getTheta())
        print(changeTheta)

    def mainLoop(self):
        # noinspection PyGlobalUndefined
        global started
        started = True
        counter = 0
        while started:
            self.quitLoopConditional()
            self.screen.fill([255, 255, 255])
            self.screen.blit(self.field.image, self.field.rect)
            self.createPoints()
            try:
                self.updateRobot(self.poseList[counter])
            except IndexError:
                pass
            counter += 1
            pygame.display.update()


if __name__ == '__main__':
    window = Main(Pose2D(-72, 0, 0), Pose2D(56, 37, 45))
