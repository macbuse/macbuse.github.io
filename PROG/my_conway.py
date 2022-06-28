# rewrite of https://gist.github.com/bennuttall/6952575

from time import sleep
import pygame
import numpy as np
from scipy import signal

pygame.init()

#Initialise the screen
xmax = 600 #Width of screen in pixels
ymax = 600 #Height of screen in pixels
screen = pygame.display.set_mode((xmax, ymax), 0, 24) #New 24-bit screen

BLACK = (0, 0, 0)

def evolve(E):
    K = np.ones((3,3), dtype=np.int8)
    K[1,1] = 0
    S = signal.convolve2d( E, K, boundary='wrap')[1:-1,1:-1]
    T = np.zeros_like(E)
    T[ (S==3) | ( ( S == 2) & (E == 1) )] = 1
    return T

def draw_block(x, y, alive_color):
    block_size = 9
    x *= block_size
    y *= block_size
    center_point = ((x + (block_size / 2)), (y + (block_size / 2)))
    pygame.draw.circle(screen, alive_color, center_point, block_size / 2,0)

def main():
    h = 0
    alive_color = pygame.Color(h,100,100)
    xlen = xmax // 9
    ylen = ymax // 9
    while True:
        world = np.random.randint(0, high=2, size=(xlen, ylen))
        for _ in range(200):
            screen.fill(BLACK)
            for x,y in np.array(np.where(world == 1)).T:
                 draw_block(x, y, alive_color)
            pygame.display.flip()
            h = (h + 2) % 360
            alive_color.hsva = (h, 100, 100)
            world = evolve(world)
            sleep(0.1)

if __name__ == '__main__':
    main()
