import pygame

from Visualizer.Field import Field
from Visualizer.Robot import Robot
from Visualizer.Utils import screenHeight


class Main:
    started = False
    screen = pygame.display.set_mode([screenHeight, screenHeight])

    def __init__(self):
        self.createBackground()
        self.createRobot()

    def createRobot(self):
        robot = Robot()
        return robot

    def createBackground(self):
        field = Field()
        return field

    def mainLoop(self):
        # noinspection PyGlobalUndefined
        global started
        started = True
        while started:
            quitEvent = pygame.event.poll()
            if quitEvent == pygame.QUIT:
                started = False
                break
