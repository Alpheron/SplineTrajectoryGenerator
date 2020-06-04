import math
import random

import numpy as np

from Visualizer.Utils import constraint


class Pose2D:

    def __init__(self, x, y, theta):
        self.x = np.clip(x, a_min=-constraint, a_max=constraint)
        self.y = np.clip(y, a_min=-constraint, a_max=constraint)
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
