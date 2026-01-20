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

---


To show that the 2-sphere $S^2$ is a manifold using the **Regular Value Theorem** (which is a direct consequence of the **Implicit Function Theorem**), we follow these steps.

### 1. Define the Smooth Map
We consider $S^2$ as a subset of $\mathbb{R}^3$. Let $f: \mathbb{R}^3 \to \mathbb{R}$ be the smooth function:
$$f(x, y, z) = x^2 + y^2 + z^2$$

The 2-sphere is defined as the level set where $f$ equals $1$:
$$S^2 = f^{-1}(1) = \{(x, y, z) \in \mathbb{R}^3 \mid f(x, y, z) = 1\}$$

---

### 2. Identify Critical Points and Regular Values
A value $c \in \mathbb{R}$ is a **regular value** if for every $p$ in the level set $f^{-1}(c)$, the differential $df_p$ is surjective. For a map into $\mathbb{R}$, this simply means the gradient $\nabla f$ must not be the zero vector.

1.  **Calculate the Gradient:**
    $$\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right) = (2x, 2y, 2z)$$
2.  **Find Critical Points:**
    The gradient $\nabla f$ is the zero vector $(0,0,0)$ if and only if $x=0, y=0, z=0$.
3.  **Check the Level Set:**
    The only critical point of the function $f$ is the origin $(0,0,0)$. However, $f(0,0,0) = 0$. 
    Since $0 \neq 1$, the origin is **not** an element of the set $S^2$.

Thus, for all $p \in S^2$, $\nabla f(p) \neq \mathbf{0}$. This confirms that **$1$ is a regular value** of $f$.



---

### 3. Application of the Regular Value Theorem
The Regular Value Theorem states:
> If $f: M \to N$ is a smooth map between manifolds of dimension $m$ and $n$, and $c \in N$ is a regular value, then the preimage $f^{-1}(c)$ is a smooth submanifold of $M$ of dimension $(m - n)$.

Applying this to our case:
* $M = \mathbb{R}^3$ (dimension 3)
* $N = \mathbb{R}$ (dimension 1)
* $c = 1$ (a regular value)

The dimension of $S^2$ is $3 - 1 = 2$. Therefore, $S^2$ is a smooth 2-manifold.

---

### 4. Relation to the Implicit Function Theorem
The Implicit Function Theorem is the "engine" behind the Regular Value Theorem. Because the gradient is non-zero at any point $p = (x_0, y_0, z_0) \in S^2$, at least one partial derivative is non-zero. 

Suppose $\frac{\partial f}{\partial z}(p) = 2z_0 \neq 0$. The Implicit Function Theorem guarantees that near $p$, there exists a smooth function $g(x, y)$ such that the sphere can be expressed as a graph:
$$z = g(x, y) = \sqrt{1 - x^2 - y^2} \quad (\text{or } -\sqrt{1 - x^2 - y^2})$$



This local representation as a graph of a smooth function provides the **coordinate charts** required by the formal definition of a manifold.


---

### 1. The Map
The projection $\pi: T \to \mathbb{R}$ is defined by:
$$f(\phi, \theta) = (R + r \cos \phi) \cos \theta$$

### 2. Finding Critical Points
We set the partial derivatives to zero:
$$\frac{\partial f}{\partial \phi} = -r \sin \phi \cos \theta = 0$$
$$\frac{\partial f}{\partial \theta} = -(R + r \cos \phi) \sin \theta = 0$$

Since $R > r$, the term $(R + r \cos \phi)$ is strictly positive. Therefore, $\sin \theta = 0$ (implying $\cos \theta = \pm 1$). Plugging this into the first equation, we find $\sin \phi = 0$. 

The critical points occur at:
- $\theta \in \{0, \pi\}$
- $\phi \in \{0, \pi\}$

### 3. The Singular Values
Evaluating $f$ at these four combinations yields the singular values:
1. $f(0, 0) = R + r$
2. $f(\pi, 0) = R - r$
3. $f(\pi, \pi) = -(R - r) = r - R$
4. $f(0, \pi) = -(R + r) = -R - r$


Geometrically, these correspond to the "outer" and "inner" edges of the torus as it is projected onto the $x$-axis.

