A partition-theoretic proof of Fermat’s Two Squares Theorem
Author links open overlay panelA. David Christopher


Fermat’s Two Squares Theorem is the following: 

**If $p = 1 \mod 4$ is prime, then $p$
 is a sum of two squares.**

This statement was announced by Fermat in 1640, but he supplied no proof. The first proof was found by Euler after much effort and is based on infinite descent (see  [3], [4]). Subsequently, Gauss  [6] and Dedekind  [9] provided separate proofs. Simplifying an earlier short proof due to Heath-Brown  [7], Zagier  [10] presented a one-sentence proof of Fermat’s assertion. A detailed description of Heath-Brown Zagier proof can be found in  [2]. Proofs due to Ewell  [5] and Hirschhorn  [8] are the consequences of Jacobi’s Triple Product Identity; indeed, Hirschhorn proved Jacobi’s Two-Square Theorem from which Fermat’s Two Squares Theorem follows immediately.

Michael D. Hirschhorn, A simple proof of Jacobi’s two-square theorem, Amer. Math. Monthly 92 (1985), 579-580.


One of Jacobi's theorems states that the number of representations of a positive integer n as a sum of two squares of integers equals
$$4(d_1(n)−d_3(n)),$$
where the function $d_i$ counts the number of positive integer divisors congruent to $i \mod 4$ of n.

[source](https://mathoverflow.net/questions/242820/jacobis-theorem-on-sums-of-two-squares-reference-request)

Dolan's version of the proof is [probably the most elegant](https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/10538-a-very-simple-proof-of-the-twosquares-theorem/D0CB1CB39CBA0E98905401EA21DCB743)

---

Elsholtz C.A
  \textit{Combinatorial Approach to Sums of Two Squares and Related   Problems.}
   In: Chudnovsky D., Chudnovsky G. (eds) Additive Number Theory. Sp   ringer, New York, NY.
   (2010)
Wells, D.: Are these the most beautiful? Math. Intelligencer 12 (1990), no. 3, 37–41.
includes Theorem 2 in a list of the [10 most beautiful results in mathematics.](https://www.matmedia.it/wp-content/uploads/2020/01/1990-wells_beauty.pdf)


In his “Apology” Hardy [18] writes: 

**“Another famous and beautiful theorem is
Fermat’s ‘two square’ theorem... All the primes of the first class” [i.e. 1 mod 4] ...
“can be expressed as the sum of two integral squares... This is Fermat’s theorem,
which is ranked, very justly, as one of the finest of arithmetic. Unfortunately, there
is no proof within the comprehension of anybody but a fairly expert mathematician.”**

In this paper we discuss quite elementary proofs and it would be interesting to
know if Hardy would also have written this about the types of proof (and its simplifications), discussed in sections 1.2, 1.3 and 1.6.2.
The history of the theorems above is described in detail in Dickson [8] (volume 2,
chapter VI), and also in Edwards [10]. Already Diophant discussed representations
of integers as a sum of two squares, and, by slightly altering the text, Jacobi interpreted Diophant’s writing in such a way that Diophant possibly essentially knew and
was able to prove: if a square-free number n is a sum of two squares, then neither n
nor any factor of n is of the form 4k −1, (see [8], page 236).
The first correct statement of the necessary and sufficient conditions for writing
an integer as a sum of two integer squares, without a proof, might have been by
Albert Girard. The theorem is also often attributed to Fermat, who wrote he had a
proof. His proof is not known to us, even though in this case it is believed he had
the right methods to prove the theorem indeed. Euler eventually gave the first proof
that has survived.


There is a multitude of proofs of Theorem 2. Most of these use quite essentially
the fact that for a prime 
$p = 1 \mod 4$ there is a solution of 
$x  = −1 \mod p.$ 

This
follows for example from 
- Wilson's theorem $x = \frac{p−1}{ 2}!$ 
- or $x = g^{p−1/ 4}$, where g is a generating element of
the group $(Z/pZ)^*$  or a nonresidue modulo p. 


However, checking the details in
this calculation from first principles is already half of the proof.
The methods involved in these various proofs include e.g. 
- congruence computations
- Minkowski’s theorem
- the pigeon hole principle
- properties of Gaussian integers
- continued fractions and the like. 

The book by Hardy and Wright [19] gives
several different proofs. For other proofs see also [33], [40], [6].
A very different second type of proof goes back to Liouville. In a series of eighteen papers Liouville describes a quite general method, a special case of which gives
Theorem 2. Liouville’s work is described in the books by Bachmann [3], Dickson
[8], Uspensky and Heaslet [34], Venkov [36], and Nathanson [29].

* This special case was considerably simplified by Heath-Brown [20]. 
* Zagier [41]
reformulated Heath-Brown’s proof to write it in one sentence, however leaving elementary calculations to the reader.


This proof has generated a considerable literature explaining the proof for teaching purposes [35], [39], [12], [31], [5] or extending it to related results: [4], [13],
[14], [16], [21], [22], [23], [32]. The collection of beautiful proofs “Proofs from the
BOOK” by Aigner and Ziegler [1] explains in its first edition Zagier’s version of the
proof, but changed to Heath-Brown’s version for the 2nd edition.


A key ingredient is an ingenious choice of a set which allows a partition into orbits of length 1 or 2. In this way a simple parity check guarantees the decomposition
into two squares. The reader who is familiar with Liouville’s method will appreciate
the simplifications made by Heath-Brown and Zagier. Still, the proof is quite mysterious. We make an attempt to demystify the proof, i.e. explain how the details can
be motivated.
In addition to the study of this second type of proof we apply the idea of orbits
of length 1 or 2 to a proof based on lattice points, which is more in the spirit of the
first type of proof. After reviewing the history of these, i.e. discuss contributions by
Lucas, Grace and others we present in section 1.6 a quite short version of the proof,
which admittedly also requires some routine checking, as is the case with the proofs
by Zagier and Heath-Brown.

---
Guillaume Dubach, Fabian Muehlboeck
  [Formal verification of Zagier's one-sentence proof ](https://arxiv.org/abs/2103.11389)

[GitHub Repo](https://github.com/gdubach/Zagier_project)


Zagier’s proof relies on the basic fact that 

**an involution f on a finite set S is such that
the number of fixed points of f and the cardinality |S| have the same parity.**

This principle is
used twice, in complementary ways: after defining an appropriate set S, a first invo
lution is
invoked to justify that |S| is odd; this implies that another involution on S has at least one
fixed point; and any such fixed point then yields two integers a and b solutions of the problem.
The second involution is a very natural one, whereas the first involution appears at first sight
to be extremely involved. The trick, in order to turn this argument into a ‘one-sentence proof’,
is to only state the definitions and major steps as one long sentence, leaving all details and
especially all ancillary (but logically necessary) verification steps to the reader. This condensed
writing style and the mysterious origin of the first involution undoubtedly endowed this proof
with rare appeal when it first appeared, and still does some thirty years later. In particular, it
prompted several generalizations and applications to other results of the same kind, a review
of which is given in [6]; our method applies to these with very few changes. 

To illustrate this,
we provide a formal proof of the following statement, following an argument first published by
Jackson [11], which was found independently by Elsholtz [5] and Generalov [7].
