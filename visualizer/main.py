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
        self.robot = Robot(trajectory=self.trajectory, screen=self.screen)
        self.field = Field(screen=self.screen)
        self.points = Point(self.trajectory, self.screen)
        self.trailList = []
        self.DataLogger = DataLogger(self.screen)
        pygame.init()
        self.mainLoop()

    def mainLoop(self):
        self.started = True
        counter = 0
        while self.started:
            quitLoopConditional(self.started)
            self.screen.fill([255, 255, 255])
            self.screen.blit(self.field.image, self.field.rect)
            self.points.createPoints()
            self.DataLogger.displayText("Test")
            self.robot.drawRobotAndTrail(counter)
            pygame.display.update()
            counter += 1


if __name__ == '__main__':
    trajectory = Trajectory(Pose2D(-50, 13, 20), Pose2D(29, 18, -40))
    trajectory.line(Pose2D(-50, 13, 20), Pose2D(0, -13, 20))
    trajectory.turn(Pose2D(0, -13, -20))
    trajectory.simultaneousMotionTurn(Pose2D(29, 18, -40))
    trajectory.end()
    window = Main(trajectory.poseList)
