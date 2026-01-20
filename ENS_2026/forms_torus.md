# 1 forms  and discussion of regular values


### A 1-Form that is not a $df$

To find a 1-form that is not the differential of a function (an **exact** form), we look for a form that is **not closed**. 

In $\mathbb{R}^2$, a general 1-form is written as:
$$\omega = P(x, y)dx + Q(x, y)dy$$

For a 1-form to be the differential of a function ($df$), it must satisfy the condition:
$$\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

If this condition is not met, the form is not exact, meaning no such $f$ exists where $df = \omega$.

### The Example
Consider the following 1-form:
$$\omega = y \, dx + 0 \, dy$$
Or simply:
**$\omega = y \, dx$**

---

### Why this is not a $df$
To prove that $\omega \neq df$ for any scalar function $f(x, y)$, we check the partial derivatives:

1.  **Identify $P$ and $Q$:**
    * $P(x, y) = y$
    * $Q(x, y) = 0$
2.  **Compute the mixed partials:**
    * $\frac{\partial P}{\partial y} = \frac{\partial}{\partial y}(y) = 1$
    * $\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}(0) = 0$
3.  **Compare:**
    * Since $1 \neq 0$, the exterior derivative $d\omega \neq 0$. 

Because the form is not **closed** ($d\omega \neq 0$), it cannot be **exact** ($\omega = df$) by Poincaré's Lemma.



### Geometric Intuition
A 1-form $\omega = df$ represents a **conservative field**. If you integrate a $df$ along a closed path, the result is always zero. 

However, if you integrate $\omega = y \, dx$ around a unit square from $(0,0)$ to $(1,0)$ to $(1,1)$ to $(0,1)$ and back to $(0,0)$:
* Along the bottom edge ($y=0$): $\int 0 \, dx = 0$
* Along the top edge ($y=1$ from $x=1$ to $x=0$): $\int_1^0 1 \, dx = -1$
* Vertical edges: $dx = 0$, so the integral is $0$.
* **Total Work:** $-1$. 

Since the line integral around a closed loop is non-zero, the form cannot be the gradient (differential) of a potential function.

---

## Torus and projection to the x-axis


### Surface of revolution: The torus

### 1. The Generating Curve
Let the generating circle $C$ be in the $xz$-plane, centered at $(R, 0, 0)$ with radius $r$. To ensure the resulting surface is a torus, we require $R > r > 0$.

The equations for this circle are:
$$(x - R)^2 + z^2 = r^2$$

Parametrization:
$$x(\phi) = R + r \cos \phi$$
$$z(\phi) = r \sin \phi$$

### 2. Parametrization of the Torus $T$
Rotating around the $z$-axis with angle $\theta \in [0, 2\pi)$:
$$x(\phi, \theta) = (R + r \cos \phi) \cos \theta$$
$$y(\phi, \theta) = (R + r \cos \phi) \sin \theta$$
$$z(\phi, \theta) = r \sin \phi$$



### 3. Implicit Definition
The torus is the zero-set of the function $F: \mathbb{R}^3 \setminus \{z\text{-axis}\} \to \mathbb{R}$:
$$F(x, y, z) = (\sqrt{x^2 + y^2} - R)^2 + z^2 - r^2$$

To show $T$ is a manifold, we check $\nabla F \neq 0$ on $T$:
$$\nabla F = \left( 2(\sqrt{x^2 + y^2} - R)\frac{x}{\sqrt{x^2 + y^2}}, \, 2(\sqrt{x^2 + y^2} - R)\frac{y}{\sqrt{x^2 + y^2}}, \, 2z \right)$$

The gradient vanishes only when $z=0$ and $\sqrt{x^2 + y^2} = R$. At such points, $F = -r^2$, which is not on our level set $F=0$. Thus, $0$ is a regular value, and $T$ is a smooth 2-manifold.

### Projection to the x-axis

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
