%Geometry of sums of squares
%greg mc
%October 2021

#

<img src="./Martin_Aigner.jpg" width="400">

- [Proofs from THE BOOK](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK#:~:text=Proofs%20from%20THE%20BOOK%20is,proof%20of%20each%20mathematical%20theorem){target="_blank"}
- [Convexity and Aigner's Conjectures](https://arxiv.org/abs/2101.03316){target="_blank"}
- Can I prove these with one figure ?

#

<img src="./theoremsab.png" width="600">


#

Markov numbers are integers that appear in triples which are solutions of
a Diophantine equation the so-called Markov cubic

200$x^2 + y^2 + z^2 - 3x y z = 0.$

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

#
### Odd index Fibonacci numbers are Markoff numbers

$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...$

200$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

# 
### Markoff numbers


<img src="./Markoff_tree_full.svg" width="500">

#
### Frobenius uniqueness conjecture

- The largest integer in a triple determines the two other numbers.
- For every Markoff number 200$m$ there are exactly 3 simple closed geodesics of length  200$2\cosh^{-1}(3m/2)$ on the modular torus 200$\mathbb{H}/\Gamma'$ 


#
### Partial results

m = Markoff number

- Jack Button for [m prime](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610798006292){target="_blank"}
- Zhang [An elementary proof...](https://arxiv.org/abs/math/0606283){target="_blank}
- Baragar [m, 3m - 2, 3m + 2 prime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/88B0E426FFCBEA8B3A345C1074B8CC59/S0008439500018828a.pdf/on-the-unicity-conjecture-for-markoff-numbers.pdf){target="_blank}
- [ Bugeaud, Reutenauer, Siksek](https://core.ac.uk/download/pdf/82088222.pdf){target="_blank}
- Conclusion too hard!!!

#
## Button's Theorem

If 200$z$ is a Markoff number which is prime<br>
then there is a unique triple 200$z > y > x$

- 200$x^2 + y^2 + z^2 - 3x y z = 0.$
- 200$\bar{x}^2 + \bar{y}^2 = 0.$ in 200$\mathbb{F}_z$
- 200$(\bar{x}/\bar{y})^2 = -1$ in 200$\mathbb{F}_z$

#

<img src="./theoremsab.png" width="600">

- Button's theorem follows from unicity here


#
## two groups of order 4

Acting on 150$\mathbb{F}_p^*$

150$\begin{array}{lll}
x &\mapsto& -x \\
x &\mapsto& 1/x
\end{array}$

Acting on 150$\mathbb{H}$

150$\begin{array}{lll}
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}
\end{array}$

#
## Farey tessalation

<img src="./farey_bicolor.png" width="400">

#
## Ford circles

<img src="./ford_circles.gif" width="400">

#

<iframe width="560" height="615" src="https://www.youtube.com/embed/0hlvhQZIOQw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#
## References etc


- Heath-Brown, Fermat’s two squares theorem. Invariant (1984) 
- Zagier, A one-sentence proof that every prime p = 1 (mod 4) is a sum of two squares, 1990
- Elsholtz, Combinatorial Approach to Sums of Two Squares and Related Problems.  (2010) 
- Penner, The decorated Teichmueller space of punctured surfaces, Comm  Math Phys  (1987)
- [Zagier text](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2323918/fulltext.pdf){target="_blank"}

#
## Zagier


<img src="./zagier.png" width="800">


#
### Burnside Lemma 

- 200$G$ acting on 200$X$ then 

    250$|G| |X/G| = \sum_{g} |X^g|$

- 200$X^g$ =  fixed points of the element 200$g$ 
- 200$X/G$  the orbit space.

#
## Theorem 1.1

Acting on 200$X = \mathbb{F}_p^*$

- identity 200$|X^g| = p-1$ 
- 200$x \mapsto -x, |X^g| = 0$  
- 200$x \mapsto 1/x, |X^g| = 2$  
- 200$x \mapsto -1/x, |X^g| = \ldots$  

#


- 250$|G| |X/G| = \sum_{g} |X^g|$
- 250$4 |X/G| = (p-1) + 2 + |X^{(x\mapsto -1/x)}|$
- 250$\Rightarrow  |X^{(x\mapsto -1/x)}|= 2$,, if 250$4 \not | (p+1)$
- 250$\Rightarrow  \exists x,\, x^2 = -1$, if 250$4 \not | (p+1)$


#
## Theorem 1.2: sum of 2 squares

Acting on 200$\mathbb{H}$

200$\begin{array}{lll}
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}
\end{array}$



#
## Primitives

- 250$\mathbb{Z}^2$ 
- infinitely many primitive elements 
- 250$(a,b)$ primitive iff 250$a,b \in \mathbb{Z}$ coprime
- 200$SL(2,\mathbb{Z})$ transitive on primitives


#
## Important

200$\{ \textit{primitives} \} = \mathbb{Q}\cup \infty \subset$ circle/projective line 200$= \partial_\infty \mathbb{H}$


#


#
## Farey tessalation


200$\mathbb{Q}\cup \infty \subset$ circle/projective line

- 200$(a,b)\text{ primitive } \mapsto a/b \in \mathbb{Q}\cup \infty$
- 200$\begin{pmatrix} a & c \\ b & d \end{pmatrix} \in \mathrm{SL}(2,\mathbb{Z})\mapsto$  arc joining 200$(a/b, c/d)$ 
- 200$(a/b, c/d)$ are Farey neighbors


#

<img src="./sami.jpg" width="600">

[source](https://www.math.mcgill.ca/sdouba/seminar/sami)

#

<img src="./farey_tree.png" width="600">

[source](https://www3.nd.edu/~math/rtg/GTS/www3.nd.edu/_jquigle2/GSTS%20FA18/Week1P.pdf)

#
## Definitions
- **arc** = Poincaré geodesic joining 200$a/b, c/d \in \mathbb{Q}\cup \infty$
- **200$\lambda$- length of  arc** 200$= |ad - bc|^2$ 

#
## Lemma

**200$\log \lambda$- length ** = length of the portion outside Ford circles tangent to the real line at its endpoints


#
## Ford circles

<img src="./ford_circles.gif" width="400">


#

200$\mathrm{SL}(2,\mathbb{Z})$ acts by Mobius transformations on 200$\mathbb{H}$

- 200$\begin{pmatrix} a & c \\ b & d \end{pmatrix}.z = \frac{az+b}{cz+d}$ 
- preserves the Poincaré (hyerbolic) metric
- the orbit of 200$F := \{ z, \mathrm{Im}\, z > 1\}$ are the Ford circles

#

<img src="./ford_circles_again.png" width="600">

- point of tangency with 200$\mathbb{R} = p/q$, diameter = 200$1/q^2$

#
### Proof of lemma

- **arc** joining 200$a/b, c/d$ has **200$\lambda$- length ** 200$= |ad - bc|^2$ 
- **200$\log \lambda$- length ** = length of the portion outside Ford circles tangent to the real line at its endpoints


#
### Proof of lemma

- 200$\mathrm{SL}(2,\mathbb{Z})$  transitive, 
- can suppose 200$a/b = \infty$ and 200$c/d = k/(ad - bc)$
- Ford circles  200$F$  tangent at 200$\infty$
- and another of diameter 200$1/(ad - bc)^2$
- the **midpoint** of this vertical arc is at height 200$1/|ad - bc|$

#
#
- 200$\Gamma = \mathrm{SL}(2,\mathbb{Z})$ has torsion so 200$\mathbb{H}/\Gamma$ orbifold
- 200$\Gamma(2) = \ker (\mathrm{SL}(2,\mathbb{Z})\rightarrow  \mathrm{SL}(2,\mathbb{F}_2))$
- 200$\Gamma' = [\Gamma,\Gamma]$
- 200$\mathbb{H}/\Gamma(2)$  three punctured sphere 
- 200$\mathbb{H}/\Gamma'$ once punctured torus 

#

In the solution of Aigner's conjectures the geometry of the 
simple geodesics on
200$\mathbb{H}/\Gamma'$ once punctured torus was important. 

- For Fermat's theorem it's the automorphisms of 
200$\mathbb{H}/\Gamma(2)$ =  three punctured sphere 

#

A three punctured sphere <br>
can be cut up into 2 ideal triangles.

<img src="./fund_dom_gamma2.png" width="400">

- Fundamental domain for 200$\Gamma(2)$


#

<img src="./three_punctured.png" width="400">

- 200$i, 1+i, \frac12 ( 1 + i)$ are midpoints

#
## reciprocals of sums of squares

- 200$i, 1+i, \frac12 ( 1 + i)$ are midpoints of arcs
- the lifts to 200$\mathbb{H}$ of the midpoints 200$=\Gamma.i$ 
- 250$\mathrm{Im} \frac{ai+b}{ci+d} = \frac{\mathrm{Im} i }{c^2 + d^2}$

#

What is the group of automorphisms?
<img src="./three_punctured.png" width="400">

#

What is the subgroup of automorphisms <br>
fixing the cusp labeled 200$\infty$?

#

- fixes the cusp and midpoint 200$\frac12(1+i)$<br>
- dashed geodesics are invariant under the group<br>
<img src="./three_punctured.png" width="400">

#
### the set 200$X$

- arcs joining cusps 200$\infty, 1$ with 200$\lambda$-length 200$p^2$
- lift to vertical lines with endpoints 200$k/p$ with 200$k$ odd
- 200$|X| = p - 1$ as before

#
### Lemma
Let 200$n$ be a positive integer.
The number of  ways of writing 200$n$  as a  sum of squares
200$n = c^2 + d^2$
with 200$c,d$ coprime integers is equal to the number of  integers 
200$0 \leq k < n-1$ coprime to 200$n$
such that the line
200$\{  k/n + i t,\, t>0  \}$
contains  a point in the 200$\Gamma$  orbit of 200$i$.

#
## subgroup lifts to 

- 200$U': z \mapsto 2-\bar{z},\, V' : z \mapsto \bar{z}/(\bar{z} - 1)$
- composition is 200$U'\circ V' : z \mapsto z \mapsto (-z + 2) /( z + 1)$
- whose fixed point is 200$i+1$.

#

- 200$U': z \mapsto 2-\bar{z}$ induces an automorphism no fixed points in
    200$X,\, p \geq 3$
- 200$V' : z \mapsto \bar{z}/(\bar{z} - 1)$ is an inversion in a circle center
    with endpoints -1 and 1
- projection to surface is simple arc of 200$\lambda$ length 200$=4$

#
## Lemma

The automorphism 200$V$ induced by 200$V'$ <br>
fixes two and exactly two arcs in 200$X$.

- apply Burnside Lemma to prove Theorem 1.2
- 200$4 |X/G| = (p-1) + 2 + |X^{U\circ V}|$

#
## Proof

- If 200$\infty$ and 200$k/p$ are exchanged by an inversion swapping Ford circles
- Then the endpoints of the fixed circle are 200$(k-1)/p$ and 200$(k+1)/p$  
- if 200$1 < k < p-1$ the arc joining these points has 200$\lambda$-length = 4p^2 > 4$

#
## Button's Theorem

If 200$z$ is a Markoff number which is prime<br>
then there is a unique triple 200$z > y > x$

- 200$x^2 + y^2 + z^2 - 3x y z = 0.$
- 200$\bar{x}^2 + \bar{y}^2 = 0.$ in 200$\mathbb{F}_z$
- 200$(\bar{x}/\bar{y})^2 = -1$ in 200$\mathbb{F}_z$

#

- Button's theorem follows from unicity and
- For every Markoff number 200$m$ there are exactly 3 simple closed geodesics of length  200$2\cosh^{-1}(3m/2)$ on the modular torus 200$\mathbb{H}/\Gamma'$ 
- there are exactly 3 simple arcs of 200$\lambda$ length 200$9m^2$ on 200$\mathbb{H}/\Gamma'$ 

# That's all folks!!!!!
