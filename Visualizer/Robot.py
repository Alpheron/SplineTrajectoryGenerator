from NeuralNetworks.Pose import Pose2D


# import window size

class Robot:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.robotPose = Pose2D(self.x, self.y, self.theta)


#    def scaledPosition(self, pose2d):


robbit = Robot(4, 10, 30)
# print(robbit.scaledPosition(robbit.robotPose))

boop = Pose2D(40, 60, 370)
print(boop.theta)
