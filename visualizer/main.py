import sys

import pygame

from neural_network.pose import Pose2D
from visualizer.sprites.field import Field
from visualizer.sprites.point import Point
from visualizer.sprites.robot import Robot
from visualizer.sprites.trail import Trail
from visualizer.utilities.data_logger import DataLogger
from visualizer.utilities.trajectory import Trajectory
from visualizer.utilities.utils import SCREEN_DIM


class Main:

    def __init__(self, trajectory):
        self.started = False
        self.trajectory = trajectory
        self.screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])
        self.robot = Robot(screen=self.screen)
        self.field = Field(screen=self.screen)
        self.trailList = []
        self.DataLogger = DataLogger(self.screen)
        pygame.init()
        self.mainLoop()

    def updateRobot(self, pose):
        self.screen.blit(self.robot.rotate(-pose.getTheta()), self.robot.move(pose.getX(), -pose.getY()))
        self.trailList.append(pose)

    def createTrail(self):
        x = 0
        while x < len(self.trailList):
            Trail(self.trailList[x], self.screen)
            x += 1

    def createPoints(self):
        startPoint = Point(self.trajectory[0].getX(), -self.trajectory[0].getY(), self.screen)
        endPoint = Point(self.trajectory[-1].getX(),
                         -self.trajectory[-1].getY(), self.screen)
        return startPoint, endPoint

    def drawRobotAndTrail(self, counter):
        try:
            self.updateRobot(self.trajectory[counter])
            self.createTrail()
        except IndexError:
            self.updateRobot(self.trajectory[-1])
            self.createTrail()

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
        counter = 0
        while started:
            self.quitLoopConditional()
            self.screen.fill([255, 255, 255])
            self.screen.blit(self.field.image, self.field.rect)
            self.DataLogger.displayText("Test")
            self.createPoints()
            self.drawRobotAndTrail(counter)
            pygame.display.update()
            counter += 1


if __name__ == '__main__':
    trajectory = Trajectory(Pose2D(-50, 13, 20), Pose2D(29, 18, -40))
    trajectory.line(Pose2D(-50, 13, 20), Pose2D(0, -13, 20))
    trajectory.turn(Pose2D(0, -13, -20))
    trajectory.simultaneousMotionTurn(Pose2D(29, 18, -40))
    trajectory.end()
    window = Main(trajectory.poseList)
