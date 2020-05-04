import numpy as np


class Pose2D:
    def __init__(self, x, y, theta):
        self.x = np.clip(x, a_min=-72, a_max=72)
        self.y = np.clip(y, a_min=-72, a_max=72)
        self.theta = theta
