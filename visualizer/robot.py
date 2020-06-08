import pygame

from neural_network.pose import Pose2D
from visualizer.utils import load_image, scaled_value


class Robot(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(18, '/home/tinku/SplineTrajectoryGenerator/visualizer/assets/Robot.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]

    # @:param Pose2D instance of new pose where robot should be
    def setPosition(self, pose):
        robotPose = Pose2D(scaled_value(pose.x), scaled_value(pose.y), pose.theta)
        self.rect.move(robotPose.x, robotPose.y)
        surface = pygame.Surface((self.rect.width, self.rect.height))
        newPose = pygame.transform.rotate(surface, -robotPose.theta)
        return newPose
