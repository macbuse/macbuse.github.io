# Conway's game of life

The Game of Life is a cellular automaton devised by the mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. 

- It is Turing complete and can simulate a universal constructor or any other Turing machine.

---

## Summary of principles

- The initial pattern constitutes the seed of the system. 
- The first generation is created by applying a fixed set of rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. 
- Each generation is a pure function of the preceding one. 
- The rules continue to be applied repeatedly to create further generations.

---

## Origins of life LOL

In late 1940, John von Neumann defined life as a creation (as a being or organism) 
- which can reproduce itself 
- and simulate a Turing machine. 


[Stanislaw Ulam](https://en.wikipedia.org/wiki/Stanislaw_Ulam) invented cellular automata
- Ulam discussed using computers to simulate his cellular automata in a two-dimensional lattice in several papers. 
- In parallel, von Neumann attempted to construct Ulam's cellular automaton. 

Conway chose his rules carefully, after considerable experimentation, to meet the following criteria:

1. There should be no explosive growth.
1. There should exist small initial patterns with chaotic, unpredictable outcomes.
1. There should be potential for von Neumann universal constructors.
1. The rules should be as simple as possible, whilst adhering to the above constraints.

---

## Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

 These rules can be condensed into the following:

- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. 
- Similarly, all other dead cells stay dead.

### Succinct version of rules

If one forgets the biological interpretation of the rules then they reduce to: 

- any cell whether  living or dead with 3 live neighbors is live in the next generation
- a living cell with 2 live neighbors is live in the next generation

State of the cell :

```
live = true
dead = false
```


The state of a cell in the next generation is given by:

```
(S = 3) OU (E = 1 ET S = 2)
```

where

- S = number of neighbors of the cell which are alive
- E = the state of the cell in the current generation 

---
## Using convolutions

I did this by myself but [this guy](https://nicholasrui.com/2017/12/18/convolutions-and-the-game-of-life/#:~:text=The%20Game%20of%20Life%20is,its%20neighbors%20must%20be%20alive) had the same idea.
He states that he wants to avoid 
- loops
- checking cases

``` 
As I expected, the lines that checked whether a player had achieved a
five-in-a-row was a verbose series of nested for-loops checking a plethora of
cases. While they often seem like a natural course of action, in many settings
they are often unwieldy and slower than desirable. Luckily for my friend, the
code ran quite quickly, but I thought about whether there was a faster way.
```

My code from last year:

``` 
    H = signal.convolve2d( G, K, boundary='wrap')[1:-1,1:-1]

    H[H<=2] = 0 #dies
    H[(H==4)&(G==0)] = 0 # dies
    H[H>4] = 0 #dies 
    H[H>0] = 1 #lives
    G = H
```


## Why these rules ?

Because I was thinking about death/life:

- All other live cells die in the next generation. 
    ```
    H[H<=2] = 0 #dies
    H[(H==4)&(G==0)] = 0 # dies
    H[H>4] = 0 #dies 
    ```
This stopped me from finding the optimal solution straight away. 
This is an example of [cognitive bias](https://en.wikipedia.org/wiki/Cognitive_bias).

## Better to copy

[from here](https://fr.wikipedia.org/wiki/Jeu_de_la_vie#Questions_math%C3%A9matiques)

L'état suivant d'une cellule est : 

```(S = 3) OU (E = 1 ET S = 2).```

Avec :

- S : nombre actuel de cellules vivantes dans son voisinage (entier naturel compris entre 0 et 8 inclus) ;
- E : état actuel de la cellule (entier naturel égal à 0 pour une cellule morte et égal à 1 pour une cellule vivante).

```
    S = signal.convolve2d( E, K, boundary='wrap')[1:-1,1:-1]
    T = np.zeros_like(E)
    T[ (S==3) | ( ( S == 2) & (E == 1) )] = 1
    E = T
````

I had to change the kernel too but you will see that in the notebook.

## conclusion

I can code the game of life in 4 LOC because
- I know about **convolutions** and **kernels**

## can u do  better ?



[this guy](https://nicholasrui.com/2017/12/18/convolutions-and-the-game-of-life/#:~:text=The%20Game%20of%20Life%20is,its%20neighbors%20must%20be%20alive) suggests changing the kernel.

what about 
- [high life](https://fr.wikipedia.org/wiki/HighLife_(automate_cellulaire))
- [day and night](https://en.wikipedia.org/wiki/Day_and_Night_(cellular_automaton))
- [these](https://github.com/bollu/cellularAutomata) ?
- [these](https://github.com/Hopson97/CellularAutomaton) ?

Or [abelian sandpiles](https://github.com/kivyfreakt/sandpile) ?
