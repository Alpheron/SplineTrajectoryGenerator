import pygame

SCREEN_DIM = 800
CONSTRAINT = 72


# @:param value to scale to display size for global size
def scaled_value(x, isRelative=False, isHeight=False):
    scaled_val = None
    if isRelative is False:
        scaled_val = int(x * (SCREEN_DIM / (CONSTRAINT * 2)))
    if isRelative is not False:
        scaled_val = int((x - (-CONSTRAINT)) * (SCREEN_DIM / (CONSTRAINT * 2)))
    if isHeight is not False and x is not 0:
        scaled_val = -scaled_val
    return scaled_val


# @:param size of the object in inches
# @:param path to where the image of robot visualizer resides to load and scale to display size
def load_image(size, pathToImage):
    surface = pygame.image.load(pathToImage)
    return pygame.transform.scale(surface, (int(scaled_value(size)),
                                            int(scaled_value(size))))
