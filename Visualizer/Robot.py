import Visualizer.Main
from NeuralNetworks.Pose import Pose2D


class Robot:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.robotPose = Pose2D(self.scaledX(x), self.scaledY(y), self.theta)

    def scaledX(self, x):
        scaledX = x * Visualizer.Main.Main.screenHeight
        return scaledX

    def scaledY(self, y):
        scaledY = y * Visualizer.Main.Main.screenHeight
        return scaledY

    # def loadImage(self, pathToImage):
