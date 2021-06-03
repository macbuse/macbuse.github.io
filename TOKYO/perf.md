#

# Matchings and snakes

- [Jim Propp](http://faculty.uml.edu/jpropp/){target="_blank"}
- [Ralph Schiffler](https://schiffler.math.uconn.edu/){target="_blank"}
- plus many coauthors of both
- a new notion of length ?

#
## length

150$(p,q)$ curve

- 150$\sqrt p^2 + q^2$
- 150$|p| + |q|$
- 150$\ell_w$
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

- 250$x^4 + y^4 + x^2z^2 + 2x^2y^2$
- match 150$\rightarrow$ monomial=product of labels 

#

13 perfect matchings

<img src="./snake_6.png" width="600">

[src](https://arxiv.org/pdf/math/0511633.pdf){target="_blank"}

#
## Snake graph from primitive 

200$A=(1,1)$,
200$B=(2,1)$,
200$C=(3,2)$

<img src="./trig_snake.png" width="600">

#
## Positivity conjecture

- [cluster algebras](https://en.wikipedia.org/wiki/Cluster_algebra){target="_blank"}
- seed is like a Markoff triple 200$(x,y,z)$
- mutation is like a Vieta flip
- Markoff number 200$\rightarrow$ Laurent polynomial 
- proof (idea) : coeffs are coeffs of the snake polynomial


#
## Positivity conjecture

- [cluster alg. from surfaces](https://www.sciencedirect.com/science/article/pii/S0001870811001423){target="_blank"}
- [general case](https://annals.math.princeton.edu/wp-content/uploads/Lee_Schiffler.pdf){target="_blank"}


#
## Calculus of arcs/snake graphs

- sophistocated combinatorial proof
- relations to continued fractions
- looking for applications

#

<img src="./matchings.jpg" height="400">

#
## Markoff numbers

200$A,B \in \mathbb{Z}^2$<br>
200$|AB|=$ number perfect matchings for associated snake graph

<img src="./matchings_markoff.png" width="900">

[src](https://arxiv.org/pdf/2010.13010.pdf)


#
## Exercise to prove

Prove the relation for matchings of triples of snake graphs

 300$tr ab  + tr ab^{-1} = (tr a) (tr b)$


#
## Ptolemy inequality


<img src="./ptolemy_inequality.png" width="900">

#


<img src="./schif_proof.png" width="900">
