import pygame


class Visualization:
    @staticmethod
    def initialize():
        pygame.init()
        screen = pygame.display.set_mode([800, 800])
        pygame.image.load("Visualizer/Assets/Field.png")
