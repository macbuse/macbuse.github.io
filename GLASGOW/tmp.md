%Matchings and snakes
%greg mc
%May 2021


#
## Principal drivers

- [Jim Propp](http://faculty.uml.edu/jpropp/)
- [Ralph Schiffler](https://schiffler.math.uconn.edu/)
- plus many coauthors of both
- a new notion of length ?

#
## length

<span style="font-size: 200%">$(p,q)$</span> curve

- <span style="font-size: 200%">$\sqrt p^2 + q^2$</span>
- <span style="font-size: 200%">$|p| + |q|$</span>
- <span style="font-size: 200%">$\ell_w$</span>
- complexity of another object ?

# 

A matching of a graph G is a set of pairwise non-adjacent edges, none of which are loops.

A perfect matching matches all vertices of the graph.

<img src="./snake_graph1.png" width="300">

#

<img src="./matchings.jpg" height="400">

#
## Matching polynomial

5 perfect matchings

<img src="./snake_graph1.png" width="300">

- <span style="font-size: 250%">$x^4 + y^4 + x^2z^2 + 2x^2y^2$</span>
- match $\rightarrow$ monomial=product of labels 

#

13 perfect matchings

<img src="./snake_6.png" width="600">

[src](https://arxiv.org/pdf/math/0511633.pdf)

#
## Snake graph from primitive 

<span style="font-size: 150%">$A=(1,1)$</span>,
<span style="font-size: 150%">$B=(2,1)$</span>,
<span style="font-size: 150%">$C=(3,2)$</span>

<img src="./trig_snake.png" width="600">

#
## Positivity conjecture

- [cluster algebras](https://en.wikipedia.org/wiki/Cluster_algebra)
- seed is like a Markoff triple <span style="font-size: 150%">$(x,y,z)$</span>
- mutation is like a Vieta flip
- Markoff number <span style="font-size: 150%">$\rightarrow$</span> Laurent polynomial 
- proof (idea) : coeffs are coeffs of the snake polynomial


#
## Positivity conjecture

- [cluster alg. from surfaces](https://www.sciencedirect.com/science/article/pii/S0001870811001423)
- [general case](https://annals.math.princeton.edu/wp-content/uploads/Lee_Schiffler.pdf)


#
## Calculus of arcs/snake graphs

- sophistocated combinatorial proof
- relations to continued fractions
- looking for applications

#

<img src="./matchings.jpg" height="400">

#
## Markoff numbers

<span style="font-size: 150%">$A,B \in \mathbb{Z}^2$</span><br>
<span style="font-size: 150%">$|AB|=$</span> number perfect matchings for associated snake graph

<img src="./matchings_markoff.png" width="900">

[src](https://arxiv.org/pdf/2010.13010.pdf)


#
## Exercise to prove

Prove the relation for matchings of triples of snake graphs

 <span style="font-size: 300%">$tr ab  + tr ab^{-1} = (tr a) (tr b)$</span>


#
## Ptolemy inequality


<img src="./ptolemy_inequality.png" width="900">

#


<img src="./schif_proof.png" width="900">
