%Stage 
%greg mc
%June 2022


# 3D


- [topology: Alexander sphere](https://www-fourier.ujf-grenoble.fr/~mcshane/3D/alexanderSphere.html){target="_blank"}
- [geometry: Heisenberg group](https://www-fourier.ujf-grenoble.fr/~mcshane/3D/heisenberg_moon_radial_hires.html){target="_blank"}

# geometry

- Pythagoras
- Théorème de Bolyai (Wallace-Bolyai-Gerwein theorem)
- Heron's formula

#

## Pythagore

Si un triangle est rectangle, le carré de la longueur de l’hypoténuse 
est égal à la somme des carrés des longueurs des deux autres côtés.

$a^2 = b^2 + c^2$

- aire d'un triangle
- aire d'un triangle rectangle $\frac12 (b\times c)$
- decoupage d'un triangle rectangle


#
## Théorème de Bolyai

### Exo

- determiner le rapport longueur/largeur d'une feuille A4, A5, A6..
- couper une feuille A5 en 3 morceaux qui se recollent pour former un carre


#
## Théorème de Bolyai

Deux polygones A et B de même aire 
sont équivalents par découpage et recollement.

---

On dit que deux polygones A et B sont <br>
**équivalents par découpage et recollement** <br>
si on peut decomposer 

- A comme une réunion finie de polygones $A_i$
- B comme une réunion finie de polygones $B_i$
 - tels que pour tout $i$, $A_i$ soit directement isométrique à $B_i$.
 - On note alors $A \sim B$
.

#
## Théorème de Bolyai

Deux polygones A et B de même aire 
sont équivalents par découpage et recollement.

1. $\forall$ triangle $T$,  $\exists$ rectangle $R$ avec $T\sim R$
1. $\forall$ rectangle $R$, $R \sim S$ avec $S=$ carre de meme aire 
1. Comment faire le cas general ?
1. [solution](https://batmath.org/wp-content/uploads/2017/09/ScissorsSFMTC171021solutions.pdf)

#
## Paradoxe

il est possible de découper une boule de $\mathbb{R}^{3}$ <br>
en 5 morceaux et de les réassembler <br>
pour former deux boules identiques à la première.

- [Banach-Tarski](https://fr.wikipedia.org/wiki/Paradoxe_de_Banach-Tarski)


# Arithmetic

- Fibonacci
- Fermat

# Games

- [Mastermind](https://fr.wikipedia.org/wiki/Mastermind){target="_blank"}
- Wordle
	- [english](https://www.nytimes.com/games/wordle/index.html){target="_blank"}
	- [french](https://www.solitaire-play.com/lemot){target="_blank"}
- [Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie){target="_blank"}

#

**Mastermind: Knuth's algorithm**

[Camille projet L3](./Mastermind_projet_Touron_Camille_L3A-checkpoint.html){target="_blank"}

# 
## algorithms

- [Parcours sup](https://framagit.org/parcoursup/algorithmes-de-parcoursup){target="_blank"}
- [maintainer](https://www.labri.fr/perso/gimbert/){target="_blank"}
- [Google Pagerank](https://fr.wikipedia.org/wiki/PageRank){target="_blank"}
- [Word2vec](https://fr.wikipedia.org/wiki/Word2vec){target="_blank"}
- [GPT3/LaMDA](https://www.npr.org/2022/06/16/1105552435/google-ai-sentient){target="_blank"}

#

## Go Echecs

- [AlphaGo](https://fr.wikipedia.org/wiki/AlphaGo){target="_blank"}
- [AlphaZero](https://fr.wikipedia.org/wiki/AlphaZero){target="_blank"}
- [StockFish](https://stockfishchess.org/){target="_blank"}
- [the match](https://www.youtube.com/watch?v=8dT6CR9_6l4}{target="_blank"}


#  
## Enumeration possibilities

- Matermind 6 colours
- $6^4 = 1296$
- 6 colours $\leftrightarrow$ digits $0,1,2\ldots 6$
- possibilities $\leftrightarrow$ digits $0,1,2\ldots 1296$

```
def number_base(n, base):
    if n == 0:
        return 0
    else:
        return n % base + 10 * number_base(n // base, base)

```

# DNN/AI

- [Deepl](https://www.deepl.com/translator#en/fr/this%20is%20a%20lot%20of%20shit){target="_blank"}
- [Github copilot](https://copilot.github.com/){target="_blank"}


# Wordle

[english wordle](https://www.nytimes.com/games/wordle/index.html){target="_blank"}

# Fibonacci

- $F_0 = 0, F_1 = 1$
- $F_{n+1} = F_n + F_{n-1}$

# Python

```
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
```


# Python 

```
fib = [1,1]
for _ in range(20):
    fib.append(fib[-1] + fib[-2])
               
print(fib)

[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 
89, 144, 233, 377, 610, 987, 1597, 
2584, 4181, 6765, 10946, 17711]
```


#
### Odd index Fibonacci numbers

```
fib[1::2] 

[1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181, 10946]$
```

- $2 = 1^2 + 1^2$
- $5 = 1^2 + 2^2$
- $13 = 2^2 + 3^2$
- $34 = 3^2 + 5^2$

#

```
[x**2 + y**2 for  x,y in zip(fib[0:11], fib[1:]) ]


[1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181, 10946]
```

#
### Odd index Fibonacci numbers

$$F_{2n+1} = F_{n+1}^2 + F_n^2$$
