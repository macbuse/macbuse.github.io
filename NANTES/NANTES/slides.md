%Markoff numbers 
%greg mc
%mars 2021

#

<img src="./Martin_Aigner.jpg" width="400">

- [Proofs from THE BOOK](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK#:~:text=Proofs%20from%20THE%20BOOK%20is,proof%20of%20each%20mathematical%20theorem){target="_blank"}
- [Convexity and Aigner's Conjectures](https://arxiv.org/abs/2101.03316){target="_blank"}
- Can I prove these with one figure ?


#

Markov numbers are integers that appear in triples which are solutions of
a Diophantine equation the so-called Markov cubic

200$x^2 + y^2 + z^2 - 3x y z = 0.$

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

# 
## infinity of Markoff numbers

$\begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$
is an automorph of 150$x^2 + y^2  - 3x y.$

 so 150$( v_n,v_{n+1},1)$ is a solution where

200$\begin{pmatrix}v_{n+1} \\ v_n \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix}1 \\ 1 \end{pmatrix}$

#
### Odd index Fibonacci numbers are Markoff numbers

$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...$

200$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

#
### Frobenius uniqueness conjecture


The largest integer in a triple determines the two other numbers.

#
### Aigner's monotonicity conjectures

- Markov’s theorem and 100 years of the uniqueness conjecture. A mathematical journey from irrational numbers to perfect matchings.  2013.  
- M. Rabideaua, R. Schiffler,
Continued fractions and orderings on the Markov numbers,
Advances in Mathematics Vol 370,  2020.
- C Lagisquet and E. Pelantová and S. Tavenas and L. Vuillon, On the Markov numbers: fixed numerator, denominator, and sum conjectures.

#

there is a natural map

200$\mathbb{Q}\cup \infty \rightarrow$ Markoff numbers

200$p/q \mapsto m_{p,q}$

<img src="./aigner_mono.png" width="700">

#
### Geometric structure

- group action 
- 200$\mathbb{Z}/2 * \mathbb{Z}/2 * \mathbb{Z}/2$ action
- [Vieta
    flipping](https://en.wikipedia.org/wiki/Vieta_jumping){target="_blank"}


#
### Vieta flips/involutions
250$x^2 + y^2 + z^2 - 3x y z = 0.$

- quadratic in 200$x$,  two roots 200$x^\pm$
- 200$x^+ + x^- = 3yz$
- involution 200$(x,y,z) \mapsto (3yz -x, y,z)$

#

Peter Sarnak (Princeton and IAS)

Title: Strong approximation for Markoff surfaces

We discuss the transitivity properties of the group of morphisms generated by Vieta involutions on the solutions in congruences to the Markoff equation as well as to other Markoff type affine cubic surfaces. These are dictated in part by the finite orbits of these actions on the algebraic points

Joint work with J.Bourgain and A.Gamburd.

# Automorphisms

- Vieta flips
- (cyclic) permutations of 200$x,y,z$
- get 200$\mathbb{Z}/2 * \mathbb{Z}/3$ action
- = 200$PSL(2,\mathbb{Z})$ action

#
Natural  = 200$PSL(2,\mathbb{Z})$-equivariant map

200$\mathbb{Q}\cup \infty \rightarrow$ Markoff numbers 200$p/q \mapsto m_{p/q}$

- 200$(1:1) \mapsto  1/1 \mapsto 2$ 
- 200$(0:1) \mapsto  0/1 \mapsto 1$ 
- 200$(1:0) \mapsto  \infty \mapsto 1$ 
- actions = projective on left and by autos on right

# 
### Tree structure

comes from Cayley graph of
 200$PSL(2,\mathbb{Z})$ 

<img src="./Markoff_tree_full.svg" width="500">

#
## Modern theory 

H. Cohn, Approach to Markov’s Minimal Forms Through Modular Functions (1955)


- modular torus = quotient of upper half plane 200$\mathbb{H}$ by  200$\Gamma$ = commutator subgroup of 200$\text{PSL}(2, \mathbb{Z})$, acting by Mobius transformations
-  relates Markoff numbers to lengths of simple closed geodesics

#

- modular torus = quotient of upper half plane 200$\mathbb{H}$ by  200$\Gamma$ = commutator subgroup of 200$\text{PSL}(2, \mathbb{Z})$, acting by Mobius transformations
- hyperbolic torus = quotient of upper half plane 200$\mathbb{H}$
by  200$\Gamma = \rho(\mathbb{Z}*\mathbb{Z})$, 
- 200$\rho:\mathbb{Z}*\mathbb{Z}\rightarrow\text{PSL}(2, \mathbb{R})$ discrete
    faithful

# 

200$\rho:\mathbb{Z}*\mathbb{Z}\rightarrow\text{PSL}(2, \mathbb{R})$ 

- lifts to 
 200$\hat{\rho}:\mathbb{Z}*\mathbb{Z}\rightarrow\text{SL}(2, \mathbb{R})$ 
- character map 200$\chi : \rho \mapsto ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$
- 200$a,b$ generators of the free group = fundamental group of the torus.

#

## puncture condition 

200$tr \hat{\rho} (aba^{-1}b^{-1}) = -2$

- 200$(x,y,z) =  ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$
- 200$x^2 + y^2 + z^2 - x y z = 0.$
- = Markoff cubic up to a change of variable

#

Cohn shows that 
the permutations and the Vieta flips
used to construct Markov's binary tree
are induced by automorphisms of the
fundamental group of the torus.

#### Exo

- Nielsen moves
- 200$tr ab  + tr ab^{-1} = (tr a) (tr b)$

#
## Counting problem

200$N(t) =$ number of Markoff numbers 200$\leq t$

200$N(t) = C (\log(3t))^2 + O(\log t)$

- Zagier (1982) [On the Number of Markov Numbers Below a Given Bound.](https://www.ams.org/journals/mcom/1982-39-160/S0025-5718-1982-0669663-7/S0025-5718-1982-0669663-7.pdf) 
- Greg McShane, Igor Rivin [A norm on homology of surfaces and counting simple geodesics](https://arxiv.org/abs/math/0005222){target="_blank"} 

#
### Counting closed simple geodesics


- character map 200$\chi : \rho \mapsto ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$
- 200$a,b$ generators  fundamental group of the torus.
- 200$a$ generator iff 200$\exists$ essential simple  closed curves representing its conjugacy class



#
### Simple representatives

<img src="./representative.svg" with="650">

#
### Simple representatives in homology

200$\phi :  \mathbb{Z}*\mathbb{Z} \rightarrow \mathbb{Z}^2 \simeq
H^1(T,\mathbb{Z})$.
abelianizing homomorphism.

- takes generators of  200$\mathbb{Z}*\mathbb{Z}$ to generators of 200$\mathbb{Z}^2$.
- 200$(m,n) \in \mathbb{Z}^2$  generator 200$\Leftrightarrow m,n$ coprime.


#
### La norme

Let 200$c$ be an essential closed curve 200$\ell_c$ its length.

200$\gamma \in H^1(T,\mathbb{Z}), \, \| \gamma \| := \inf_{ c \in \gamma} \ell_c/2$

- convexity/triangle inequality
- any pair of curves in linearly independent homology classes intersect
- a curve with self intersections is never a minimizer

#

<img src="./surgery.jpg" width="800">

#

<img src="./minimizers.png" width="800">
<img src="./minimizer2.png" width="800">

#
## Unit ball

<img src="./holed_torus.png" width="500">

#
### Unit ball and counting

- 200$\sharp \{ \gamma,\, \| \gamma \| \leq t \} \sim \text{area unit ball}\times t^2$ 
- 200$\sharp \{ \gamma \text{ primitive},\, \| \gamma \| \leq t \} \sim \frac{6}{\pi^2}\text{area unit ball}\times t^2$ 
- the area of the unit ball depends on the hyperbolic structure
- with Rivin we studied it, but now it's called the Mirzakhani function :(

#
## Why log ?
200$N(t) = C (\log(3t)^2 + O(\log t)$

- 200$m_{p/q} = \frac13 tr \hat{\rho}( \gamma_{p/q})$
- 200$= \frac23 \cosh\left(\frac{\ell_{\gamma_p}}{2} \right)$
- 200$= \frac23 \cosh(\| (q,p) \|_s)$


#
## Aigner's conjectures 
<img src="./aigner_mono.png" width="700">

#

[On the ordering of the Markov numbers](https://arxiv.org/abs/2010.13010){target="_blank"}
Kyungyong Lee, Li Li, Michelle Rabideau, Ralf Schiffler

The proof uses a connection to cluster algebras. It was observed
in [P, BBH] that the Markov numbers can be obtained from the cluster variables in the cluster
algebra of the once-punctured torus by specializing the initial cluster variables to 1. Moreover, the clusters in the cluster algebra then specialize to the Markov triples. On the other hand, the cluster variables can be computed by a combinatorial formula given as a summation over the perfect matchings of a so-called snake graph.

#
## Aigner's conjectures 

Let 200$p, q$ be real non negative numbers and 200$i > 0$ then

- 200$\|(q,p) \|_s < \|(q + i,p) \|_s$
- 200$\|(q,p) \|_s < \|(q ,p +i ) \|_s$
- If in addition 200$p < q$ then
200$\|(q ,p  ) \|_s < \|(q + i ,p -i ) \|_s$

#
## Aigner's conjectures proof


<img src="./lines.png" width="700">


#
##

<img src="./schiffler.png" width="700">

[source](https://arxiv.org/pdf/2010.13010.pdf){target="_blank"}