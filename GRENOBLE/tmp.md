%Geometry of sums of squares
%greg mc
%November 2021

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

<span style="font-size: 100%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

#
### Odd index Fibonacci numbers are Markoff numbers

$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...$

<span style="font-size: 100%">$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$</span>

# 
### Markoff numbers


<img src="./Markoff_tree_full.svg" width="500">

#
### Frobenius uniqueness conjecture

- The largest integer in a triple determines the two other numbers.
- For every Markoff number <span style="font-size: 100%">$m$</span> there are exactly 3 simple closed geodesics of length  <span style="font-size: 100%">$2\cosh^{-1}(3m/2)$</span> on the modular torus <span style="font-size: 100%">$\mathbb{H}/\Gamma'$</span> 


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

If <span style="font-size: 100%">$z$</span> is a Markoff number which is prime<br>
then there is a unique triple <span style="font-size: 100%">$z > y > x$</span>

- <span style="font-size: 100%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>
- <span style="font-size: 100%">$\bar{x}^2 + \bar{y}^2 = 0.$</span> in <span style="font-size: 100%">$\mathbb{F}_z$</span>
- <span style="font-size: 100%">$(\bar{x}/\bar{y})^2 = -1$</span> in <span style="font-size: 100%">$\mathbb{F}_z$</span>

#

<img src="./theoremsab.png" width="600">

- Button's theorem follows from unicity here


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

<iframe width="560" height="315" src="https://www.youtube.com/embed/0hlvhQZIOQw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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

- <span style="font-size: 100%">$G$</span> acting on <span style="font-size: 100%">$X$</span> then 

    <span style="font-size: 250%">$|G| |X/G| = \sum_{g} |X^g|$</span>

- <span style="font-size: 100%">$X^g$</span> =  fixed points of the element <span style="font-size: 100%">$g$</span> 
- <span style="font-size: 100%">$X/G$</span>  the orbit space.

#
## Theorem 1.1

Acting on <span style="font-size: 100%">$X = \mathbb{F}_p^*$</span>

- identity <span style="font-size: 100%">$|X^g| = p-1$</span> 
- <span style="font-size: 100%">$x \mapsto -x, |X^g| = 0$</span>  
- <span style="font-size: 100%">$x \mapsto 1/x, |X^g| = 2$</span>  
- <span style="font-size: 100%">$x \mapsto -1/x, |X^g| = \ldots$</span>  

#


- <span style="font-size: 250%">$|G| |X/G| = \sum_{g} |X^g|$</span>
- <span style="font-size: 250%">$4 |X/G| = (p-1) + 2 + |X^{(x\mapsto -1/x)}|$</span>
- <span style="font-size: 250%">$\Rightarrow  |X^{(x\mapsto -1/x)}|= 2$</span>,, if <span style="font-size: 250%">$4 \not | (p+1)$</span>
- <span style="font-size: 250%">$\Rightarrow  \exists x,\, x^2 = -1$</span>, if <span style="font-size: 250%">$4 \not | (p+1)$</span>


#
## Theorem 1.2: sum of 2 squares

Acting on <span style="font-size: 100%">$\mathbb{H}$</span>

<span style="font-size: 100%">$\begin{array}{lll}
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}
\end{array}$</span>



#
## Primitives

- <span style="font-size: 250%">$\mathbb{Z}^2$</span> 
- infinitely many primitive elements 
- <span style="font-size: 250%">$(a,b)$</span> primitive iff <span style="font-size: 250%">$a,b \in \mathbb{Z}$</span> coprime
- <span style="font-size: 100%">$SL(2,\mathbb{Z})$</span> transitive on primitives


#
## Important

<span style="font-size: 100%">$\{ \textit{primitives} \} = \mathbb{Q}\cup \infty \subset$</span> circle/projective line <span style="font-size: 100%">$= \partial_\infty \mathbb{H}$</span>


#


#
## Farey tessalation


<span style="font-size: 100%">$\mathbb{Q}\cup \infty \subset$</span> circle/projective line

- <span style="font-size: 100%">$(a,b)\text{ primitive } \mapsto a/b \in \mathbb{Q}\cup \infty$</span>
- <span style="font-size: 100%">$\begin{pmatrix} a & c \\ b & d \end{pmatrix} \in \mathrm{SL}(2,\mathbb{Z})\mapsto$</span>  arc joining <span style="font-size: 100%">$(a/b, c/d)$</span> 
- <span style="font-size: 100%">$(a/b, c/d)$</span> are Farey neighbors


#

<img src="./sami.jpg" width="600">

[source](https://www.math.mcgill.ca/sdouba/seminar/sami)

#

<img src="./farey_tree.png" width="600">

[source](https://www3.nd.edu/~math/rtg/GTS/www3.nd.edu/_jquigle2/GSTS%20FA18/Week1P.pdf)

#
## Definitions
- **arc** = Poincaré geodesic joining <span style="font-size: 100%">$a/b, c/d \in \mathbb{Q}\cup \infty$</span>
- **<span style="font-size: 100%">$\lambda$</span>- length of  arc** <span style="font-size: 100%">$= |ad - bc|^2$</span> 

#
## Lemma

**<span style="font-size: 100%">$\log \lambda$</span>- length ** = length of the portion outside Ford circles tangent to the real line at its endpoints


#
## Ford circles

<img src="./ford_circles.gif" width="400">


#

<span style="font-size: 100%">$\mathrm{SL}(2,\mathbb{Z})$</span> acts by Mobius transformations on <span style="font-size: 100%">$\mathbb{H}$</span>

- <span style="font-size: 100%">$\begin{pmatrix} a & c \\ b & d \end{pmatrix}.z = \frac{az+b}{cz+d}$</span> 
- preserves the Poincaré (hyperbolic) metric
- the orbit of <span style="font-size: 100%">$F := \{ z, \mathrm{Im}\, z > 1\}$</span> are the Ford circles

#

<img src="./ford_circles_again.png" width="600">

- point of tangency with <span style="font-size: 100%">$\mathbb{R} = p/q$</span>, diameter = <span style="font-size: 100%">$1/q^2$</span>

#
### Proof of lemma

- **arc** joining <span style="font-size: 100%">$a/b, c/d$</span> has **<span style="font-size: 100%">$\lambda$</span>- length ** <span style="font-size: 100%">$= |ad - bc|^2$</span> 
- **<span style="font-size: 100%">$\log \lambda$</span>- length ** = length of the portion outside Ford circles tangent to the real line at its endpoints


#
### Proof of lemma

- <span style="font-size: 100%">$\mathrm{SL}(2,\mathbb{Z})$</span>  transitive, 
- can suppose <span style="font-size: 100%">$a/b = \infty$</span> and <span style="font-size: 100%">$c/d = k/(ad - bc)$</span>
- Ford circles  <span style="font-size: 100%">$F$</span>  tangent at <span style="font-size: 100%">$\infty$</span>
- and another of diameter <span style="font-size: 100%">$1/(ad - bc)^2$</span>
- the **midpoint** of this vertical arc is at height <span style="font-size: 100%">$1/|ad - bc|$</span>

#
#
- <span style="font-size: 100%">$\Gamma = \mathrm{SL}(2,\mathbb{Z})$</span> has torsion so <span style="font-size: 100%">$\mathbb{H}/\Gamma$</span> orbifold
- <span style="font-size: 100%">$\Gamma(2) = \ker (\mathrm{SL}(2,\mathbb{Z})\rightarrow  \mathrm{SL}(2,\mathbb{F}_2))$</span>
- <span style="font-size: 100%">$\Gamma' = [\Gamma,\Gamma]$</span>
- <span style="font-size: 100%">$\mathbb{H}/\Gamma(2)$</span>  three punctured sphere 
- <span style="font-size: 100%">$\mathbb{H}/\Gamma'$</span> once punctured torus 

#

In the solution of Aigner's conjectures the geometry of the 
simple geodesics on
<span style="font-size: 100%">$\mathbb{H}/\Gamma'$</span> once punctured torus was important. 

- For Fermat's theorem it's the automorphisms of 
<span style="font-size: 100%">$\mathbb{H}/\Gamma(2)$</span> =  three punctured sphere 

#

A three punctured sphere <br>
can be cut up into 2 ideal triangles.

<img src="./fund_dom_gamma2.png" width="400">

- Fundamental domain for <span style="font-size: 100%">$\Gamma(2)$</span>


#

<img src="./three_punctured.png" width="400">

- <span style="font-size: 100%">$i, 1+i, \frac12 ( 1 + i)$</span> are midpoints

#
## reciprocals of sums of squares

- <span style="font-size: 100%">$i, 1+i, \frac12 ( 1 + i)$</span> are midpoints of arcs
- the lifts to <span style="font-size: 100%">$\mathbb{H}$</span> of the midpoints <span style="font-size: 100%">$=\Gamma.i$</span> 
- <span style="font-size: 250%">$\mathrm{Im} \frac{ai+b}{ci+d} = \frac{\mathrm{Im}\, i }{c^2 + d^2}$</span>

#

What is the group of automorphisms?
<img src="./three_punctured.png" width="400">

#

What is the subgroup of automorphisms <br>
fixing the cusp labeled <span style="font-size: 100%">$\infty$</span>?

#

- fixes the cusp and midpoint <span style="font-size: 100%">$\frac12(1+i)$</span><br>
- dashed geodesics are invariant under the group<br>
<img src="./three_punctured.png" width="400">

#
### the set <span style="font-size: 100%">$X$</span>

- arcs joining cusps <span style="font-size: 100%">$\infty, 1$</span> with <span style="font-size: 100%">$\lambda$</span>-length <span style="font-size: 100%">$p^2$</span>
- lift to vertical lines with endpoints <span style="font-size: 100%">$k/p$</span> with <span style="font-size: 100%">$k$</span> odd
- <span style="font-size: 100%">$|X| = p - 1$</span> as before

#
### Lemma
Let <span style="font-size: 100%">$n$</span> be a positive integer.
The number of  ways of writing <span style="font-size: 100%">$n$</span>  as a  sum of squares
<span style="font-size: 100%">$n = c^2 + d^2$</span>
with <span style="font-size: 100%">$c,d$</span> coprime integers is equal to the number of  integers 
<span style="font-size: 100%">$0 \leq k < n-1$</span> coprime to <span style="font-size: 100%">$n$</span>
such that the line
<span style="font-size: 100%">$\{  k/n + i t,\, t>0  \}$</span>
contains  a point in the <span style="font-size: 100%">$\Gamma$</span>  orbit of <span style="font-size: 100%">$i$</span>.

#
### Proof of lemma


#
## subgroup lifts to 

- <span style="font-size: 100%">$U': z \mapsto 2-\bar{z},\, V' : z \mapsto \bar{z}/(\bar{z} - 1)$</span>
- composition is <span style="font-size: 100%">$U'\circ V' : z \mapsto z \mapsto (-z + 2) /( z + 1)$</span>
- whose fixed point is <span style="font-size: 100%">$i+1$</span>.

#

- <span style="font-size: 100%">$U': z \mapsto 2-\bar{z}$</span> induces an automorphism no fixed points in
    <span style="font-size: 100%">$X,\, p \geq 3$</span>
- <span style="font-size: 100%">$V' : z \mapsto \bar{z}/(\bar{z} - 1)$</span> is an inversion in a circle center
    with endpoints -1 and 1
- projection to surface is simple arc of <span style="font-size: 100%">$\lambda$</span> length <span style="font-size: 100%">$=4$</span>

#
## Lemma

The automorphism <span style="font-size: 100%">$V$</span> induced by <span style="font-size: 100%">$V'$</span> <br>
fixes two and exactly two arcs in <span style="font-size: 100%">$X$</span>.

- apply Burnside Lemma to prove Theorem 1.2
- <span style="font-size: 100%">$4 |X/G| = (p-1) + 2 + |X^{U\circ V}|$</span>

#
## Proof

- If <span style="font-size: 100%">$\infty$</span> and <span style="font-size: 100%">$k/p$</span> are exchanged by an inversion swapping Ford circles
- Then the endpoints of the fixed circle are <span style="font-size: 100%">$(k-1)/p$</span> and <span style="font-size: 100%">$(k+1)/p$</span>  
- if <span style="font-size: 100%">$1 < k < p-1$</span> the arc joining these points has <span style="font-size: 100%">$\lambda$</span>-length = <span style="font-size: 100%">$4p^2 >4$</span> 

#
## Button's Theorem

If <span style="font-size: 100%">$z$</span> is a Markoff number which is prime<br>
then there is a unique triple <span style="font-size: 100%">$z > y > x$</span>

- <span style="font-size: 100%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>
- <span style="font-size: 100%">$\bar{x}^2 + \bar{y}^2 = 0$</span> in <span style="font-size: 100%">$\mathbb{F}_z$</span>
- <span style="font-size: 100%">$(\bar{x}/\bar{y})^2 = -1$</span> in <span style="font-size: 100%">$\mathbb{F}_z$</span>

#

- Button's theorem follows from unicity and
- For every Markoff number <span style="font-size: 100%">$m$</span> there are exactly 3 simple closed geodesics of length  <span style="font-size: 100%">$2\cosh^{-1}(3m/2)$</span> on the modular torus <span style="font-size: 100%">$\mathbb{H}/\Gamma'$</span> 
- exactly 3 simple arcs of <span style="font-size: 100%">$\lambda$</span> length <span style="font-size: 100%">$9m^2$</span> on <span style="font-size: 100%">$\mathbb{H}/\Gamma'$</span> 

# That's all folks!!!!!
