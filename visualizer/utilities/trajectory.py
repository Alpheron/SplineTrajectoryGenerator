from neural_network.pose import Pose2D
from visualizer.utilities.utils import DEFAULT_STEP_SIZE


class Trajectory:
    def __init__(self, startPose, endPose, robot=None):
        self.startPose = startPose
        self.endPose = endPose
        self.poseList = []
        self.poseList.append(startPose)
        self.robot = robot
        self.counter = 0

    def simultaneousMotionTurn(self, pose2):
        lastPosition = self.poseList[(self.counter * DEFAULT_STEP_SIZE) - 1]
        rateOfX = (pose2.getX() - lastPosition.getX()) / DEFAULT_STEP_SIZE
        rateOfY = (pose2.getY() - lastPosition.getY()) / DEFAULT_STEP_SIZE
        rateOfTheta = (pose2.getTheta() - lastPosition.getTheta()) / DEFAULT_STEP_SIZE
        x = 0
        while x < DEFAULT_STEP_SIZE:
            pose = Pose2D(lastPosition.getX() + (x * rateOfX), lastPosition.getY() + (x * rateOfY),
                          lastPosition.getTheta() + (x * rateOfTheta))
            print("Pose: " + str(pose.getX()) + ", " + str(pose.getY()) + ", " + str(pose.getTheta()))
            self.poseList.append(pose)
            x += 1
        self.counter += 1

    def line(self, pose2):
        lastPosition = self.poseList[(self.counter * DEFAULT_STEP_SIZE) - 1]
        rateOfX = (pose2.getX() - lastPosition.getX()) / DEFAULT_STEP_SIZE
        rateOfY = (pose2.getY() - lastPosition.getY()) / DEFAULT_STEP_SIZE
        x = 0
        while x < DEFAULT_STEP_SIZE:
            pose = Pose2D(lastPosition.getX() + (x * rateOfX), lastPosition.getY() + (x * rateOfY),
                          lastPosition.getTheta())
            print("Pose: " + str(pose.getX()) + ", " + str(pose.getY()) + ", " + str(pose.getTheta()))
            self.poseList.append(pose)
            x += 1
        self.counter += 1

    def turn(self, pose1):
        lastPosition = self.poseList[(self.counter * DEFAULT_STEP_SIZE) - 1]
        angleChange = (pose1.getTheta() - lastPosition.getTheta()) / DEFAULT_STEP_SIZE
        x = 0
        while x < DEFAULT_STEP_SIZE:
            pose = Pose2D(pose1.getX(), pose1.getY(),
                          pose1.getTheta() + (x * angleChange))
            self.poseList.append(pose)
            x += 1
        self.counter += 1

    def end(self):
        self.poseList.append(self.endPose)
        print(
            "Pose: " + str(self.endPose.getX()) + ", " + str(self.endPose.getY()) + ", " + str(self.endPose.getTheta()))
