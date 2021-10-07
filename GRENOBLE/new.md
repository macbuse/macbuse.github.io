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
### Burnside Lemma says

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

- Define **midpoint$$ of this arc to be...


#
### Proof of lemma

- 200$\mathrm{SL}(2,\mathbb{Z})$  transitive, 
- can suppose 200$a/b = \infty$ and 200$c/d = k/(ad - bc)$
- Ford circles  200$F$  tangent at 200$\infty$
- and another of diameter 200$(ad - bc)^2$

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

- arcs joining cusps 200$\infty, 1$ with 200$\lambda$-length 200$p$
- lift to vertical lines with endpoints 200$k/p$ with 200$k$ odd
- 200$|X| = p - 1$ as before

#
### Lemma
Let 200$n$ be a positive integer.
The number of  ways of writing 200$n$  as a  sum of squares
200$n = c^2 + d^2$
with 200$c,d$ coprime integers
is equal to the number the  integers 200$0 \leq k < n-1$ coprime to 200$n$
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
- 200$V' : z \mapsto \bar{z}/(\bar{z} - 1)$ is an inversion in a circle center 200$1$
- projection to surface 200$\lambda$ length is 200$4$

#
## Lemma

The automorphism induced by 200$U'$ fixes two and exactly two arcs in 200$X$.
