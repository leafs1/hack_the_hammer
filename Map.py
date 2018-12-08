import sys

import pygame, time
from pygame.locals import *

def run():
    pygame.init()
    window = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Shopper Mapper")
    clock = pygame.time.Clock()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # draw on the surface object

    window.fill(WHITE)

    #pygame.draw.polygon(window, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    #pygame.draw.line(window, BLUE, (60, 60), (120, 60), 4)
    #pygame.draw.line(window, BLUE, (120, 60), (60, 120))
    #pygame.draw.line(window, BLUE, (60, 120), (120, 120), 4)
    #pygame.draw.circle(window, BLUE, (300, 50), 20, 0)
    #pygame.draw.ellipse(window, RED, (300, 250, 40, 80), 1)
    rectangle = [window, RED, (300, 1, 100, 60)]
    rectangle2 = [window, GREEN, (400, 1, 100, 60)]


    pygame.draw.rect(rectangle[0], rectangle[1], rectangle[2])
    pygame.draw.rect(rectangle2[0], rectangle2[1], rectangle2[2])


    #rect (x-axis, y-axis, x length, y length)

    pixObj = pygame.PixelArray(window)
    pixObj[480][380] = BLACK
    pixObj[482][382] = BLACK
    pixObj[484][384] = BLACK
    pixObj[486][386] = BLACK
    pixObj[488][388] = BLACK

    del pixObj










    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            print(event)
        pygame.display.update()


if __name__ == "__main__":
    run()