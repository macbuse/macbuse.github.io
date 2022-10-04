<title> Toponogov </title>

# differentiability

This is an outline of the ideas behind Theorem 2.1. of the paper ["Simple curves on tori"](https://arxiv.org/abs/math/0005220).


It is standard that every convex function admits left and right derivatives at every point 
and that these are equal except possibly at countably many points. One can view the boundary 
of a convex set as being locally a convex function so the same is true,
that is it is a smooth except possibly at countably many points

For the stable norm the corner part, that is non differentiability at rational slopes,
isn't difficult to do and there is a proof in [this paper](https://arxiv.org/abs/2107.13499).
As for the flatness there is technically [a proof of this](https://arxiv.org/abs/2001.05557),
which is essentially what we had in mind in the paragraph after Theorem 2.2,
although our approach has a much more geometric flavour.

The idea is that if we have a convex function and look at the graph
around a minimum at smaller and smaller scales then 
the height of the graph gets vanishingly small compared with it's width.
To do this for the stable norm we will compare it with a sequence
of euclidean norms.


## Squeezing and differentiability


We want to show that the euclidean norm ball is smooth in a round about way
by viewing it as the graph over a line segment and then bounding the 
graph from above by the graph of a very simple quadratic function.
This method works in general provided that the point in question
can be *approximated from the right and left* by points 
corresponding to primitive homology classes.

---

**Approximation**
The notion of approximated from the right and left
was introduced in [my thesis](http://wrap.warwick.ac.uk/4008/) for geodesics on a punctured surface
but for the torus it is just a fact about continued fractions 
(see [here](https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents))
: if $\zeta$ is an irrational and $p_n/q_n$ the sequence of convergents
then (after possibly renumbering)
$$p_{2n}/q_{2n} < \zeta < p_{2n+1}/q_{2n+1}.$$

You should think of the vectors below  as being 
$$v_0= (p_{2n},q_{2n}), v_1 = (p_{2n+1},q_{2n+1}).$$

---


Let $v_0,v_1 \in \mathbb{R}^2$ be pair of linearly independent vectors and
$\|.\|$ be an arbitrary norm on $\mathbb{R}$.

Given a norm $\|. \|$ then there are two obvious norms on $\mathbb{R}$ that one can compare it with:

1. The one norm $\|x v_0 + y v_1 \|_1 := |x|\|v_0\| + |v| \|v_1\|$
1. The hilbert norm $\| x v_0 + y v_1 \|_2^2 := |x|^2\|v_0\|^2 +2 \|v_0\|^\|v_1\|\cos(\theta) +  |y|^2 \|v_1\|^2$

Here $\theta$ might be the angle between $v_0, v_1$ but it may be thought of as
an arbitrary parameter.

By a standard calculation

$$\| x v_0 + y v_1 \|_1^2 - \| x v_0 + y v_1 \|_2^2  =   2 |x| |y| \|v_0\|\|v_1\| sin^2(\theta/2)$$

which gives

<!-- $$\| x v_0 + y v_1 \|_1 - \| x v_0 + y v_1 \|_2  =   \frac{2|x| |y| \|v_0\|\|v_1\| sin^2(\theta/2)}{\| x v_0 + y v_1 \|_1 + \| x v_0 + y v_1 \|_2}$$ -->
$$\| x v_0 + y v_1 \|_1 - \| x v_0 + y v_1 \|_2  =   
(2|x| |y| \|v_0\|\|v_1\| sin^2(\theta/2))/( x v_0 + y v_1 \|_1 + \| x v_0 + y v_1 \|_2)$$


so that

<!-- $$0 \leq \| x v_0 + y v_1 \|_1 - \| x v_0 + y v_1 \|_2  \leq   \frac{2 |x| |y| \|v_0\|\|v_1\| sin^2(\theta/2)}{2\| x v_0 + y v_1 \|_2}.$$ -->
$$0 \leq \| x v_0 + y v_1 \|_1 - \| x v_0 + y v_1 \|_2  \leq   (2 |x| |y| \|v_0\|\|v_1\| sin^2(\theta/2))/(2\| x v_0 + y v_1 \|_2).$$


Now we want to show that the euclidean norm ball is smooth in a round about way.
We divide by norms and suppose that $\|v_0\|= \|v_1\|=1$
and define $v_t := (1-t)v_0 + tv_1$ so that the estimate above becomes:
$$0 \leq \|  v_t \|_1 - \| v_t\|_2  \leq   2 t(1-t) sin^2(\theta/2)/m,$$
where $m := \inf_{0 \leq t \leq 1} \| v_t \|_2$, which is bounded away from $0$ since $v_0,v_1$ is a basis
and under the hypothesis $\|v_0\|= \|v_1\|=1$ it is just $\cos(\theta/2)$.
Now to simplify the argument we will suppose that $v_t$ is a horizontal line 
and we consider the portion of the euclidean norm ball above the segment
$v_t,\, 0 \leq t \leq 1$
it is easy to see that this is the graph of a function which lies between the line segment and the graph of
$$ t \mapsto  2t(1-t) sin^2(\theta/2)/m,$$
which is a parabola.
Now we are interested in the behavior of vectors tangent to support planes as $\theta \rightarrow 0$.
The distance between $v_0$ and $v_1$ is $O(\theta)$ and the distance between $v_0$ and $v_t$ is roughly $t$
and we'll use this later to calculate tangents.

For the point $A(t)$ on the parabola corresponding to $t$ the tangent vector is inside a cone
bounded by lines tangent to $A(0)A(t)$ and $A(1)A(t)$.
One can estimate the slope of these lines in:
in the case of $A(0)A(t)$  this is 

<!-- $$\frac{2t(1-t) \sin^2(\theta/2)}{2t\sin(\theta/2)} = (1-t) \sin(\theta/2).$$ -->
$$(2t(1-t) \sin^2(\theta/2))/(2t\sin(\theta/2)) = (1-t) \sin(\theta/2).$$

So this is bounded between $0$ and $\sin(\theta/2)$. 

By elementary geometry the same estimate is holds for points on the portion 
of the euclidean norm ball *squeezed* between the chord (the $\|.\|_1$ norm ball) and the parabola. It is easy to see from this that the norm ball is differentiable.



![**Figure:** The euclidean ball getting squeezed](./triangle.png)


## Comparison norm

The above argument will work for the stable norm $\|. \|_s$ 
provided we can bound it from above (locally) by a euclidean norm.
This follows from a general principle in negative curvature:
**distances are always greater than they are in a "comparable" euclidean/flat configuration.**


Let $v_0$ and $v_1$ be primitive homology classes which form a basis. Then one
has: 
$$\sinh(\|v_0\|_s/2)\sinh(\|v_1\|_s/2)\sin(\theta_h) = 1,$$ 
where $\theta_h$ is the angle between the corresponding simple closed geodesics at the unique
point where they intersect (see [this article](https://arxiv.org/abs/math/0403041)).
Because of the $\sinh$ factors the angle between hyperbolic geodesics
tends to zero exponentially faster than for the comparable geodesics
on a euclidean torus. This is a manifestation of exponential divergence 
of Jacobi fields.

From this data, that is the angle $\theta_h$, we can construct a  comparison norm 
$$\| x v_0 + y v_1 \|_e^2 := x^2\|v_0\|^2 +2xy \|v_0\|^\|v_1\|\cos(\theta_h) +  y^2 \|v_1\|^2.$$

---

**Theorem [CAT+]** 
The restrictions of the stable norm and the comparison norms to the the positive cone
$$\{ x v_0 + y v_1 , \, x,y \in \mathbb{R}^+ \}.$$
satisfy 

$$\| v \|_e \leq \| v \|_s \leq \| v \|_1.$$

---

This follows from:
- an inductive enumeration of primitive homology classes (with positive coefficients)
which is really due to [Farey](https://en.wikipedia.org/wiki/Farey_sequence).
- [Toponogov's Theorem](https://en.m.wikipedia.org/wiki/Toponogov%27s_theorem#:~:text=It%20is%20one%20of%20a,a%20region%20of%20low%20curvature.)

The latter was used extensively by Gromov in his work on $\delta$-hyperbolicity 
but [this](https://www2.math.upenn.edu/~wziller/math660/TopogonovTheorem-Myer.pdf) gives an adequate exposittion.

The first step in the induction is when we have a  pair of triangles with side lengths
$\|v_0\|/2,\|v_1\|/2$ which meet at an angle $\theta$.
- one in euclidean space 
- the other in hyperbolic space
Topongov says that the other edge is longer in hyperbolic space than in euclidean space.

The reason why I divide by 2 is explained in [this article](https://arxiv.org/abs/math/0403041).



