# Niven


These theorems are fascinating 
because they assert the existence of a solution
if a certain simple arithmetic condition is met.

| Niven's Theorem I |
| --- |
| Every Gaussian integer that is not divisible by $(1 + i)^3$ is a sum of 2 squares of Gaussian integers. |

- Ivan Niven,
Integers of Quadratic Fields as Sums of Squares,
Transactions of the American Mathematical Society,
Vol. 48, No. 3 (Nov., 1940), pp. 405-417 (13 pages)


There are a lot of proofs of this theorem
which are elementary,
it is basically a consequence of the following identity:
$$ x = \left(\frac{x + 1}{2}\right)^2 + \left(\frac{x - 1}{2i}\right)^2$$
but Niven's uses Mordell's theorem.


- L. J. Mordell, On the representation of a binary quadratic form as a sum of squares of linear forms, Math. Z. 35 (1932), no. 1, 1–15.
- L. J. Mordell, The Representation of a Gaussian integer as a Sum of two Squares, Math.
Mag. 40 (1967), no. 4, 209.


This only really works for Gaussian integers:

- K. S. Williams, On a theorem of Niven, Canad. Math. Bull. 10 (1967), 573–578.



1. [Smith](https://bpb-us-w2.wpmucdn.com/sites.baylor.edu/dist/6/47/files/2015/01/smithfv-1a6rchp.pdf)
1. [Delorme](https://www.emis.de/journals/INTEGERS/papers/p3/p3.pdf)


---

### Mordell

A quadratic form
$$Q = a x^2 + 2h xy + c y^2$$
is a sum of squares iff
- discriminant is a square $d^2$
- all prime factors of the pgcd (a, h, c) are congruent to 1 mod 4

Obviously the matrix of the quadratic form is
$$\begin{pmatrix} a & h \\ h & c \end{pmatrix}$$

Calculating the discriminant gives:
$$ac = h^2 + d^2= (h + id)(h - id)= |h \pm id|^2$$
and, in some sense, we want to take the square root of this.

If
$a = |\alpha_1 + i \alpha_2|^2$
then,
after possibly changing the sign of $h$ and $d$,
we have $c = |\gamma_1 + i \gamma_2|^2$
where 
$$(\alpha_1 + i \alpha_2)(\gamma_1 + i \gamma_2) = h + id.$$
<!-- $$\gamma_1 + i \gamma_2 = \frac{h + id}{\alpha_1 + i \alpha_2}.$$ -->

So that 
$$\begin{pmatrix} a & h \\ h & c \end{pmatrix} 
= \begin{pmatrix}
\alpha_1 & \alpha_2 \\ \gamma_1 & \gamma_2 \end{pmatrix}
\begin{pmatrix}
\alpha_1 & \gamma_1 \\ \alpha_2 & \gamma_2 \end{pmatrix}
$$

This is interesting when $a$ can be written as a sum of squares
in more than one way.
For example
$$65 = 5\cdot13 = 1^2 + 8^2 = 4^2 + 7^2.$$


**Can this be proved by reduction?**

**Question 1**:
Suppose $Q$ is a quadratic form
such that $Q(p,q)$ is a sum of squares
for all pairs of coprime integers $p, q$


Is $Q$ a sum of squares à la Mordell?

*I've looked at this a bit and it seems that
it could be true but I don't see how to prove it
using Conway's topograph for example.*

With respect to the triple $10,13,17$ each integer 
- is a sum of squares 
- a value of the form $10x^2 -6 xy + 13y^2$ for the pairs $(x,y) = (1,0), (0,1), (1,1)$ respectively

Using the sum of squares decompositions for $10$ and $13$ 
one discovers that
$$10x^2 -6 xy + 13y^2 = (3x - 2y)^2 + (x + 3y)^2$$


This is a question of lifting a solution

$$A(x,y,z) = 2(xy + yz + zx) - (x^2 + y^2 + z^2) $$

- $A(x,y,z) > 0 \Leftrightarrow x, y, z$ are squares of the sides of a triangle with area squared equal to $A(x,y,z)$

---

**Question 2**:
Can this be made effective
ie is a finite set of values of $p, q$ enough?

**Question 3**:
What is the correct generalization of Mordell's theorem
to other quadratic fields?

---



### Lagrange's four-square theorem


Every natural number is a sum of 4 squares


**Lemma (reduction)**:
If $m$ and $n$ are sums of 4 squares then so is $mn$

---
**Lemma**:

Let $p$ be a prime
then there are integers $x, y$ such that
$$x^2 + y^2 \equiv -1 \mod p$$

---


Can you show that all the squares (say) are Zaremba?

**Reciprocity obstructions in semigroup orbits in SL(2, Z)**
James Rickards, Katherine E. Stange

[arxiv](https://arxiv.org/abs/2401.01860)

Shows that there are semigroups for which every odd integer is
admissible but no square is represented.


Techniques manage powers of $2$ and $3$ 
and some geometric sequences but nothing 
that has polynomial growth.



**Zaremba's Conjecture for Geometric Sequences:** An Algorithm
Elias Dubno

Even though Zaremba's conjecture remains open, Bourgain and Kontorovich solved the problem for a full density subset. Nevertheless, there are only a handful of explicit sequences known to satisfy the strong version of the conjecture, all of which were obtained using essentially the same algorithm. In this note, we provide a refined algorithm using the folding lemma for continued fractions, which both generalizes and improves on the old one. As a result, we uncover new examples that fulfill the strong version of Zaremba's conjecture.

[arxiv](https://arxiv.org/abs/2310.11279)

Dyadic Fractions with Small Partial Quotients.
Harald Niederreiter
Monatshefte für Mathematik (1986)
Volume: 101, page 309-316

Quantitative generalizations of Niederreiter's result concerning continuants
Igor D. Kan, Natalia A. Krotkova


[arxiv](https://arxiv.org/abs/1109.1633)


The big problem from a
geometric point of view is that any modification to a path results
in a measurable increase in length $\delta$ say but this translates
to a multiplicative increase $e^\delta$ in the $\lambda$-length ie
the denominator.



\begin{theorem}[Folding Lemma]\label{thm:cfmatrices}
    Let $\frac{b}{d}=[0,a_1,a_2,\dots,a_n]$ be a reduced fraction, and let $z\geq1$ be a positive integer. 
Then the fraction 
$$\frac{b}{d}+\frac{(-1)^n}{zd^2}=\frac{zbd+(-1)^n}{zd^2}$$ 
is reduced and its continued fraction expansion is given by
$$\frac{zbd+(-1)^n}{zd^2} = [0,  a_1,a_2,\dots,a_{n-1},a_n,z-1,1,a_n-1,a_{n-1},a_{n-2},\dots,a_1],$$
where we use the convention that

$[\dots,a,0,a',\dots]=[\dots,a+a',\dots]$.

\end{theorem}


---

En fait je me dis que ce serait peut-être pas mal de faire un ou deux exos supplémentaires sur les intégrales impropres (à partir du 4.20, intégrales à paramètres, mais pas le 4.34, j’ai essayé d’en faire un sujet de partiel). Ou le 37 ? (Normes L1 et L2). Enfin il faut dire aussi que moi je n’ai pas traité le 17 car je l’ai donné en DM et personne ne l’a fait (tant pis pour eux…).

Je te joins quelques idées pour le sujet de CC. En as-tu d’autres ? 
Je pense que c’est trop dur pour eux mais je voudrais bien qu’il y ait des choses théoriques car la dernière fois ils ont tous essentiellement traité les questions calculatoires et presque toutes les notes étaient regroupées entre 7 et 10… Je vais essayer d’y réfléchir dans les jours qui viennent.
