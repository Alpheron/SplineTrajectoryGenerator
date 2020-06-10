import pygame

from visualizer.utils import load_image


class Robot(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(18, '/home/tinku/SplineTrajectoryGenerator/visualizer/assets/Robot.png')
        self.rect = self.image.get_rect()
        self.rect.center = [400, 400]

    # @:param Pose2D instance of new pose where robot should be
    def setPosition(self, pose):
        self.rect.center = [750, 100]
        # robotPose = Pose2D(scaled_value(pose.x, isRelative=True), scaled_value(pose.y, isRelative=True), pose.theta)
        # print(robotPose.y)
        # surface = pygame.Surface((self.rect.width, self.rect.height))
        # newPose = pygame.transform.rotate(surface, -robotPose.theta)
        # return newPose
