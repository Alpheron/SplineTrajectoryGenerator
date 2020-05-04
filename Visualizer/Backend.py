import pygame


class Visualization:
    started = False

    def initialize(self):
        pygame.init()
        screen = pygame.display.set_mode([800, 800])
        pygame.image.load("/home/tinku/SplineTrajectoryGenerator/Visualizer/Assets/Field.png")
        global started
        started = True

    def main(self):
        global started
        while started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    started = False
                    break
        pygame.quit()


if __name__ == "__main__":
    Vis = Visualization
