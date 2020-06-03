import pygame

from Visualizer.Utils import loadImage


class Field(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = loadImage(144, '/home/tinku/SplineTrajectoryGenerator/Visualizer/Assets/Field.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
