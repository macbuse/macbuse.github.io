## Dan Martin


**this is naif as the valence of vertices changes**
it depends on Pisano periods which divide $p-1$
if $p$ is 1 mod 4.


$\chi(S) = V - E + F$

$6n\chi(S) = 6(nV) - 3n(2E) + 2(3F) = (6-3n+2)T$

- $n = p-1,$
$6\chi(S) =  (6-3(p-1)+2)V= (3p+5)V$

$T = 3F = 2E = nV$

$3F = nV$

## Pisano periods 

Here $n$ is the period of $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ modulo $p$

| Case | Condition | Behavior of $\pi(p)$ |
| :--- | :--- | :--- |
| Small Prime | $p = 2$ | $\pi(2) = 3$ |
| Small Prime | $p = 5$ | $\pi(5) = 20$ |
| Quadratic Residue | $p \equiv 1, 4 \pmod 5$ | $\pi(p)$ divides $p - 1$ |
| Quadratic Non-residue | $p \equiv 2, 3 \pmod 5$ | $\pi(p)$ divides $2(p + 1)$ |

Why does this happen?

- If $\left(\frac{5}{p}\right) = 1$: $\sqrt{5}$ exists in $\mathbb{Z}_p$. The eigenvalues are in the field, and by Fermat's Little Theorem, $\lambda^{p-1} \equiv 1 \pmod p$. Thus, the period divides $p-1$.
- If $\left(\frac{5}{p}\right) = -1$: $\sqrt{5}$ does not exist in $\mathbb{Z}_p$. We must work in the extension field $\mathbb{F}_{p^2}$. In this case, it can be shown that $\lambda^{p+1}$ results in a scalar matrix, and $\lambda^{2(p+1)} \equiv 1$, meaning the period divides $2(p+1)$.


### Reduction over $\mathbb{Z}$

Since there are 4 
non trivial components over $\mathbb{R}$ then there are at most 2
over $\mathbb{F}_p$.

This pre supposes surjectivity of the reduction map, which may not
always be the case.

## Pisano periods




#### Connectivity of components

So shouldn't it just be a question of showing $(\pm 3, \pm 3, 3)$ are in the same component mod $p$?


For example, for $p=5$, the reduction map is not
surjective, and we have only 2 components instead of 4.



---



- Connectivity of Orbits

- Generalizations of continued fractions
[here](https://arxiv.org/pdf/1908.00121)

- Silverman's survey [Notices](https://www.ams.org/journals/notices/202605/rnoti-p367.pdf)

- [More divisibility](https://arxiv.org/pdf/2509.02187)
- Is there a get of jail clause here or is parabolic special


- spectrum of rotations
    - starting with Pisano periods, we can ask about the
    distribution of these periods as $p$ varies. Are there
    infinitely many primes for which $\pi(p)$ takes on a
    particular value? How does $\pi(p)$ grow on average as $p$
    increases? These questions connect to deeper topics in number
    theory and the distribution of primes.


## Farey symbol

- https://gap-packages.github.io/congruence/doc/chap4_mj.html
- [Cheng Mong](https://arxiv.org/pdf/1509.04796)
- [Optimal](https://arxiv.org/pdf/2601.01324)
- [for bianchi groups](https://arxiv.org/abs/2509.02269)

A **Farey symbol** is a compact, elegant way to encode the geometry and algebraic structure of a **subgroup of the modular group** $\Gamma = PSL_2(\mathbb{Z})$. 

While a subgroup can be defined by its generators or its fundamental domain, the Farey symbol provides a "blueprint" for constructing that domain and understanding how its edges are glued together.

---

### 1. The Structure of a Farey Symbol
A Farey symbol consists of two main parts: a **generalized Farey sequence** and a string of **labels** (glueing types).

#### The Farey Sequence
The symbol starts with a finite sequence of rational numbers (including infinity) in increasing order:
$$\{-\infty, x_1, x_2, \dots, x_n, \infty\}$$
These represent the **cusps** of the subgroup's fundamental domain on the boundary of the upper half-plane $\mathbb{H}$. Every adjacent pair of fractions $\frac{a}{b}, \frac{c}{d}$ in this sequence must satisfy the **Farey condition**:
$$|ad - bc| = 1$$
This ensures that the hyperbolic geodesic (semicircle) connecting them is an edge of the modular tessellation.



#### The Labels (Glueing Rules)
Below the gaps between these numbers, we assign labels that tell us how the edges are identified:
* **Even ($2$):** Indicates an elliptic element of order 2 (a $180^\circ$ rotation) fixes the midpoint of this edge.
* **Odd ($3$):** Indicates an elliptic element of order 3. These edges usually come in pairs.
* **Integers ($1, 2, 3 \dots$):** Matching integers indicate that the two corresponding edges are identified (glued) by a parabolic or hyperbolic element of the subgroup.

---

### 2. An Example: $\Gamma_0(2)$
The congruence subgroup $\Gamma_0(2)$ (matrices where the bottom-left entry is even) has a very simple Farey symbol:
$$\{- \infty, 0, 1, \infty \}$$
$$\text{labels: } \quad 1 \quad \quad 1$$

* **Interpretation:** The edges are the geodesics $(-\infty, 0)$, $(0, 1)$, and $(1, \infty)$.
* **The Labels:** The "1" under the first and second gaps means those two edges are glued together. This identifies the cusp at $0$ with the cusp at $\infty$.

---

### 3. Why is it useful?
The Farey symbol is essentially the "DNA" of the subgroup. From it, you can instantly determine:
1.  **Generators:** There is an algorithm (by Kulkarni) to extract a minimal set of independent generators for the subgroup directly from the symbol.
2.  **Fundamental Domain:** It gives you the vertices of the hyperbolic polygon that tiles the upper half-plane.
3.  **Genus and Index:** By counting the labels and cusp types, you can calculate the Euler characteristic and the genus of the resulting Riemann surface ($X = \mathbb{H}/\Gamma$).



---

### 4. Connection to Continued Fractions
Farey symbols are deeply linked to **continued fractions**. The process of moving from one cusp to the next in the sequence is equivalent to performing a sequence of modular transformations, much like how the Euclidean algorithm navigates the rational numbers.

Would you like to see how to calculate the generators for a specific subgroup using its Farey symbol?

##  Nicola Harifa 

[here](./NicolaHarif_HorospheresandImaginaryQuadraticFieldsofHeegnerNumbers.pdf)


Connectivity of horoshere graphs

Paulin Hersonsky

Bianchi groups and Hurwitz constants

##

https://arxiv.org/pdf/2603.04096v1
https://arxiv.org/pdf/2507.06900
https://arxiv.org/pdf/2503.21872
https://arxiv.org/pdf/2206.12072
https://arxiv.org/pdf/1602.01011

https://arxiv.org/pdf/2410.21619


TROPICALIZATION AND CLUSTER ASYMPTOTIC PHENOMENON OF

GENERALIZED MARKOV EQUATIONS
ZHICHAO CHEN AND ZELIN JIA


[Musiker](https://arxiv.org/pdf/2503.21872)

[Maloni 4-holed sphere](https://arxiv.org/pdf/1304.5770)

[Super Ptolemy](https://arxiv.org/abs/2206.12072)
https://arxiv.org/pdf/2206.12072


CLUSTER ALGEBRAIC INTERPRETATION OF GENERALIZED
MARKOV NUMBERS AND THEIR MATRIXIZATIONS
ESTHER BANAIAN AND YASUAKI GYODA

[here](https://arxiv.org/pdf/2507.06900)

## Fibonacci and the cluster algebra 

of the annulus.

Are there relations between Fibonacci numbers that are obvious from the cluster algebra perspective but not from the combinatorial one?

What about Pell numbers?


$F_{2n+1} = F_n^2 + F_{n+1}^2$
