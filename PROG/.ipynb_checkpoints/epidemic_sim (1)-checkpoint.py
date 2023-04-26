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

class Grid():
    
    def __init__(self, sz = 40):
        self.sz = sz
        W =  np.zeros((sz+1,sz+1),dtype=int)
        #place the walls
        W[:,0] = W[0,:] = W[sz,:] = W[:,sz] = 1
        
        #expose this so that you can add extra walls
        #some would say I should not expose W but...
        self.W = W
        self.G = np.zeros((sz,sz))
        self.mk_moves()
        self.walls = np.array([1])
        
    def set_blank(self):
        self.G = np.zeros_like(self.X)
        self.G += self.W[1:-1,1:-1]
        
    def mk_moves(self):
        # you can rewrite this without using the convolution
        
            # mke a kernel
            K = [0,1,0,2,0,8,0,4,0]
            K = np.array(K).reshape(3,3)

            #these are the forbidden transitions for the agent_states
            forbidden = {0: [], 
                    8: [3], 4: [2], 2: [1], 1: [0],
                    9: [0,3], 6: [1,2],
                    12: [2,3], 3:[0,1]
            }

            # calculate the agent_states for the grid
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
    BLOCK_SIZE = 9
    x *= BLOCK_SIZE
    y *= BLOCK_SIZE
    center_point = ((x + (BLOCK_SIZE / 2)), (y + (BLOCK_SIZE / 2)))
    pygame.draw.circle(screen, color, center_point, BLOCK_SIZE / 2,0)

def update_screen(world):

    ALIVE_COLOR = pygame.Color(0,100,100)
    INFECTED_COLOR = pygame.Color(250,10,10)
    WALL_COLOR = pygame.Color(250,250,10)

    screen.fill((0,0,0))

    for x,y in world.walls:
        draw_block(x, y, WALL_COLOR)
    for x,y in np.array(np.where(world.G == UNINFECTED)).T:
        draw_block(x, y, ALIVE_COLOR)
    for x,y in np.array(np.where(world.G == INFECTED)).T:
        draw_block(x, y, INFECTED_COLOR)

    pygame.display.flip()

def main():

    def clip(x):
        # don't look outside the box
        # sz is global
        if x < 0 : return 0
        if x > sz : return sz
        return x

    # initialise
    sz = 100
    world  = Grid(sz=sz)
    world.W[47] = 1
    world.W[47,70:90] = 0
    world.W[:36,40] = 1
    # mk_moves should get called just once after the walls are set
    world.mk_moves()
    world.walls = np.array(np.where(world.W[1:-1,1:-1] == 1)).T 

    sz -= 2
    #initial configuration evenly spaced
    start_pos = []
    for j in range(2, sz, 8):
        for k in range(2, sz, 8):
            start_pos.append( np.array([j,k],dtype=int) )
            
    pts = np.array(start_pos)
    #choose who is infected
    global INFECTED, UNINFECTED
    UNINFECTED = 2
    INFECTED = 7
    agent_state = UNINFECTED*np.ones(len(start_pos))
    agent_state[44] = agent_state[-36] =  agent_state[-1] = INFECTED

    # do the event loop
    stats_now = []
    for k in range(1000):

        world.set_blank() 
        for pt, state in zip(pts, agent_state):
            pos = tuple(pt)
            world.G[pos] = state
            pt += world.get_move(pos)
        
        for _ in np.where(agent_state == UNINFECTED)[0]:
            x, y = pts[_]
            neighbors = world.G[clip(x-1):clip(x+2), clip(y-1):clip(y+2) ]
            if np.max(neighbors) == INFECTED:
                agent_state[_] = INFECTED

        #count infected, should be dumped to a file at the end
        stats_now.append(len(agent_state[agent_state==INFECTED]))

        update_screen(world)
        sleep(0.1)

    #dump the data for analysis
    pass

if __name__ == '__main__':
    main()
