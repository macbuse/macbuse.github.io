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

Acting on <span style="font-size: 150%">$\mathbb{F}_p^*$</span>

<span style="font-size: 150%">$\begin{array}{lll}
x &\mapsto& -x \\
x &\mapsto& 1/x
\end{array}$</span>

Acting on <span style="font-size: 150%">$\mathbb{H}$</span>

<span style="font-size: 150%">$\begin{array}{lll}
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}
\end{array}$</span>

#
## Farey tessalation

<img src="./farey_bicolor.png" width="400">

#
## Ford circles

<img src="./ford_circles.gif" width="400">

#
### Burnside Lemma says

- <span style="font-size: 200%">$G$</span> acting on <span style="font-size: 200%">$X$</span> then 

    <span style="font-size: 250%">$|G| |X/G| = \sum_{g} |X^g|$</span>

- <span style="font-size: 200%">$X^g$</span> =  fixed points of the element <span style="font-size: 200%">$g$</span> 
- <span style="font-size: 200%">$X/G$</span>  the orbit space.

#
## Theorem 1.1

Acting on <span style="font-size: 200%">$X = \mathbb{F}_p^*$</span>

- identity <span style="font-size: 200%">$|X^g| = p-1$</span> 
- <span style="font-size: 200%">$x \mapsto -x, |X^g| = 0$</span>  
- <span style="font-size: 200%">$x \mapsto 1/x, |X^g| = 2$</span>  
- <span style="font-size: 200%">$x \mapsto -1/x, |X^g| = \ldots$</span>  

#


- <span style="font-size: 250%">$|G| |X/G| = \sum_{g} |X^g|$</span>
- <span style="font-size: 250%">$4 |X/G| = (p-1) + 2 + |X^{(x\mapsto -1/x)}|$</span>
- <span style="font-size: 250%">$\Rightarrow  |X^{(x\mapsto -1/x)}|= 2$</span>,, if <span style="font-size: 250%">$4 \not | (p+1)$</span>
- <span style="font-size: 250%">$\Rightarrow  \exists x,\, x^2 = -1$</span>, if <span style="font-size: 250%">$4 \not | (p+1)$</span>


#
## Theorem 1.2: sum of 2 squares

Acting on <span style="font-size: 200%">$\mathbb{H}$</span>

<span style="font-size: 200%">$\begin{array}{lll}
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}
\end{array}$</span>



#
## Primitives

- <span style="font-size: 250%">$\mathbb{Z}^2$</span> 
- infinitely many primitive elements 
- <span style="font-size: 250%">$(a,b)$</span> primitive iff <span style="font-size: 250%">$a,b \in \mathbb{Z}$</span> coprime
- <span style="font-size: 200%">$SL(2,\mathbb{Z})$</span> transitive on primitives


#
## Important

<span style="font-size: 200%">$\{ \textit{primitives} \} = \mathbb{Q}\cup \infty \subset$</span> circle/projective line <span style="font-size: 200%">$= \partial_\infty \mathbb{H}$</span>


#


#
## Farey tessalation


<span style="font-size: 200%">$\mathbb{Q}\cup \infty \subset$</span> circle/projective line

- <span style="font-size: 200%">$(a,b)\text{ primitive } \mapsto a/b \in \mathbb{Q}\cup \infty$</span>
- <span style="font-size: 200%">$\begin{pmatrix} a & c \\ b & d \end{pmatrix} \in \mathrm{SL}(2,\mathbb{Z})\mapsto$</span>  arc joining <span style="font-size: 200%">$(a/b, c/d)$</span> 
- <span style="font-size: 200%">$(a/b, c/d)$</span> are Farey neighbors


#

<img src="./sami.jpg" width="600">

[source](https://www.math.mcgill.ca/sdouba/seminar/sami)

#

<img src="./farey_tree.png" width="600">

[source](https://www3.nd.edu/~math/rtg/GTS/www3.nd.edu/_jquigle2/GSTS%20FA18/Week1P.pdf)

#
## Definitions
- **arc** = Poincaré geodesic joining <span style="font-size: 200%">$a/b, c/d \in \mathbb{Q}\cup \infty$</span>
- **<span style="font-size: 200%">$\lambda$</span>- length of  arc** <span style="font-size: 200%">$= |ad - bc|^2$</span> 

#
## Lemma

**<span style="font-size: 200%">$\log \lambda$</span>- length ** = length of the portion outside Ford circles tangent to the real line at its endpoints


#
## Ford circles

<img src="./ford_circles.gif" width="400">


#

<span style="font-size: 200%">$\mathrm{SL}(2,\mathbb{Z})$</span> acts by Mobius transformations on <span style="font-size: 200%">$\mathbb{H}$</span>

- <span style="font-size: 200%">$\begin{pmatrix} a & c \\ b & d \end{pmatrix}.z = \frac{az+b}{cz+d}$</span> 
- preserves the Poincaré (hyerbolic) metric
- the orbit of <span style="font-size: 200%">$F := \{ z, \mathrm{Im}\, z > 1\}$</span> are the Ford circles

#

<img src="./ford_circles_again.png" width="600">

- point of tangency with <span style="font-size: 200%">$\mathbb{R} = p/q$</span>, diameter = <span style="font-size: 200%">$1/q^2$</span>

#
### Proof of lemma

- **arc** joining <span style="font-size: 200%">$a/b, c/d$</span> has **<span style="font-size: 200%">$\lambda$</span>- length ** <span style="font-size: 200%">$= |ad - bc|^2$</span> 
- **<span style="font-size: 200%">$\log \lambda$</span>- length ** = length of the portion outside Ford circles tangent to the real line at its endpoints


#
### Proof of lemma

- <span style="font-size: 200%">$\mathrm{SL}(2,\mathbb{Z})$</span>  transitive, 
- can suppose <span style="font-size: 200%">$a/b = \infty$</span> and <span style="font-size: 200%">$c/d = k/(ad - bc)$</span>
- Ford circles  <span style="font-size: 200%">$F$</span>  tangent at <span style="font-size: 200%">$\infty$</span>
- and another of diameter <span style="font-size: 200%">$(ad - bc)^2$</span>

#
#
- <span style="font-size: 200%">$\Gamma = \mathrm{SL}(2,\mathbb{Z})$</span> has torsion so <span style="font-size: 200%">$\mathbb{H}/\Gamma$</span> orbifold
- <span style="font-size: 200%">$\Gamma(2) = \ker (\mathrm{SL}(2,\mathbb{Z})\rightarrow  \mathrm{SL}(2,\mathbb{F}_2))$</span>
- <span style="font-size: 200%">$\Gamma' = [\Gamma,\Gamma]$</span>
- <span style="font-size: 200%">$\mathbb{H}/\Gamma(2)$</span>  three punctured sphere 
- <span style="font-size: 200%">$\mathbb{H}/\Gamma'$</span> once punctured torus 

#

In the solution of Aigner's conjectures the geometry of the 
simple geodesics on
<span style="font-size: 200%">$\mathbb{H}/\Gamma'$</span> once punctured torus was important. 

- For Fermat's theorem it's the automorphisms of 
<span style="font-size: 200%">$\mathbb{H}/\Gamma(2)$</span> =  three punctured sphere 

#

A three punctured sphere <br>
can be cut up into 2 ideal triangles.

<img src="./fund_dom_gamma2.png" width="400">

- Fundamental domain for <span style="font-size: 200%">$\Gamma(2)$</span>


#

<img src="./three_punctured.png" width="400">

- <span style="font-size: 200%">$i, 1+i, \frac12 ( 1 + i)$</span> are midpoints

#
## reciprocals of sums of squares

- <span style="font-size: 200%">$i, 1+i, \frac12 ( 1 + i)$</span> are midpoints of arcs
- the lifts to <span style="font-size: 200%">$\mathbb{H}$</span> of the midpoints <span style="font-size: 200%">$=\Gamma.i$</span> 
- <span style="font-size: 250%">$\mathrm{Im} \frac{ai+b}{ci+d} = \frac{\mathrm{Im} i }{c^2 + d^2}$</span>

#

What is the group of automorphisms?
<img src="./three_punctured.png" width="400">

#

What is the subgroup of automorphisms <br>
fixing the cusp labeled <span style="font-size: 200%">$\infty$</span>?


#

- fixes the cusp fixes and midpoint <span style="font-size: 200%">$\frac12(1+i)$</span><br>
- dashed geodesics are invariant under the group<br>
<img src="./three_punctured.png" width="400">

#
### the set <span style="font-size: 200%">$X$</span>

- arcs joining cusps <span style="font-size: 200%">$\infty, 1$</span> with <span style="font-size: 200%">$\lambda$</span>-length <span style="font-size: 200%">$p$</span>
- lift to vertical lines with endpoints <span style="font-size: 200%">$k/p$</span> with <span style="font-size: 200%">$k$</span> odd
- <span style="font-size: 200%">$|X| = p - 1$</span> as before

#
### Lemma
Let <span style="font-size: 200%">$n$</span> be a positive integer.
The number of  ways of writing <span style="font-size: 200%">$n$</span>  as a  sum of squares
<span style="font-size: 200%">$n = c^2 + d^2$</span>
with <span style="font-size: 200%">$c,d$</span> coprime integers
is equal to the number the  integers <span style="font-size: 200%">$0 \leq k < n-1$</span> coprime to <span style="font-size: 200%">$n$</span>
such that the line
<span style="font-size: 200%">$\{  k/n + i t,\, t>0  \}$</span>
contains  a point in the <span style="font-size: 200%">$\Gamma$</span>  orbit of <span style="font-size: 200%">$i$</span>.

#
## subgroup lifts to 

- <span style="font-size: 200%">$U': z \mapsto 2-\bar{z},\, V' : z \mapsto \bar{z}/(\bar{z} - 1)$</span>
- composition is <span style="font-size: 200%">$U'\circ V' : z \mapsto z \mapsto (-z + 2) /( z + 1)$</span>
- whose fixed point is <span style="font-size: 200%">$i+1$</span>.
#

- <span style="font-size: 200%">$U': z \mapsto 2-\bar{z}$</span> induces an automorphism no fixed points in
    <span style="font-size: 200%">$X,\, p \geq 3$</span>
- <span style="font-size: 200%">$V' : z \mapsto \bar{z}/(\bar{z} - 1)$</span> is an inversion in a circle center <span style="font-size: 200%">$1$</span>
