from NeuralNetworks.Pose import Pose2D
from Visualizer.Utils import loadImage
from Visualizer.Utils import scaledVal


class Robot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadImage(18, '/home/tinku/SplineTrajectoryGenerator/Visualizer/Assets/Robot.png')
        screen = pygame.display.get_surface()
        self.area - screen.get_rect()
        self.vector = None

    # @:param Pose2D instance of new pose where robot should be
    def setPosition(self, pose, rect=self.rect):
        robotPose = Pose2D(scaledVal(pose.x), scaledVal(pose.y), pose.theta)
        newPose = pygame.transform.rotate((rect.move(robotPose.x, robotPose.y)), -robotPose.theta)
        return newPose
