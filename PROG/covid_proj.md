# Random walks with infection

---

so this is a model I made after I found one  that I found googling [carole adams](https://www.liglab.fr/fr/membre/carole-adam)

- the world is modeled as a grid just like  in a [platform game](https://eloquentjavascript.net/16_game.html) 
- I make a grid from this which contains a dictionary key to the transitions possible from a position

I used to write platform games in the early 2000s using Flash/Actionscript so I know how to do this.

Actually grids and coding walls into them  goes back to [rogue](https://en.wikipedia.org/wiki/Rogue_(video_game)#User_interface)

Here is a [tuto](http://rogueliketutorials.com/) in *simple* Python.

- I learned to program in Basic/C so I use a lot of tricks
- because I hate nested loops


---

## Grid

I wrapped the game board in a  class called ```Grid``` because 

- it's easier to debug as the names and methods aren't global
- here is a stub of the API


```
class Grid():
    
    def __init__(self, *args):
        initialise the grid with the border walls
        call self.mk_moves
        
    def get_blank(self):
        #make a blank copy of the grid without boundary walls
        return np.zeros_like(self.X)
                
    def mk_moves(self):
        calculate the valid moves for each position on the grid
        store as private attributes 


    def get_move(self, pos):
        #expose private attributes
        return  valid move   
    
```
            
          
---

### The loop

The simulation is a loop which is easy to port to another framework ie
- pygame
- tkinter

This is an important feature of **good** programming:
- it should be independant of the output device 
- data should be abstract/rich enough to be translated to other formats



### Here's the meta code



```
initialise everything

for _ in simulation duration:
    make a blank grid
    for each agent:
        draw the agent into the grid
        update the position of the agent
    save the state of the simulation
    
    for some agents:  
        determine interactions which change the state of an agent
        update the state of the agent if necessary

    
```

---

## Determining interactions

An interaction usually occurs during a *collision* between agents.
I implemented two different collision detection methods
- computing distance using [scipy.spatial.distance_matrix]()
- checking in a small box around the agents for other agents

### Advantages/disadvantages

- the first method can be useful if there are long distance interactions but is computationally expensive
- the second method is **cheap** but you have to clip the box if the agent is at the edge of the grid



---


