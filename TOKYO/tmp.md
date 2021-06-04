%Part 2
%greg mc
%May 2021


#
### Contents

- Character variety
- Norms and counting
- Proof of Aigner
- Proof by snakes
- More lengths

#
## Character variety

H. Cohn, Approach to Markov’s Minimal Forms Through Modular Functions (1955)


- modular torus = quotient of upper half plane $\mathbb{H}$ by  $\Gamma$ = commutator subgroup of $PSL(2,\mathbb{Z})$, acting by Mobius transformations
-  relates Markoff numbers to lengths of simple closed geodesics

#
## Back to the Torus

- <span style="font-size: 200%">$\mathbb{Z}^2$</span> acting on <span style="font-size: 200%">$\mathbb{R}^2$</span> by translation
- quotient space (orbit space) is a euclidean torus
- primitive elements <span style="font-size: 200%">$(p,q)\in \mathbb{Z}^2$</span> 
- $\rightarrow$ closed curve on torus = $(p,q)$ curve
- (usual) length <span style="font-size: 200%">$=\|(p,q)\| = \sqrt{p^2 + q^2}$</span>

#

## Usual Torus

<img src="./torus_cover.png" width="900">

#

## Torus

- <span style="font-size: 200%">$\mathbb{Z}^2$</span> acts by translation in lots of different ways
- translation lengths of <span style="font-size: 200%">$(1,0),(0,1),(1,-1)$</span> determine (up to conjugation)
- the representation <span style="font-size: 200%">$\mathbb{Z}^2 \rightarrow \text{isom}(\mathbb{R}^2)$</span>
- length of <span style="font-size: 200%">$(p,q)$</span> curve given by quadratic form 

#

representation <span style="font-size: 200%">$\mathbb{Z}^2 \rightarrow \text{isom}(\mathbb{R}^2)$</span>

<img src="./skew_torus.png" height="500">


#

representation <span style="font-size: 200%">$\mathbb{Z}^2 \rightarrow \text{isom}(\mathbb{R}^2)$</span>

<img src="./skew_torus (1).png" height="500">

#
### Threes, triangles, tori

- 3 side lengths determine a triangle
- need 3 numbers to build a euclidean torus
- what about the 3 Markoff numbers ?
- can build a hyperbolic punctured torus
- no simple formula for length of <span style="font-size: 200%">$(p,q)$</span> curve

#

- modular torus = quotient of upper half plane <span style="font-size: 200%">$\mathbb{H}$</span> by  <span style="font-size: 200%">$\Gamma$</span> = commutator subgroup of <span style="font-size: 200%">$\text{PSL}(2, \mathbb{Z})$</span>, acting by Mobius transformations
- hyperbolic torus = quotient of upper half plane <span style="font-size: 200%">$\mathbb{H}$</span>
by  <span style="font-size: 200%">$\Gamma = \rho(\mathbb{Z}*\mathbb{Z})$</span>, 
- <span style="font-size: 200%">$\rho:\mathbb{Z}*\mathbb{Z}\rightarrow\text{PSL}(2, \mathbb{R})$</span> discrete
    faithful

#
## Flat torus
<img src="./torus_cover.png" width="900">

#
## Punctured torus

<img src="./fund_dom.png" width="900">


# 

[Geometry of the Markoff
numbers](https://www.researchgate.net/publication/226685228_The_geometry_of_markoff_numbers){target="_blank"}

<img src="./fund_dom_cut.png" height="300">
<img src="./punctured_torus_series.png" height="300">

#

<span style="font-size: 200%">$\rho:\mathbb{Z}*\mathbb{Z}\rightarrow\text{PSL}(2, \mathbb{R})$</span> 

- lifts to 
 <span style="font-size: 200%">$\hat{\rho}:\mathbb{Z}*\mathbb{Z}\rightarrow\text{SL}(2, \mathbb{R})$</span> 
- character map <span style="font-size: 200%">$\chi : \rho \mapsto ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$</span>
- <span style="font-size: 200%">$a,b$</span> generators of the free group = fundamental group of the torus.

#
Traces behave "like squares of translation lengths"

- [parallogram
    law](https://en.wikipedia.org/wiki/Parallelogram_law){target="_blank}
- <span style="font-size: 200%">$b\in SL(2,\mathbb{C}),\,b^2 - (tr b)b + I_2 = 0$</span> 
- (Cayley-Hamilton) <span style="font-size: 200%">$\Rightarrow$</span>
- <span style="font-size: 200%">$tr ab  + tr ab^{-1} = (tr a) (tr b)$</span>

#

## Markoff cubic from the puncture 

Loop round the puncture <span style="font-size: 200%">$aba^{-1}b^{-1}$</span>

- isn't trivial but it's special (parabolic)
- corresponding matrix something like 
- <span style="font-size: 200%">$\begin{pmatrix} \pm 1 & 6 \\ 0 & \pm 1 \end{pmatrix}$</span> 

#

## puncture condition 

<span style="font-size: 200%">$tr \hat{\rho} (aba^{-1}b^{-1}) = -2$</span>

- <span style="font-size: 200%">$(x,y,z) =  ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$</span>
- <span style="font-size: 200%">$x^2 + y^2 + z^2 - x y z = 2 + tr \hat{\rho} (aba^{-1}b^{-1})=0.$</span>
- = Markoff cubic up to a change of variable

#
## "inverse" character map 

Section: character variety to representation variety

 <span style="font-size: 200%">$\begin{pmatrix}  x & -1 \\ 1 & 0 \end{pmatrix}$</span> 
 <span style="font-size: 200%">$\begin{pmatrix}  0 &  \eta \\ -\eta^{-1} & y \end{pmatrix}$</span> 

<span style="font-size: 200%">$z = \text{trace of  product} = \eta + \eta^{-1}$</span>

#

Cohn shows that 
the permutations and the Vieta flips
used to construct Markov's binary tree
are induced by automorphisms of the
fundamental group of the torus.

#### Exo

- Nielsen move <span style="font-size: 200%">$(a,b,ab) \mapsto (a, b^{-1}, ab^{-1})$</span>
- <span style="font-size: 200%">$tr ab  + tr ab^{-1} = (tr a) (tr b)$</span>

#
## Counting problem

<span style="font-size: 200%">$N(t) =$</span> number of Markoff numbers <span style="font-size: 200%">$\leq t$</span>

- <span style="font-size: 200%">$N(t) = C (\log(3t))^2 + O(\log t)$</span>
- Zagier (1982) [On the Number of Markov Numbers Below a Given Bound.](https://www.ams.org/journals/mcom/1982-39-160/S0025-5718-1982-0669663-7/S0025-5718-1982-0669663-7.pdf) 
- Greg McShane, Igor Rivin [A norm on homology of surfaces and counting simple geodesics](https://arxiv.org/abs/math/0005222){target="_blank"} 

#
### Counting closed simple geodesics


- character map <span style="font-size: 200%">$\chi : \rho \mapsto ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$</span>
- <span style="font-size: 200%">$a,b$</span> generators  fundamental group of the torus.
- <span style="font-size: 200%">$a$</span> generator iff <span style="font-size: 200%">$\exists$</span> essential simple  closed curves representing its conjugacy class



#
### Simple representatives

<img src="./representative.svg" with="650">

#
### Simple representatives in homology

<span style="font-size: 200%">$\phi :  \mathbb{Z}*\mathbb{Z} \rightarrow \mathbb{Z}^2 \simeq
H^1(T,\mathbb{Z})$</span>
abelianizing homomorphism.

- generators <span style="font-size: 200%">$\in \mathbb{Z}*\mathbb{Z}$</span>  <span style="font-size: 200%">$\mapsto$</span> primitive  <span style="font-size: 200%">$\in \mathbb{Z}^2$</span>.
- <span style="font-size: 200%">$(p,q) \in \mathbb{Z}^2$</span>  primitive <span style="font-size: 200%">$\Leftrightarrow p,q$</span> coprime.


#
### La norme

Let <span style="font-size: 200%">$c$</span> be an essential closed curve <span style="font-size: 200%">$\ell_c$</span> its length.

<span style="font-size: 200%">$\gamma \in H^1(T,\mathbb{Z}), \, \| \gamma \| := \inf_{ c \in \gamma} \ell_c/2$</span>

- convexity/triangle inequality
- any pair of curves in linearly independent homology classes intersect
- a curve with self intersections is never a minimizer

#

<img src="./surgery.jpg" width="800">

#

more formally from our paper
<img src="./minimizers.png" width="800">
<img src="./minimizer2.png" width="800">

#
## Unit ball

<img src="./holed_torus.png" width="500">

#
## Corollary

The length function does not coincide with any reasonable function

- not differentiable at rational slopes
- is well approximated by piecewise linear

#
### Unit ball and counting

- <span style="font-size: 200%">$\sharp \{ \gamma,\, \| \gamma \| \leq t \} \sim \text{area unit ball}\times t^2$</span> 
- <span style="font-size: 200%">$\sharp \{ \gamma \text{ primitive},\, \| \gamma \| \leq t \} \sim \frac{6}{\pi^2}\text{area unit ball}\times t^2$</span> 
- the area of the unit ball depends on the hyperbolic structure
- with Rivin we studied it, but now it's called the Mirzakhani function :(
- <span style="font-size: 200%">$\frac{6}{\pi^2}$</span> = [proba 2 random integers
    coprime](https://hal.archives-ouvertes.fr/hal-01413829/document){target="_blank"}

#
## Why log ?
<span style="font-size: 200%">$N(t) = C (\log 3 ))^2 + O(\log t)$</span>

- <span style="font-size: 200%">$m_{p/q} = \frac13 tr \hat{\rho}( \gamma_{p/q})$</span>
- <span style="font-size: 200%">$= \frac23 \cosh\left(\frac{\ell_{\gamma_p}}{2} \right)$</span>
- <span style="font-size: 200%">$= \frac23 \cosh(\| (q,p) \|_s)$</span>


#
## Aigner's conjectures 
<img src="./aigner_mono.png" width="700">

#
## Aigner's conjectures 

Let <span style="font-size: 200%">$p, q$</span> be real non negative numbers and <span style="font-size: 200%">$i > 0$</span> then

- <span style="font-size: 200%">$\|(q,p) \|_s < \|(q + i,p) \|_s$</span>
- <span style="font-size: 200%">$\|(q,p) \|_s < \|(q ,p +i ) \|_s$</span>
- If in addition <span style="font-size: 200%">$p < q$</span> then
<span style="font-size: 200%">$\|(q ,p  ) \|_s < \|(q + i ,p -i ) \|_s$</span>

#
## Aigners conjectures proof


<img src="./lines.png" width="700">


#
##

<img src="./schiffler.png" width="700">

[source](https://arxiv.org/pdf/2010.13010.pdf){target="_blank"}



#
## Pair of pants

- coprime <span style="font-size: 200%">$(p,q) \mapsto w_{p,q} \in \langle a,b \rangle$</span>
- extend length from <span style="font-size: 200%">$\mathbb{Z}^2$</span> to <span style="font-size: 200%">$\mathbb{R}^2$</span> 
- technically, can be done in general using immersed train tracks


#
## Goldman integer pts, orbifolds

<span style="font-size: 200%">$x^2 + y^2 + z^2 - x y z = 20.$</span>

- different <span style="font-size: 150%">$GL(2,\mathbb{Z})$</span> orbts
- (2,2,-2) three punctured sphere
- (0,3,1) orbifold, disc with 2 cone points
- (0, 4,2) orbifold, punctured disc one cone point


#
## Three punctured sphere

<img src="./punctured_sphere.png" width="600">


#
## Pair of pants


<span style="font-size: 200%">$x^2 + y^2 + z^2 - x y z \geq  20.$</span>

<img src="./three_holed_longer_longer.png" width="500">

#
## (0,4,2) orbifold

<img src="./cylinder_pi.png" width="600">

#
## (0,3,1) orbifold

<img src="./cylinder_2pi_3.png" width="600">


#
## 

<img src="./main theorem.png" width="600">

# Thanks

