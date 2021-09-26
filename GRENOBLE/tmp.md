%Geometry of sums of squares
%greg mc
%October 2021

#

<img src="./Martin_Aigner.jpg" width="400">

- [Proofs from THE BOOK](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK#:~:text=Proofs%20from%20THE%20BOOK%20is,proof%20of%20each%20mathematical%20theorem){target="_blank"}
- [Convexity and Aigner's Conjectures](https://arxiv.org/abs/2101.03316){target="_blank"}
- Can I prove these with one figure ?



#

Markov numbers are integers that appear in triples which are solutions of
a Diophantine equation the so-called Markov cubic

<span style="font-size: 200%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

# 
## Infinity of Markoff numbers

$\begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$
is an automorph of <span style="font-size: 150%">$x^2 + y^2  - 3x y.$</span>

 so <span style="font-size: 150%">$( v_n,v_{n+1},1)$</span> is a solution where

<span style="font-size: 150%">$\begin{pmatrix}v_{n+1} \\ v_n \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix}1 \\ 1 \end{pmatrix}$</span>

#
### Odd index Fibonacci numbers are Markoff numbers

$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...$

<span style="font-size: 200%">$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$</span>

#
### Frobenius uniqueness conjecture


The largest integer in a triple determines the two other numbers.

#
### Partial results

m = Markoff number

- Jack Button for [m prime](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610798006292){target="_blank"}
- Zhang [An elementary proof...](https://arxiv.org/abs/math/0606283){target="_blank}
- Baragar [m, 3m - 2, 3m + 2 prime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/88B0E426FFCBEA8B3A345C1074B8CC59/S0008439500018828a.pdf/on-the-unicity-conjecture-for-markoff-numbers.pdf){target="_blank}
- [ Bugeaud, Reutenauer, Siksek](https://core.ac.uk/download/pdf/82088222.pdf){target="_blank}
- Conclusion too hard!!!


#
### Aigner's monotonicity conjectures

- Markov’s theorem and 100 years of the uniqueness conjecture. A mathematical journey from irrational numbers to perfect matchings.  2013.  
- M. Rabideaua, R. Schiffler,
Continued fractions and orderings on the Markov numbers,
Advances in Mathematics Vol 370,  2020.
- C Lagisquet and E. Pelantová and S. Tavenas and L. Vuillon, On the Markov numbers: fixed numerator, denominator, and sum conjectures.


#

### Natural map ?

<span style="font-size: 200%">$\mathbb{Q}\cup \infty \rightarrow$</span> Markoff numbers

<span style="font-size: 200%">$p/q \mapsto m_{p,q}$</span>

- projective <span style="font-size: 200%">$GL(2, \mathbb{Z})$</span> action on <span style="font-size: 200%">$\mathbb{Q}\cup \infty$</span> 
- action on Markoff numbers ?
- automorphisms of the Markoff cubic?

#
## Automorphisms

- (cyclic) permutations of <span style="font-size: 200%">$x,y,z$</span>
- Vieta flips/involutions
- get <span style="font-size: 200%">$\mathbb{Z}/2 * \mathbb{Z}/3$</span> action
- = <span style="font-size: 200%">$PSL(2,\mathbb{Z})$</span> action

#
### Vieta flips/involutions
<span style="font-size: 250%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>

- quadratic in <span style="font-size: 200%">$x$</span>,  two roots <span style="font-size: 200%">$x^\pm$</span>
- <span style="font-size: 200%">$x^+ + x^- = 3yz$</span>
- involution <span style="font-size: 200%">$(x,y,z) \mapsto (3yz -x, y,z)$</span>

#
Natural  = <span style="font-size: 200%">$PSL(2,\mathbb{Z})$</span>-equivariant map

<span style="font-size: 200%">$\mathbb{Q}\cup \infty \rightarrow$</span> Markoff numbers <span style="font-size: 200%">$p/q \mapsto m_{p/q}$</span>

- <span style="font-size: 200%">$(1:1) \mapsto  1/1 \mapsto 2$</span> 
- <span style="font-size: 200%">$(0:1) \mapsto  0/1 \mapsto 1$</span> 
- <span style="font-size: 200%">$(1:0) \mapsto  \infty \mapsto 1$</span> 
- actions = projective on left and by autos on right


## Topological representation

<span style="font-size: 200%">$\mathbb{Q}\cup \infty \subset$</span> circle/projective line

- <span style="font-size: 200%">$(a,b)\text{ primitive } \mapsto a/b \in \mathbb{Q}\cup \infty$</span>
- <span style="font-size: 200%">$\begin{pmatrix} a & c \\ b & d \end{pmatrix} \mapsto$</span>  arc joining <span style="font-size: 200%">$(a/b, c/d)$</span> 
- <span style="font-size: 200%">$(a/b, c/d)$</span> are Farey neighbors

#

<img src="./sami.jpg" width="600">

[source](https://www.math.mcgill.ca/sdouba/seminar/sami)

#

<img src="./pozzi.jpg.png" width="600">

[source](https://www.mathi.uni-heidelberg.de/~pozzetti/trees/4.pdf)

#

<img src="./farey_tree.png" width="600">

[source](https://www3.nd.edu/~math/rtg/GTS/www3.nd.edu/_jquigle2/GSTS%20FA18/Week1P.pdf)


# 
### Markoff numbers


<img src="./Markoff_tree_full.svg" width="500">

