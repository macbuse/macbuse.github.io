# Big Three


In differential topology, the concept of a **regular value** is the primary tool used to ensure that the preimage of a set is a well-behaved manifold.

### The Definition

Let $f: X \to Y$ be a smooth map between manifolds of dimensions $n$ and $m$, respectively.

**1. Critical Points**
A point $x \in X$ is called a **critical point** of $f$ if the derivative (or differential):
$$df_x: T_xX \to T_{f(x)}Y$$
is **not surjective** (i.e., the rank of the linear map is less than the dimension of the target manifold $Y$).

**2. Regular Points**
A point $x \in X$ is a **regular point** if $df_x$ is surjective. This means the derivative map "hits" every direction in the target tangent space.

**3. Regular Values**
A point $y \in Y$ is called a **regular value** of $f$ if **every** $x$ in the preimage $f^{-1}(y)$ is a regular point. 

> **Important Note:** If the preimage $f^{-1}(y)$ is empty, $y$ is vacuously considered a **regular value**.

---

### The Preimage Theorem
If $y$ is a regular value of a smooth map $f: X \to Y$, then the subset $Z = f^{-1}(y) \subset X$ is a **submanifold** of $X$ with:
$$\dim Z = \dim X - \dim Y$$


## example


To determine if $0$ is a regular value of the map $f(x, y, z) = x^2 + y^2 + z^2 - 1$, we must follow the definition: check the derivative at every point in the preimage $f^{-1}(0)$.

### 1. Identify the Preimage
First, we look at all points $(x, y, z)$ such that $f(x, y, z) = 0$:
$$x^2 + y^2 + z^2 - 1 = 0 \implies x^2 + y^2 + z^2 = 1$$
The preimage $f^{-1}(0)$ is the **unit sphere** $S^2$ in $\mathbb{R}^3$.

### 2. Compute the Derivative
The map $f$ goes from $\mathbb{R}^3 \to \mathbb{R}$. Its derivative $df$ at any point $(x, y, z)$ is represented by the gradient (a linear map from $\mathbb{R}^3 \to \mathbb{R}$):
$$df_{(x,y,z)} = \begin{bmatrix} 2x & 2y & 2z \end{bmatrix}$$



### 3. Test for Surjectivity
For $0$ to be a **regular value**, the linear map $df_{(x,y,z)}$ must be **surjective** for every point in the preimage.
* Since the target space is $\mathbb{R}^1$, "surjective" simply means the linear map is not the zero map ($rank = 1$).
* The only point in all of $\mathbb{R}^3$ where the derivative is the zero map $[0, 0, 0]$ is the origin $(0, 0, 0)$.

### 4. Check the Preimage Points
Is the origin $(0, 0, 0)$ in our preimage $f^{-1}(0)$?
* $0^2 + 0^2 + 0^2 = 0 \neq 1$.
* The origin is **not** on the sphere.

Since the origin is the only critical point of the function, and it does not lie on the sphere, the derivative is surjective at every point on the sphere. Thus, $0$ is a **regular value**.

---

### Comparison: When is a value NOT regular?
If we chose the value $c = -1$, the preimage $f^{-1}(-1)$ would be:
$$x^2 + y^2 + z^2 - 1 = -1 \implies x^2 + y^2 + z^2 = 0$$
The

---


### Why these are the "Big Three" for Milnor
* **Inverse Function Theorem:** Milnor uses this to define **local coordinates**. It ensures that if the derivative is non-singular, the manifold "looks like" Euclidean space locally.
* **Implicit Function Theorem:** This is used to prove that the preimage of a **regular value** is a submanifold. For example, if $f(x,y,z) = x^2+y^2+z^2-1$, the regular value $0$ gives us the sphere.
* **Change of Variables:** This is the heart of **Integration on Manifolds**. It proves that the integral of a differential form doesn't depend on which coordinate chart (like stereographic projection) you choose.

## Notation

That is an astute observation regarding Spivak's specific pedagogical choices. In *Calculus on Manifolds*, Michael Spivak is very deliberate about how he bridges the gap between elementary calculus and modern differential geometry.

The short answer is: **Spivak uses $f'$ as a shorthand for the total derivative (the linear transformation), whereas $df(a)$ or $df_a$ is more common in the "modern" manifold language used by Milnor and G&P.**

Here is the breakdown of why he chooses that notation and how it relates to the other books.

---

### 1. The "Calculus" Heritage
Spivak titled the book *Calculus on Manifolds* because he wanted to generalize the $f'(x)$ you learned in high school. 
* In 1D calculus, $f'(x)$ is a number. 
* In Spivak's multivariable world, **$f'(a)$ is the unique linear transformation** that best approximates $f$ near $a$.
* By keeping the "prime" notation, he emphasizes that this is exactly the same concept as the derivative of a single-variable function, just upgraded to higher dimensions.

### 2. $f'(a)$ vs. $Df(a)$ vs. $df_a$
In the mathematical community, there is a "notation war" for the derivative. Here is how they compare:

| Notation | Author/Context | Nuance |
| :--- | :--- | :--- |
| **$f'(a)$** | **Spivak** | Emphasizes the derivative as a single object (a linear map). |
| **$Df(a)$** | **Analysis/G&P** | Often used to emphasize the "Differential Operator" acting on $f$. |
| **$df_a$** | **Milnor / Geometry** | Emphasizes the **Differential Form** or the map between Tangent Spaces ($T_aM \to T_{f(a)}N$). |
| **$J_f(a)$** | **Applied Math** | The **Jacobian matrix** (the numerical representation of the linear map). |

### 3. The Geometric Shift in Milnor
When you move from Spivak to Milnor, you will see the notation shift to $df_a$. 
* **Spivak** stays in $\mathbb{R}^n$, so he doesn't need to worry about which "space" the derivative lives in; it's always $\mathbb{R}^n$.
* **Milnor** is working on manifolds $M$ and $N$. He uses $df_a$ because he is thinking of the derivative as a **push-forward**—it takes a vector in the tangent space of the starting manifold and "pushes" it into the tangent space of the target manifold.



---

### Summary: How to read them
When you are reading the "Big Three" theorems in Spivak:
* Every time you see **$f'(a)$**, read it as **"The linear transformation that is the derivative."**
* When you go back to **Milnor**, and he writes **$df_a$**, realize he is talking about the exact

---

## Statements of the "Big Three" Theorems in Spivak

Here are the statements as they appear in the text (specifically Chapters 2 and 3).

### 1. Inverse Function Theorem
**Found in: Chapter 2**

> **Theorem 2-11:** Suppose that $f: \mathbb{R}^n \to \mathbb{R}^n$ is a continuously differentiable function in an open set containing $a$, and $\det f'(a) \neq 0$. Then there is an open set $V$ containing $a$ and an open set $W$ containing $f(a)$ such that $f: V \to W$ has a continuous inverse $f^{-1}: W \to V$ which is differentiable and for all $y \in W$ satisfies
> $$(f^{-1})'(y) = [f'(f^{-1}(y))]^{-1}$$



---

### 2. Implicit Function Theorem
**Found in: Chapter 2**

Spivak presents this as a consequence of the Inverse Function Theorem, often using the following notation for a function $f: \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}^m$:

> **Theorem 2-12:** Let $f: \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}^m$ be continuously differentiable in an open set containing $(a, b)$ and suppose $f(a, b) = 0$. Let $M$ be the $m \times m$ matrix $(D_{n+j} f^i(a, b))$. If $\det M \neq 0$, then there is an open set $A \subset \mathbb{R}^n$ containing $a$ and an open set $B \subset \mathbb{R}^m$ containing $b$, and a unique function $g: A \to B$ such that $f(x, g(x)) = 0$ for all $x \in A$. The function $g$ is differentiable.



---

### 3. Change of Variables Formula
**Found in: Chapter 3**

This is the most technically demanding statement in the book, involving the absolute value of the determinant of the Jacobian.

> **Theorem 3-13:** Let $A \subset \mathbb{R}^n$ be an open set and $g: A \to \mathbb{R}^n$ a $1-1$ continuously differentiable function such that $\det g'(x) \neq 0$ for all $x \in A$. If $f: g(A) \to \mathbb{R}$ is integrable, then
> $$\int_{g(A)} f = \int_A (f \circ g) \cdot |\det g'|$$



---

