import pygame

from NeuralNetworks.Pose import Pose2D
from Visualizer.Main import Main

screenHeight = 800
constraint = 72


# @:param value to scale to display size
def scaledVal(x):
    scaled_val = x * (Main.screenHeight / Pose2D.constraint)
    return scaled_val


# @:param size of the object in inches
# @:param path to where the image of robot visualizer resides to load and scale to display size
def loadImage(size, pathToImage):
    surface = pygame.image.load(pathToImage)
    return pygame.transform.scale(surface, (int(scaledVal(size)),
                                            int(scaledVal(size))))
