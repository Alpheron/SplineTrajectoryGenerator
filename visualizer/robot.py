import pygame

from neural_network.pose import Pose2D
from visualizer.utils import load_image, scaled_value


class Robot(pygame.sprite.Sprite):
    rect = None

    def __init__(self):
        # noinspection PyGlobalUndefined
        global rect
        pygame.sprite.Sprite.__init__(self)
        rect = load_image(18, '/home/tinku/SplineTrajectoryGenerator/visualizer/assets/Robot.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = None

    # @:param Pose2D instance of new pose where robot should be
    def setPosition(self, pose):
        # noinspection PyGlobalUndefined
        global rect
        robotPose = Pose2D(scaled_value(pose.x), scaled_value(pose.y), pose.theta)
        newPose = pygame.transform.rotate((rect.move(robotPose.x, robotPose.y)), -robotPose.theta)
        return newPose
