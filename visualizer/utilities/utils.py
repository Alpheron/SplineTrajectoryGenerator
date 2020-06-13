import sys

import pygame

SCREEN_DIM = 800
CONSTRAINT = 72
DEFAULT_STEP_SIZE = 100


def quitLoopConditional(started):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            started = False
            pygame.quit()
            sys.exit()


# @:param value to scale to display size for global size
def scaled_value(x, isRelative=False):
    scaled_val = None
    if isRelative is False:
        scaled_val = int(x * (SCREEN_DIM / (CONSTRAINT * 2)))
    if isRelative is not False:
        scaled_val = int((x - (-CONSTRAINT)) * (SCREEN_DIM / (CONSTRAINT * 2)))
    return scaled_val


# @:param size of the object in inches
# @:param path to where the image of robot visualizer resides to load and scale to display size
def load_image(size, pathToImage, alpha=None):
    if alpha is None:
        surface = pygame.image.load(pathToImage).convert()
        return pygame.transform.scale(surface, (int(scaled_value(size)),
                                                int(scaled_value(size))))

    if alpha is not None:
        surface = pygame.image.load(pathToImage).convert_alpha()
        return pygame.transform.scale(surface, (int(scaled_value(size)),
                                                int(scaled_value(size))))
