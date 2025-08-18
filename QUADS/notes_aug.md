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

