# Odds and sods

[Stange circle packings](https://math.colorado.edu/~kstange/papers/Stange-medshort-exp.pdf)

- [osvienko dual numbers](https://arxiv.org/pdf/2111.02553.pdf)
- [def dual numbers](https://en.wikipedia.org/wiki/Dual_number)
- [clifford algebras and discreteness](https://arxiv.org/pdf/1808.06756.pdf)
- [mobius transforms and cliff alg.](https://www.emis.de/journals/CMUC/pdf/cmuc1002/lawson.pdf)
- [Bhargava higher composition laws](https://upcommons.upc.edu/server/api/core/bitstreams/cbe62df4-d24b-420a-9797-89c7045018b5/content)


- [osvienko Farey boat](https://arxiv.org/pdf/1811.01229.pdf)
- [mcmullen low geodesics](https://people.math.harvard.edu/~ctm/papers/home/text/papers/cf/cf.pdf)
	- [Wilson Limit points Lagrange Spectrum](http://www.numdam.org/article/BSMF_1980__108__137_0.pdf)
	- [Gbur Limit points again](https://link.springer.com/article/10.1007/BF01579595)
	- [more recent](https://arxiv.org/abs/1911.06170)
	- [mercat on mcmulle](http://www.numdam.org/item/10.5802/jtnb.829.pdf)

- [osvienko Ramanujan cubic](https://arxiv.org/pdf/2110.01282.pdf)

This looks like Markoff but it is
$$X^3 + Y^3 + Z^3 - 3XYZ$$

- [Schafer Forms and composition](https://core.ac.uk/download/pdf/82584475.pdf)


---

ON THE GREATEST PRIME FACTOR AND UNIFORM
EQUIDISTRIBUTION OF QUADRATIC POLYNOMIALS
LASSE GRIMMELT AND JORI MERIKOSKI

[paper](https://arxiv.org/pdf/2505.00493)


### Near-square primes
Landau's fourth problem asked whether there are infinitely many primes which are of the form 
$$p = n^2 + 1$$
(The list of known primes of this form is A002496.) The existence of infinitely many such primes would follow as a consequence of other number-theoretic conjectures such as the Bunyakovsky conjecture and Bateman–Horn conjecture.

One example of near-square primes are Fermat primes. Henryk Iwaniec showed that there are infinitely many numbers of the form 
$n^{2}+1$ with at most two prime factors.



---

so what if we thought of $b^2 - 4ac$ as a discriminant of a quadratic form?

And so if $b = 2n$  then 
$$\Delta = b^2 - 4ac = -4 \Leftrightarrow n^2 + 1 = ac$$


So  what if we look at the fixed points of
$$\begin{pmatrix}n & -c \\ a & -n\end{pmatrix}$$
which are just the solutions $z_\pm$ of
$$az^2 - 2nz + c = 0.$$
As usual we write:
$$z_\pm = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{2n \pm 2i}{2a}
= \frac{n \pm i}{a}.$$

According to Penner in his discussion of Gauss composition of
quadratic forms the quantity 
$$\frac{n}{2}= \frac{b}{\sqrt{-\Delta}}$$ 
is geometric quantity namely the hyperbolic distance between $z_+$ and the geodesic connecting $0$ and $\infty$ in the upper half plane model of hyperbolic space.

So now Landau's conjecture is equivalent to the fact that there are an infinity of curves $\arg(z) = \tan^{-1}(1/n)$ each of which contains a single point of the orbit of $i$ under the action of the group of matrices with integer entries and determinant $1$
ie $SL(2, \mathbb{Z})$.


The composition of the two involutions is a loxodromic
transformation with matrix

$$\begin{pmatrix}n & -c \\ a & -n\end{pmatrix}
\begin{pmatrix}-n & -c \\ a & n\end{pmatrix} = 
\begin{pmatrix}-n^2 -ca & -2cn  \\ -2an & -n^2 -ca\end{pmatrix}$$
so the trace is 
$$-2(n^2 + ac) = -2(2n^2 +1)= -((2n)^2 + 2)$$

On the other hand the composition with
the elliptic involution has matrix:
$$
\begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}
\begin{pmatrix}n & -c \\ a & -n\end{pmatrix}
= \begin{pmatrix} -a & n \\ n & -c\end{pmatrix}$$
and note that this is a symmetric matrix with trace 
$-(a+c)$.

---

## Congruences

If a prime $p$ divides $n^2 + 1$ then
$$n^2 \equiv -1 \mod p$$
and so $p$ is either $2$ or congruent to $1$ modulo $4$.

For example $5$ divides $2^2 + 1 = 5$ and $13$ divides $5^2 + 1 = 26$. Further
$$(5k + 2)^2 + 1 = 25k^2 + 20k + 5 = 5(5k^2 + 4k + 1)$$
so one could sieve out all numbers of this form.

The discriminant of $5k^2 + 4k + 1$
is $16 - 20 = -4$ so this is another quadratic form of discriminant $-4$ and the roots of $5k^2 + 4k + 1 = 0$
are
$$\frac{-2 \pm i }{5}$$
So in theory if Bunyakovsky's conjecture is true for this form then there are infinitely many primes of the form $5k^2 + 4k + 1$ and
the form $n^2 + 1$ represents $5q$ for infinitely many primes $q$.

##

There are essentially four types of  curves in the hyperbolic plane defined by a fixed distance from a given object

- geodesics that is the set of points at a fixed distance from apair of distinct points
- spheres that is the set of points at a fixed distance from a point
- horocycles that is the set of points at a fixed distance from an
ideal point
- equidistant curves that is the set of points at a fixed distance
from a geodesic

Horocycles are particular in that they are the limit of smilies of pheres  and of equidistant curves as the center or the geodesic respectively tends to an ideal point.






