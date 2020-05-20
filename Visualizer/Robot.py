from NeuralNetworks.Pose import Pose2D
from Visualizer.Utils import loadImage
from Visualizer.Utils import scaledVal


class Robot:
    def __init__(self):
        loadImage(18, '/home/tinku/SplineTrajectoryGenerator/Visualizer/Assets/Robot.png')

    # @:param Pose2D instance of new pose where robot should be
    def setPosition(self, pose):
        robotPose = Pose2D(scaledVal(pose.x), scaledVal(pose.y), pose.theta)
        return robotPose
