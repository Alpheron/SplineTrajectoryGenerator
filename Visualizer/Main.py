import pygame

from Visualizer.Utils import screenHeight


class Main:

    def __init__(self, winSize=screenHeight):
        started = False
        screen = pygame.display.set_mode([winSize, winSize])
        pygame.image.load("/home/tinku/SplineTrajectoryGenerator/Visualizer/Assets/Field.png")
        pygame.init()
