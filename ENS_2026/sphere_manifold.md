To explain that the 2-sphere ($S^2$) is a manifold using stereographic projection, you are essentially showing that the sphere can be covered by "flat" coordinate maps (charts). This is the perfect example of the "Differentiable Viewpoint" because it uses smooth functions to link the curved geometry of the sphere to the flat plane of $\mathbb{R}^2$.

---

## 1. The Setup
We define the unit 2-sphere in $\mathbb{R}^3$ as:
$$S^2 = \{(x, y, z) \in \mathbb{R}^3 : x^2 + y^2 + z^2 = 1\}$$

To prove it is a manifold, we need to find a collection of open sets that cover the sphere and "map" them smoothly to $\mathbb{R}^2$. We use two specific points to project from:
1.  **The North Pole ($N$):** $(0, 0, 1)$
2.  **The South Pole ($S$):** $(0, 0, -1)$



## 2. The Projection Formula (The "North" Chart)
Imagine a light source at the North Pole. For any point $P(x, y, z)$ on the sphere (except the North Pole itself), we draw a line from $N$ through $P$ until it hits the $xy$-plane ($z=0$).

The point where it hits the plane is $U(u, v)$. Using similar triangles or line equations, the mapping $\sigma_N: S^2 \setminus \{N\} \to \mathbb{R}^2$ is:
$$u = \frac{x}{1-z}, \quad v = \frac{y}{1-z}$$

### Why this matters:
* **Smoothness:** This map is smooth (infinitely differentiable) everywhere except at $z=1$ (the North Pole).
* **Homeomorphism:** It is a one-to-one mapping between the "punctured" sphere and the entire flat plane.

## 3. Covering the Whole Sphere
One map isn't enough because we "missed" the North Pole. To fix this, we create a second map, $\sigma_S$, by projecting from the **South Pole** onto the plane.
$$\sigma_S: S^2 \setminus \{S\} \to \mathbb{R}^2$$
$$u' = \frac{x}{1+z}, \quad v' = \frac{y}{1+z}$$

Now, every single point on the sphere is covered by at least one of these two open "neighborhoods"
* $U_N = S^2 \setminus \{N\}$
* $U_S = S^2 \setminus \{S\}$

## 4. The "Differentiable" Check (Transition Maps)
In Milnor's view, for this to be a *differentiable* manifold, the overlap between these two maps must be smooth. If you take a point in the overlap (everywhere except the poles), map it to the plane via $\sigma_N$, and then map it back to the other plane via $\sigma_S$, the result must be a smooth function.

The transition map $\sigma_S \circ \sigma_N^{-1}$ from $\mathbb{R}^2 \setminus \{(0,0)\}$ to itself is:
$$(u, v) \mapsto \left( \frac{u}{u^2 + v^2}, \frac{v}{u^2 + v^2} \right)$$
Since $u^2 + v^2 \neq 0$ on the overlap, this function is smooth. 

---

### Summary for your explanation:
* **The Atlas:** You have two charts $(\sigma_N, \sigma_S)$.
* **The Manifold:** Because these charts cover $S^2$ and the transition between them is smooth, $S^2$ is a smooth 2-manifold.
* **Visual Analogy:** It’s like a world map. You can’t represent the whole Earth on one flat map without a "tear," but you can use two maps (like two hemispheres) that overlap smoothly at the edges.
