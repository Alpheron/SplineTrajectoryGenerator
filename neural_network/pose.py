import math
import random

import numpy as np

from visualizer.utils import CONSTRAINT


class Pose2D:

    def __init__(self, x, y, theta):
        self.x = np.clip(x, a_min=-CONSTRAINT, a_max=CONSTRAINT)
        self.y = np.clip(y, a_min=-CONSTRAINT, a_max=CONSTRAINT)
        self.theta = self.angleWrap(theta)

    def angleWrap(self, angle):
        result = (angle + 2.0 * math.pi) % (2.0 * math.pi)
        if angle < 0.0 or angle > 2.0 * math.pi:
            return self.angleWrap(result)
        return result

    def random(self):
        randPose = Pose2D((random.uniform(-CONSTRAINT, CONSTRAINT)),
                          random.uniform(-CONSTRAINT, CONSTRAINT),
                          self.angleWrap(random.random()))
        return randPose
