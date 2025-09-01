## Brahmagupta–Fibonacci identity

The Brahmagupta identity states that the product of two sums of two
squares is again a sum of two squares. It can be expressed as:
$$ (a^2+b^2)(c^2+d^2) = (ac+ bd)^2 + (ad-bc)^2$$
The "square root" of this identity can be expressed   in terms of moduli of complex numbers as: 
$$(ai+b)(-ci+d) = (ac+bd) + (ad-bc)i.$$
It is amusing to note that the 2 dimensional Cauchy-Schwarz inequality is a corollary:

$$\begin{array}{lll}
 \|(a,b)\|^2\|(c,d)\|^2 
&=& (a^2+b^2)(c^2+d^2) \\
&\geq& (ac+ bd)^2  \\
&=& |(a,b)\cdot(c,d)|^2
\end{array}
$$

There is also the amusing identity:
$$\frac{ai+b}{ci+d} = \frac{(ac+bd) + (ad-bc)i}{c^2+d^2}.$$


### Gauss  composition of binary quadratic forms

The identity
$$ (a^2+b^2)(c^2+d^2) = (ac+ bd)^2 + (ad-bc)^2$$
is a special case of the composition law discovered by Gauss for binary quadratic forms: it says that the square of the form $x^2+y^2$ is the form itself. 
In fact Brahmagupta discovered the more general identity:
$$ (a^2+nb^2)(c^2+nd^2) = (ac+ nbd)^2 + n(ad-bc)^2$$


### Ptolemy's identity

The Brahmagupta identity is a special case of  Ptolemy's identity

Let $(a,b), (c,d)$ be a pair of non-collinear points in the plane.

$$ \begin{pmatrix} a & -b \\ b & a  \end{pmatrix}
\begin{pmatrix}c & d\\ -d & c\end{pmatrix}
=\begin{pmatrix} ac+bd & ad-bc \\ -ad+bc & ac + bd
\end{pmatrix}$$

<!-- $$\begin{vmatrix} a & -b \\ b & a  \end{vmatrix} -->
<!-- \begin{vmatrix}c & d\\ -d & c\end{vmatrix} -->
<!-- =\begin{vmatrix} ac+bd & ad-bc \\ -ad+bc & ac + bd -->
<!-- \end{vmatrix}$$ -->

And we compute determinants to obtain the identity.
In fact the quantities $ac+bd$ and $ad-bc$ are also determinants of
2x2 matrices:
$$ ad-bc = \begin{vmatrix} a & b \\ c & d \end{vmatrix}, \quad ac+bd
= \begin{vmatrix} a & -b \\ d & c \end{vmatrix}.$$

So that in terms of determinants, we have the identity:
$$\begin{vmatrix} a & -b \\ b & a  \end{vmatrix}
\begin{vmatrix}c & d\\ -d & c\end{vmatrix}
=
\begin{vmatrix} a & b \\ c & d \end{vmatrix}^2
+ 
 \begin{vmatrix} a & -b \\ d & c \end{vmatrix}^2.$$

## Spinnors

Following Matthews we define a \textit{spinnor} 
$(a,b)\in \mathbb{C}^2$
and we regard the latter as a symplectic vector space with the symplectic form
$$\{(a,b), (c,d)\} = (a,b)\wedge (c,d)= ad - bc.$$

We will only be interested in the subspace of real non null spinnors which we denote by $\mathbb{R}^2_*$.

Given 3 spinnors $u,v,w\in \mathbb{R}^2_*$, one has
a **Jacobi identity** for the symplectic form:
$$\{v,w\}u + \{w,u\}v + \{u,v\}w = 0,$$
and it follows that
$$ \{v^+,w\}\{u,v^-\} + \{w,u\}\{v^+,v^-\} + \{u,v^+\}\{w,v^-\} = 0 $$
for any quadruple of spinnor $v^\pm, w^\pm\in \mathbb{R}^2_*$.
This latter identity is a version of  the \textit{Ptolemy
identity}.

$$ \{v^+,w^+\}\{w^-,v^-\}+ \{w^-,v^+\}\{w^+,v^-\} 
= \{w^+,w^-\}\{v^+,v^-\}$$ 

To any such quadruple of spinnors we can associate an ideal
quadrilateral in the Poincaré disk: this is just the convex hull of
the four points on the projective line $\mathbb{RP}^1$ corresponding
to the obtained from the spinnors by the map
$$\mathbb{R}^2_* \to \mathbb{RP}^1, \quad (a,b) \mapsto [a:b].$$
We may suppose that after possibly changing labels
$v^+,w^+,v^-,w^-$ are in the correct cyclic order (see figure).

We say that an ideal quadrilateral is an ideal parallologram if
opposite sides have the same lambda length, that is, if the
spinnors $v^+, v^-$ and $w^+, w^-$ satisfy
$$|\{v^\pm,w^\pm\}| = |\{v^\mp,w^\mp\}|.$$


For any ideal parallogram, we have the following identity:
$$X^2 + Y^2 = Z_+ Z_-$$
This is
one of the two Vieta identities for the quadratic polynomial:
$$Z^2 - (kXY)Z + X^2 + Y^2 = 0$$
where $Z_+$ and $Z_-$ are the two roots of the polynomial
and $k$ is a constant.
The other Vieta identity is:
$$Z_+ + Z_- = kXY.$$

![](./ptolemy_rectangles.png)


---

## Quadratic forms

The quadratic forms over $\mathbb{Z}$
of a given discriminant $D$ form a group under the
composition law discovered by Gauss. The identity element
is 

- if $D\equiv 0 \mod 4$ the class of the form 
$$x^2 + \frac{D}{4}y^2$$

- if $D\equiv 1 \mod 4$  the class of the form 
$$x^2 + xy + \frac{1-D}{4}y^2$$ 


The inverse of the class of the form $ax^2 + bxy + cy^2$ is the
class of the form $ax^2 - bxy + cy^2$.

The composition law can be described in terms of
the bilinear matrix:
$$B = \begin{pmatrix} 2a & b \\ b & 2c \end{pmatrix}.$$
The composition of the forms $F(x,y) = (x,y)B(x,y)^T$ and
$F'(x,y) = (x,y)B'(x,y)^T$ is the form
$F''(x,y) = (x,y)B''(x,y)^T$ where
$$B'' = \frac{1}{g} \begin{pmatrix} 2aa' & ab' + ba' \\ ab' + ba' &
2cc' \end{pmatrix}$$



---

## Euler's four-square identity

There is a corresponding identity for sums of four squares, known as
Euler's four-square identity:


$$
\begin{array}{lll}
&& (a^2+b^2+c^2+d^2)(p^2+q^2+r^2+s^2)\\
&=& (ap+bq+cr+ds)^2
+(aq-bp-ecs+edr)^2 \\
&+&(ar+ebs-cp-edq)^2
+(as-ebr+ecq-dp)^2
\end{array}
$$
where e=1 or e=-1 .

This identity can also be expressed in terms of moduli of
quaternions:
$$|(a+bi+cj+dk)(p+qi+rj+sk)|^2 = |(ap+bq+cr+ds) + (aq-bp-ecs+edr)i +
(ar+ebs-cp-edq)j + (as-ebr+ecq-dp)k|^2.$$


[four square identity](https://en.wikipedia.org/wiki/Euler%27s_four-square_identity)
[cut the
knot](https://www.cut-the-knot.org/m/Algebra/BrahmaguptaFibonacci.shtml)


https://arxiv.org/pdf/1905.10704

Continued Fractions and Factoring
Michele Elia
Legendre found that the continued fraction expansion of \sqrt N having odd period leads directly to an explicit representation of N as the sum of two squares. Similarly, it is shown here that the continued fraction expansion of \sqrt N having even period directly produces a factor of a composite N. Shanks' infrastructural method is then revisited, and some consequences of its application to factorization by means of the continued fraction expansion of \sqrt N are derived.
https://arxiv.org/abs/1706.05919

Rational Right Triangles of a Given Area
Stephanie Chan
Starting from any given rational-sided, right triangle, for example the -triangle with area , we use Euclidean geometry to show that there are infinitely many other rational-sided, right triangles of the same area. We show further that the set of all such triangles of a given area is finitely generated under our geometric construction. Such areas are known as "congruent numbers" and have a rich history in which all the results in this article have been proved and far more. Yet, as far as we can tell, this seems to be the first exploration using this kind of geometric technique.
