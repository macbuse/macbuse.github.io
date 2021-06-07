%Markoff numbers 
%greg mc
%June 2021

#
##University of Glasgow

June 7th 2021

- Undergrad 1983-87
- [Alex Miller](https://otago.academia.edu/AlexMiller)
- [(S)Tony Mulholland](https://research-information.bris.ac.uk/en/persons/anthony-mulholland)

#
### quote

- you realise that we are the only normal people here?
- What makes you think that we are normal?

# Contents

- Markoff numbers and Frobenius conjecture
- Aigners monotonicity conjectures
- Group actions and labelling numbers
- Visualizing Markoff numbers
- Norms, Growth, Convexity

#

<img src="./Martin_Aigner.jpg" width="400">

- Author of [Proofs from THE BOOK](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK#:~:text=Proofs%20from%20THE%20BOOK%20is,proof%20of%20each%20mathematical%20theorem){target="_blank"}
- [Convexity and Aigner's Conjectures](https://arxiv.org/abs/2101.03316){target="_blank"}
- Can I prove these with one figure ?

#

Markov numbers are integers that appear in triples which are solutions of
a Diophantine equation the so-called Markov cubic

<span style="font-size: 200%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>

$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$

# 
## infinity of Markoff numbers

$\begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$
is an automorph of <span style="font-size: 200%">$x^2 + y^2  - 3x y.$</span>

so <span style="font-size: 200%">$( v_n,v_{n+1},1)$</span> is a solution to Markov cubic:

<span style="font-size: 150%">$\begin{pmatrix}v_{n+1} \\ v_n \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix}1 \\ 1 \end{pmatrix}$</span>

#
### Odd index Fibonacci numbers are Markoff numbers

$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...$

<span style="font-size: 200%">$(1,1,1),(1,1,2),(1,2,5),(1,5,13)$</span>

#
### Frobenius uniqueness conjecture


The largest integer in a triple (x,y,z)<br>
determines the two other numbers.

#
### Partial results

m = Markoff number

- Jack Button for [m prime power](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610798006292){target="_blank"}
- Zhang [An elementary proof...](https://arxiv.org/abs/math/0606283){target="_blank}
- Baragar [m, 3m - 2, 3m + 2 prime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/88B0E426FFCBEA8B3A345C1074B8CC59/S0008439500018828a.pdf/on-the-unicity-conjecture-for-markoff-numbers.pdf){target="_blank}
- [ Bugeaud, Reutenauer, Siksek](https://core.ac.uk/download/pdf/82088222.pdf){target="_blank}
- [Multiplicities of simple closed geodesics](https://projecteuclid.org/journals/geometry-and-topology/volume-12/issue-4/Multiplicities-of-simple-closed-geodesics-and-hypersurfaces-in-Teichm%C3%BCller-space/10.2140/gt.2008.12.1883.full){target="_blank}
- Conclusion too hard!!!


#
### Aigner's monotonicity conjectures

- Markov’s theorem and 100 years of the uniqueness conjecture. A mathematical journey from irrational numbers to perfect matchings.  2013.  
- M. Rabideaua, R. Schiffler,
Continued fractions and orderings on the Markov numbers,
Advances in Mathematics Vol 370,  2020.
- C Lagisquet and E. Pelantová and S. Tavenas and L. Vuillon, On the Markov numbers: fixed numerator, denominator, and sum conjectures.


#

There is a natural map (we'll see why shortly)

<span style="font-size: 200%">$\mathbb{Q}\cup \infty \rightarrow$</span> Markoff numbers

<span style="font-size: 200%">$p/q \mapsto m_{p/q}= m_{p,q}$</span>


<img src="./aigner_mono.png" width="700">

# 
## A tale of three trees

Labeling Markoff numbers

- Markoff number = <span style="font-size: 250%">$m_{p/q}$</span>
- Farey tree of coprime integers <span style="font-size: 250%">$p,q$</span>
- Markoff tree of solutions to his cubic
- Bass-Serre of a free product (<span style="font-size: 250%">$PSL(2,\mathbb{Z})$</span>)

# 
## Story of correspondences 

- <span style="font-size: 200%">$GL(2,\mathbb{Z})$</span> and its actions
- coprime integers <span style="font-size: 250%">$p,q$</span>
- simple closed geodesics on a torus
- snake graphs
- "lengths"


# 
### Lines on grids

<div class="wrap"><iframe data-src="./snake2.html" > </iframe></div>



# 
### Lines on grids

<div class="wrap"><iframe data-src="./snake1.html" > </iframe></div>




# 
### Lines on grids


 coprime integers <span style="font-size: 250%">$p,q$</span> live in a grid with a line

<img src="./grid_pq.jpg" height="400">

#
## Matchings

<img src="./matchings.jpg" height="400">


#
## Favorite Groups

- <span style="font-size: 250%">$\mathbb{Z}$</span> fundamental group of circle
- <span style="font-size: 250%">$\mathbb{Z}^2$</span> fundamental group of torus

#
## Generators/primitives

- <span style="font-size: 250%">$\mathbb{Z}^2$</span> acting by translation on <span style="font-size: 250%">$\mathbb{R}^2$</span>.
- infinitely many primitive elements 
- <span style="font-size: 250%">$(a,b)$</span> primitive iff <span style="font-size: 250%">$a,b \in \mathbb{Z}$</span> coprime

#
## Two choices (red/blue pill)

Next most interesting groups ?

- free product <span style="font-size: 200%">$\mathbb{Z}*\mathbb{Z}$</span>
- automorphism group  <span style="font-size: 200%">$GL(2,\mathbb{Z})$</span>
- both lead to hyperbolic geometry

#
## Actions

- <span style="font-size: 200%">$GL(2,\mathbb{Z})$</span> acting by "base change" on <span style="font-size: 200%">$\mathbb{Z}^2$</span>
- Bezout's identity <span style="font-size: 200%">$\Rightarrow$</span> transitive on primitives
- Visualize  <span style="font-size: 200%">$GL(2,\mathbb{Z})$</span> action 

#

<span style="font-size: 200%">$\mathbb{Q}\cup \infty \subset$</span> circle/projective line

- <span style="font-size: 200%">$(a,b)\text{ primitive } \mapsto a/b \in \mathbb{Q}\cup \infty$</span>
- <span style="font-size: 200%">$\begin{pmatrix} a & c \\ b & d \end{pmatrix} \mapsto$</span>  arc joining <span style="font-size: 200%">$(a/b, c/d)$</span> 
- <span style="font-size: 200%">$(a/b, c/d)$</span> are Farey neighbors

#

<img src="./sami.jpg" width="600">

[source](https://www.math.mcgill.ca/sdouba/seminar/sami)

#

<img src="./farey_tree.png" width="600">

[source](https://www3.nd.edu/~math/rtg/GTS/www3.nd.edu/_jquigle2/GSTS%20FA18/Week1P.pdf)

#
### natural map ?

<span style="font-size: 200%">$\mathbb{Q}\cup \infty \rightarrow$</span> Markoff numbers

<span style="font-size: 200%">$p/q \mapsto m_{p,q}$</span>

- projective <span style="font-size: 200%">$GL(2, \mathbb{Z})$</span> action on <span style="font-size: 200%">$\mathbb{Q}\cup \infty$</span> 
- action on Markoff numbers ?
- [Vieta flipping](https://en.wikipedia.org/wiki/Vieta_jumping){target="_blank"}


#
### Vieta flips/involutions
<span style="font-size: 250%">$x^2 + y^2 + z^2 - 3x y z = 0.$</span>

- quadratic in <span style="font-size: 200%">$x$</span>,  two roots <span style="font-size: 200%">$x^\pm$</span>
- <span style="font-size: 200%">$x^+ + x^- = 3yz$</span>
- involution <span style="font-size: 200%">$(x,y,z) \mapsto (3yz -x, y,z)$</span>

#

Peter Sarnak (Princeton and IAS)

Title: Strong approximation for Markoff surfaces

We discuss the transitivity properties of the group of morphisms generated by Vieta involutions on the solutions in congruences to the Markoff equation as well as to other Markoff type affine cubic surfaces. These are dictated in part by the finite orbits of these actions on the algebraic points

Joint work with J.Bourgain and A.Gamburd.

#
## Automorphisms 

- Vieta flips
- (cyclic) permutations of <span style="font-size: 200%">$x,y,z$</span>
- get <span style="font-size: 200%">$\mathbb{Z}/2 * \mathbb{Z}/3$</span> action
- = [<span style="font-size: 200%">$PSL(2,\mathbb{Z})$</span> action](https://en.wikipedia.org/wiki/Modular_group){target="_blank}

#
Natural  = <span style="font-size: 200%">$PSL(2,\mathbb{Z})$</span>-equivariant map

<span style="font-size: 150%">$\mathbb{Q}\cup \infty \rightarrow$</span> Markoff numbers <span style="font-size: 150%">$p/q \mapsto m_{p/q}$</span>

- <span style="font-size: 150%">$(1:1) \mapsto  1/1 \mapsto 2$</span> 
- <span style="font-size: 150%">$(0:1) \mapsto  0/1 \mapsto 1$</span> 
- <span style="font-size: 150%">$(1:0) \mapsto  \infty \mapsto 1$</span> 
- actions = projective on left and by autos on right

# 
### Tree structure

comes from Bass-Serre tree of
 <span style="font-size: 200%">$PSL(2,\mathbb{Z})$</span> 

<img src="./Markoff_tree_full.svg" width="500">

#
## Visualization

- so we have seen the structure of the Markoff numbers
- is there a better way?
- is there hidden information?

#
## Motivation

<span style="font-size: 200%">$x^2 + y^2 + z^2 - x y z = 0.$</span>

- positive characteristic Sarnak et al.
- over <span style="font-size: 200%">$\mathbb{C}$</span> ? 
- Bowditch
- Sakuma et al.
- SP Tan et al.

#
## Fibonacci growth

[Bowditch](http://homepages.warwick.ac.uk/~masgak/papers/bhb-markoff.pdf){target="_blank"}

<img src="./fib_growth.png" width="800">

#
## Fibonacci growth

<img src="./fib_growth.png" width="800">

- <span style="font-size: 200%">$a,b$</span> generate <span style="font-size: 200%">$\mathbb{Z}*\mathbb{Z}$</span>
- coprime <span style="font-size: 200%">$(p,q) \mapsto w \in \langle a, b \rangle$</span>
- <span style="font-size: 200%">$1/c (|p| + |q|) \leq \ell_w \leq  c(|p| + |q|)$</span>
- [Svarc-Milnor](https://en.wikipedia.org/wiki/%C5%A0varc%E2%80%93Milnor_lemma)


#
### Is there a norm hidden here?


