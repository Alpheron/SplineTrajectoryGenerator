import math

import numpy as np


class Pose2D:
    def __init__(self, x, y, theta):
        self.x = np.clip(x, a_min=-72, a_max=72)
        self.y = np.clip(y, a_min=-72, a_max=72)
        self.theta = self.angleWrap(theta)

    def angleWrap(self, angle):
        result = (angle + 2.0 * math.pi) % (2.0 * math.pi)
        if angle < 0.0 or angle > 2.0 * math.pi:
            return self.angleWrap(result)
        return result
