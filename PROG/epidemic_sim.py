# MIT licence


from time import sleep
import pygame
import numpy as np
from scipy import signal
import random

pygame.init()

#Initialise the screen
xmax = 900 #Width of screen in pixels
ymax = 900 #Height of screen in pixels
screen = pygame.display.set_mode((xmax, ymax), 0, 24) #New 24-bit screen
pygame.display.set_caption('Simulation of an epidemic')

BLACK = (0, 0, 0)

class Grid():
    
    def __init__(self, sz = 40):
        self.sz = sz
        W =  np.zeros((sz+1,sz+1),dtype=int)
        #place the walls
        W[:,0] = W[0,:] = W[sz,:] = W[:,sz] = 1
        
        #expose this so that you can add extra walls
        #some would say I should not expose W but...
        self.W = W
        self.mk_moves()
        
    def get_blank(self):
        return np.zeros_like(self.X)
        
        
    def mk_moves(self):
        # you can rewrite this without using the convolution
        
            # mke a kernel
            K = [0,1,0,2,0,8,0,4,0]
            K = np.array(K).reshape(3,3)

            #these are the forbidden transitions for the states
            forbidden = {0: [], 
                    8: [3], 4: [2], 2: [1], 1: [0],
                    9: [0,3], 6: [1,2],
                    12: [2,3], 3:[0,1]
            }

            # calculate the states for the grid
            self.X = signal.convolve2d(self.W, K)[2:-2,2:-2]

            #apparently these get cast to np.array when I add???
            diffs = [[1,0],[0,1],[-1,0],[0,-1]]

            allowed_moves = {}
            for x in forbidden:
                allowed_moves[x] =  [ y for k,y in enumerate(diffs)
                                         if k not in  forbidden[x]] 
            #expose to the user
            self.allowed_moves = allowed_moves
    
    def get_move(self, pos):
        return random.choice(self.allowed_moves[self.X[pos]])
        

def draw_block(x, y, color):
    block_size = 9
    x *= block_size
    y *= block_size
    center_point = ((x + (block_size / 2)), (y + (block_size / 2)))
    pygame.draw.circle(screen, color, center_point, block_size / 2,0)


def main():
    def clip(x):
        # don't look outside the box
        # sz is global
        if x < 0 : return 0
        if x > sz :return sz
        return x

    # initialise

    alive_color = pygame.Color(0,100,100)
    infected_color = pygame.Color(250,10,10)
    wall_color = pygame.Color(250,250,10)

    sz = 100
    world  = Grid(sz=sz)
    world.W[47] = 1
    world.W[47,70:90] = 0
    world.W[:36,40] = 1
    world.mk_moves()
    walls = np.array(np.where(world.W[1:-1,1:-1] == 1)).T 

    sz -= 2
    #initial configuration evenly spaced
    pp = []
    for j in range(2, sz,8):
        for k in range(2, sz,8):
            pp.append( np.array([j,k],dtype=int) )
            
    pts = np.array(pp)
    #choose who is infected
    cols = 2*np.ones(len(pp))
    cols[44] = cols[-36] =  cols[-1] = 7

    # do the event loop
          
    stats_now = []
    for k in range(1000):
        grid = world.get_blank() 
        #update
        for pt,color in zip(pts, cols):
            pos = tuple(pt)
            grid[pos] = color
            pt += world.get_move(pos)
        
        grid += world.W[1:-1,1:-1]
        screen.fill(BLACK)

        for x,y in walls:
            draw_block(x, y, wall_color)
        for x,y in np.array(np.where(grid == 2)).T:
            draw_block(x, y, alive_color)
        for x,y in np.array(np.where(grid == 7)).T:
            draw_block(x, y, infected_color)

        pygame.display.flip()

        #count infected, should be dumped to a file at the end
        stats_now.append(len(cols[cols>5]))
        # I have to recalculate this every time  
        for _ in np.where(cols == 2)[0]:
            x, y = pts[_]
            neighbors = grid[clip(x-1):clip(x+2), clip(y-1):clip(y+2) ]
            if np.max(neighbors) > 6:
                cols[_] = 7
        sleep(0.1)

    #dump the data for analysis
    pass

if __name__ == '__main__':
    main()
