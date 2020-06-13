from math import degrees

import pygame

from visualizer.utilities.utils import SCREEN_DIM


class DataLogger:
    def __init__(self, trajectory, clock=None, screen=None):
        self.screen = screen
        self.FontSize = 20
        self.trajectory = trajectory
        self.clock = clock
        self.numberOfWidgets = 0

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()
        self.numberOfWidgets += 1

    def displayText(self, text, location):
        largeText = pygame.font.Font('/home/tinku/.local/share/fonts/JetBrainsMono-Bold.ttf', self.FontSize)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.topleft = location
        constrainedRect = TextRect.clamp(self.screen.get_rect())
        self.screen.blit(TextSurf, constrainedRect)

    def renderDashboard(self, counter):
        try:
            self.displayText(str("FPS: " + str(round(float(self.clock.get_fps()), 3))),
                             [SCREEN_DIM, SCREEN_DIM])
            self.displayText(str("X: " + str(round(float(self.trajectory[counter].getX()), 3))), [0, 0])
            self.displayText(str("Y: " + str(round(float(self.trajectory[counter].getY()), 3))),
                             [0, self.FontSize])
            self.displayText(
                str("Theta: " + str(round(float(degrees(self.trajectory[counter].getTheta())), 3))),
                [0, (self.FontSize * 2)])
            self.displayText(str("Time: " + str(round((float((pygame.time.get_ticks() / 1000))), 3))),
                             [0, (self.FontSize * 3)])
        except IndexError:
            self.displayText(str("FPS: " + str(round(float(self.clock.get_fps()), 3))),
                             [SCREEN_DIM, SCREEN_DIM])
            self.displayText(str("X: " + str(round(float(self.trajectory[-1].getX()), 3))), [0, 0])
            self.displayText(str("Y: " + str(round(float(self.trajectory[-1].getY()), 3))),
                             [0, (self.FontSize * self.numberOfWidgets)])
            self.displayText(str("Theta: " + str(round(float(degrees(self.trajectory[-1].getTheta())), 3))),
                             [0, (self.FontSize * self.numberOfWidgets)])
