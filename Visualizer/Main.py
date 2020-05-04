import pygame


class Main:
    screenHeight = 800

    def __init__(self, winSize=screenHeight):
        started = False
        screen = pygame.display.set_mode([winSize, winSize])
        pygame.image.load("/home/tinku/SplineTrajectoryGenerator/Visualizer/Assets/Field.png")
        pygame.init()
