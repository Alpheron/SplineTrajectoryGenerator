import sys
import time

import pygame

from neural_network.pose import Pose2D
from visualizer.sprites.field import Field
from visualizer.sprites.point import Point
from visualizer.sprites.robot import Robot
from visualizer.utilities.data_logger import DataLogger
from visualizer.utilities.trajectory import Trajectory
from visualizer.utilities.utils import SCREEN_DIM, quitLoopConditional


class Main:

    def __init__(self, trajectory):
        self.started = False
        self.trajectory = trajectory
        self.screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])
        self.screen.set_alpha(None)
        pygame.event.set_allowed([pygame.QUIT])
        self.clock = pygame.time.Clock()
        self.robot = Robot(self.trajectory, screen=self.screen)
        self.field = Field(screen=self.screen)
        self.points = Point(self.trajectory, self.screen)
        self.DataLogger = DataLogger(self.trajectory, self.clock, self.screen)
        self.current = time.time()
        pygame.init()
        self.mainLoop()

    def mainLoop(self):
        self.started = True
        counter = 0
        while self.started:
            quitLoopConditional(self.started)
            self.clock.tick(70)
            self.screen.fill([255, 255, 255])
            self.screen.blit(self.field.image, self.field.rect)
            self.points.createPoints()
            self.DataLogger.renderDashboard(counter)
            self.robot.drawRobotAndTrail(counter)
            if counter == len(self.trajectory):
                stop = time.time()
                print(stop - self.current)
                sys.exit()
            pygame.display.update()
            counter += 1


if __name__ == '__main__':
    trajectory = Trajectory(Pose2D(-72 + 9, 0, 7.87), Pose2D(72 - 9, 0, 7.87))
    trajectory.line(Pose2D(72 - 9, 0, 7.87))
    trajectory.end()
    window = Main(trajectory.poseList)
