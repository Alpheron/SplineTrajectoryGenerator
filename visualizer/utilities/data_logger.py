import pygame


class DataLogger:
    def __init__(self, screen=None):
        self.screen = screen

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def displayText(self, text):
        largeText = pygame.font.Font('/home/tinku/.local/share/fonts/JetBrainsMono-Bold.ttf', 50)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.topleft = [0, 0]
        self.screen.blit(TextSurf, TextRect)
