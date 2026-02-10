<!-- toc -->

- second countability
- metrizability
- embedding theorems
- bump functions

---

# The Long Line, Second Countability

## 1. What is Second Countability?

A topological space is **second-countable** if its topology has a **countable base**.

To put it simply: you can describe every open set in the space using a "construction kit" that contains only a countable number of basic shapes. For example, the standard real line  is second-countable because every open interval can be built using intervals with rational endpoints, and the set of pairs of rational numbers  is countable.

**Why it matters:**

* **Metric Spaces:** For a metric space, being second-countable is equivalent to being **separable** (having a countable dense subset).
* **Embeddings:** Second-countable manifolds can be embedded into higher-dimensional Euclidean spaces.
* **Compactness:** It helps ensure that concepts like "compactness" and "sequential compactness" behave predictably.

---

## 2. The Long Line ($\mathbf{L}$)

The Long Line is a topological space that is "longer" than the real line $\mathbb{R}$. While the real line is built by placing unit intervals  side-by-side indexed by the integers, the Long Line is built by placing unit intervals side-by-side indexed by the **first uncountable ordinal**, .

### Key Properties:

* **Locally Euclidean:** If you zoom in on any point, it looks exactly like a piece of the standard real line. It is a 1-dimensional manifold.
* **Not Second-Countable:** Because there are uncountably many "units" glued together, you cannot describe its topology with a countable base.
* **Normal but not Metric:** It is a normal space, but because it isn't second-countable, it **cannot be metrized**. You can't define a standard distance  that works for the whole line.
* **Path Connected:** You can draw a continuous path between any two points.

---

## 3. Comparison: The Real Line vs. The Long Line

| Feature | Real Line () | Long Line () |
| --- | --- | --- |
| **Local Structure** | 1D Manifold | 1D Manifold |
| **Countability** | Second-Countable | **Not** Second-Countable |
| **Metrizability** | Metrizable | Not Metrizable |
| **Compactness** | Not Compact | Not Compact (but "Sequentially Compact") |
| **Size** | "Countably" long | "Uncountably" long |

---

## Why should you care?

The Long Line is the "Boogeyman" of topology. It warns mathematicians that **local properties** (looking like  at every point) do not always dictate **global properties** (being able to measure the whole thing with a ruler). It proves that you can have a space that is perfectly smooth and continuous, yet so vast that it breaks the fundamental rules of distance.

---

# Metrizability Theorems

## 1. The Urysohn Metrization Theorem
Urysohn's theorem provides a sufficient condition for a topological space to be metrizable. It is a "top-down" approach: if a space is small enough (second-countable) and separated enough (regular), it must be metrizable.

**Theorem:** Every second-countable, regular $T_2$ space is metrizable.

* **Regular ($T_3$):** For every closed set $F \subset X$ and point $x \notin F$, there exist disjoint open sets $U$ and $V$ such that $x \in U$ and $F \subset V$.
* **Second-countable:** The topology $\mathcal{T}$ has a countable base $\mathcal{B} = \{B_n\}_{n \in \mathbb{N}}$.



---

## 2. The Bing-Nagata-Smirnov Theorem
This theorem provides the necessary and sufficient (if and only if) conditions for metrizability, covering spaces that Urysohn's theorem might miss.

**Theorem:** A topological space $X$ is metrizable if and only if it is regular, Hausdorff, and has a $\sigma$-locally finite base.

* **$\sigma$-locally finite base:** A base $\mathcal{B}$ is $\sigma$-locally finite if $\mathcal{B} = \bigcup_{n \in \mathbb{N}} \mathcal{B}_n$, where each collection $\mathcal{B}_n$ is locally finite. 
* **Local Finiteness:** Each point $x \in X$ has a neighborhood $W$ such that the set $\{B \in \mathcal{B}_n : B \cap W \neq \emptyset\}$ is finite.

---

## 3. Why Metrizability Matters
In a metrizable space $(X, d)$, the topology behaves with a specific "rigidity" that general spaces lack:

* **Sequences:** A point $x$ is in the closure of $A$ if and only if there is a sequence $(x_n) \subseteq A$ such that $x_n \to x$. In non-metrizable spaces, this is not always true, requiring the use of nets $(x_\alpha)_{\alpha \in A}$.
* **Distance Function:** We can define a function $d: X \times X \to [0, \infty)$ that satisfies the triangle inequality:
    $$d(x, z) \leq d(x, y) + d(y, z)$$
* **Compactness:** In any metric space, **Compactness**, **Sequential Compactness**, and **Countable Compactness** are all equivalent.

---

## 4. Why the Long Line $L$ Fails
The Long Line is the quintessential example of a non-metrizable manifold.

* **Local Metrizability:** Every point $p \in L$ has a neighborhood $U$ such that $U \cong (0, 1)$. Since $(0, 1)$ is metrizable, $L$ is locally metrizable.
* **Global Failure:** The Long Line is constructed as $L = \omega_1 \times [0, 1)$ (where $\omega_1$ is the first uncountable ordinal). 
* **The Contradiction:** $L$ is sequentially compact but **not** compact. In a metrizable space, these two properties must coincide. Therefore, $L$ cannot be metrized.
* **Size:** $L$ is "

# Embedding Compact Manifolds into $\mathbb{R}^N$"


## 1. The Core Idea: Manifolds as Metric Spaces
By definition, a manifold $M$ is **locally Euclidean**. This means every point $p \in M$ has a neighborhood $U$ such that there exists a homeomorphism $\phi: U \to V$, where $V$ is an open subset of $\mathbb{R}^n$.

If a manifold is **compact**, several "niceness" properties converge:
* It is automatically **second-countable**.
* It is **Hausdorff** ($T_2$) and **normal** ($T_4$).
* Because it is second-countable and regular, the **Urysohn Metrization Theorem** tells us that every compact manifold is metrizable.

> **The takeaway:** Every compact manifold is a metric space, meaning there exists a metric $d: M \times M \to [0, \infty)$ that induces the manifold's topology.

---

## 2. Embedding into Euclidean Space $\mathbb{R}^N$
The most common metric space target is $\mathbb{R}^N$. The **Whitney Embedding Theorem** provides the upper bound for the dimension $N$ required to fit an $n$-dimensional manifold.

* **Weak Whitney Theorem:** Any smooth, compact $n$-dimensional manifold can be embedded in $\mathbb{R}^{2n+1}$.
* **Strong Whitney Theorem:** Any smooth, compact $n$-dimensional manifold can be embedded in $\mathbb{R}^{2n}$.

For example:
* The circle $S^1$ (where $n=1$) embeds into $\mathbb{R}^2$.
* The Klein Bottle (where $n=2$) cannot embed into $\mathbb{R}^3$ without self-intersection, but it embeds into $\mathbb{R}^4$.



---

## 3. The Mechanism: Partition of Unity
To construct a global embedding, we use a **partition of unity**. This allows us to "glue" local coordinate maps together.

1.  Cover $M$ with a finite collection of coordinate patches $\{U_i\}_{i=1}^k$ and homeomorphisms $\phi_i: U_i \to \mathbb{R}^n$.
2.  Define a set of smooth "bump functions" $\psi_i: M \to [0, 1]$ such that the support of $\psi_i$ is contained in $U_i$ and $\sum \psi_i(x) = 1$ for all $x \in M$.
3.  Construct the global map $f: M \to \mathbb{R}^{k(n+1)}$ by:
    $$f(x) = (\psi_1(x)\phi_1(x), \dots, \psi_k(x)\phi_k(x), \psi_1(x), \dots, \psi_k(x))$$

Since $M$ is compact and $f$ is a continuous injection into a Hausdorff space, $f$ is a **homeomorphism onto its image**.

---

## 4. Why the Long Line $L$ Fails
The Long Line is a $1$-dimensional manifold, but it cannot be embedded into any metric space $\mathbb{R}^N$.

* **Dimension vs. Size:** While $L$ is locally $1$-dimensional, it is not second-countable. 
* **The Euclidean Barrier:** Any subspace of $\mathbb{R}^N$ must be second-countable (because $\mathbb{R}^N$ has a countable base of rational balls). 
* Since $L$ is "too long" (its length is indexed by the first uncountable ordinal $\omega_1$), it cannot be contained within the countable structure of Euclidean space.

---

### Summary Table

| Manifold Type | Metrizable? | Embeddable in $\mathbb{R}^N$? |
| :--- | :--- | :--- |
| **Compact $n$-manifold** | Yes | Yes (in $\mathbb{R}^{2n}$) |
| **Non-compact $2^{nd}$ countable** | Yes | Yes (in $\mathbb{R}^{2n}$) |
| **Long Line** | No | No |


---

# Partition of unity with references

## 1. References in Michael Spivak
**Book:** *Calculus on Manifolds: A Modern Approach to Classical Theorems of Advanced Calculus*

In this text, Spivak introduces bump functions specifically to build a **Partition of Unity**, which he then uses to define integration on manifolds.

* **Theorem 3-11 (The Existence of Bump Functions):** Found in Chapter 3 (Integration). Spivak constructs a smooth function $f: \mathbb{R}^n \to \mathbb{R}$ such that $f(x) > 0$ for $|x| < a$ and $f(x) = 0$ for $|x| \geq a$.
* **Construction:** He starts with the classic non-analytic smooth function:
    $$ \lambda(x) = 
    \begin{cases} 
    e^{-1/x^2} & x > 0 \\ 
    0 & x \leq 0 
    \end{cases} $$
* **Partition of Unity:** This is covered in the subsequent pages of Chapter 3. He proves that for any open cover $\mathcal{O}$ of a closed rectangle $A$, there exist smooth functions $\phi_i$ subordinate to the cover such that $\sum \phi_i = 1$.

---

## 2. References in Guillemin & Pollack
**Book:** *Differential Topology* (Victor Guillemin and Alan Pollack)

Guillemin and Pollack (often referred to as G&P) use bump functions more explicitly for embeddings and the Whitney Embedding Theorem.

* **Chapter 1, Section 6 (Partition of Unity):** G&P introduce the "Bump Function" as a technical Lemma. 
* **The Lemma:** They prove that for any closed set $A$ and open set $U$ containing $A$ ($A \subset U$), there exists a smooth function $\rho$ such that $0 \leq \rho \leq 1$, where $\rho = 1$ on $A$ and $\text{support}(\rho) \subset U$.
* **Applications:** In the same section, they use these functions to:
    1.  Extend local maps $f: U \to \mathbb{R}^n$ to global maps.
    2.  Construct the embedding of a compact manifold $X$ into $\mathbb{R}^N$.

---

## 3. Comparison of Approach

| Feature | Spivak (*Calculus on Manifolds*) | Guillemin & Pollack |
| :--- | :--- | :--- |
| **Primary Goal** | Integration and Stokes' Theorem | Topology and Embeddings |
| **Construction** | Explicit formula using $e^{-1/x}$ | More axiomatic/lemma-based |
| **Locality** | Usually defined on rectangles | Defined on arbitrary closed sets $A$ |


---

## Why this matters for your Embedding
As mentioned in the previous sections, to embed a manifold into a metric space, you need a way to "turn off" a coordinate map $\phi_i$ before you leave its domain $U_i$. 

If you have a map $\phi_i: U_i \to \mathbb{R}^n$, the product $\psi_i(x)\phi_i(x)$ (where $\psi_i$ is a bump function) is well-defined on the **entire** manifold $M$. Without the bump function, the map would "blow up" or be undefined outside of $U_i$.
