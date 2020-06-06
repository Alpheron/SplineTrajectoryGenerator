import pygame

SCREEN_HEIGHT = 800
CONSTRAINT = 72


# @:param value to scale to display size
def scaled_value(x):
    scaled_val = x * (SCREEN_HEIGHT / CONSTRAINT)
    return scaled_val


# @:param size of the object in inches
# @:param path to where the image of robot visualizer resides to load and scale to display size
def load_image(size, pathToImage):
    surface = pygame.image.load(pathToImage)
    return pygame.transform.scale(surface, (int(scaled_value(size)),
                                            int(scaled_value(size))))
