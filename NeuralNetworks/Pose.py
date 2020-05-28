import math
import random

import numpy as np

from Visualizer.Utils import constraint


class Pose2D:

    def __init__(self, x, y, theta, sizeConstraint=constraint):
        self.x = np.clip(x, a_min=-sizeConstraint, a_max=sizeConstraint)
        self.y = np.clip(y, a_min=-sizeConstraint, a_max=sizeConstraint)
        self.theta = self.angleWrap(theta)

    def angleWrap(self, angle):
        result = (angle + 2.0 * math.pi) % (2.0 * math.pi)
        if angle < 0.0 or angle > 2.0 * math.pi:
            return self.angleWrap(result)
        return result

    def random(self):
        randPose = Pose2D((random.uniform(-constraint, constraint)),
                          random.uniform(-constraint, constraint), (random.random()))
        return randPose
