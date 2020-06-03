import pygame

from Visualizer.Field import Field
from Visualizer.Robot import Robot
from Visualizer.Utils import screenHeight


class Main:

    def __init__(self):
        self.init()

    def createRobot(self):
        robot = Robot()
        return robot

    def createBackground(self):
        field = Field()
        return field

    def init(self):
        started = False
        screen = pygame.display.set_mode([screenHeight, screenHeight])
        self.createBackground()
        self.createRobot()
        return started, screen
