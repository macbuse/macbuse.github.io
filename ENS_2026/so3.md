# $SO(3)$ is a manifold

## Identity as a regular value proof


To show that $SO(3)$ is a manifold, we consider it as a subspace of the Euclidean space of matrices $M(3, \mathbb{R}) \cong \mathbb{R}^9$.

### 1. The Mapping
Define a smooth map $f: M(3, \mathbb{R}) \to \text{Sym}(3, \mathbb{R})$ by:
$$f(A) = A^T A$$
where $\text{Sym}(3, \mathbb{R}) \cong \mathbb{R}^6$ is the space of $3 \times 3$ symmetric matrices. The orthogonal group $O(3)$ is the preimage of the identity matrix:
$$O(3) = f^{-1}(I)$$

### 2. The Derivative
To apply the Regular Value Theorem, we calculate the derivative $Df_A$ at a point $A \in O(3)$ in the direction of a tangent vector $H \in M(3, \mathbb{R})$:
$$Df_A(H) = \left. \frac{d}{dt} \right|_{t=0} f(A + tH)$$
$$Df_A(H) = \left. \frac{d}{dt} \right|_{t=0} (A + tH)^T(A + tH)$$
$$Df_A(H) = A^T H + H^T A$$

### 3. Surjectivity Proof
For $I$ to be a regular value, $Df_A$ must be surjective onto $\text{Sym}(3, \mathbb{R})$. Let $S \in \text{Sym}(3, \mathbb{R})$ be an arbitrary symmetric matrix. We must find an $H$ such that $Df_A(H) = S$.

Choose $H = \frac{1}{2} AS$. Substituting this into the derivative:
$$Df_A\left(\frac{1}{2} AS\right) = A^T\left(\frac{1}{2} AS\right) + \left(\frac{1}{2} AS\right)^T A$$
Since $A^T A = I$ and $S^T = S$:
$$Df_A\left(\frac{1}{2} AS\right) = \frac{1}{2}(A^T A)S + \frac{1}{2}S^T(A^T A)$$
$$Df_A\left(\frac{1}{2} AS\right) = \frac{1}{2}IS + \frac{1}{2}SI = S$$

### 4. Conclusion
Since $Df_A$ is surjective for all $A \in f^{-1}(I)$, the Regular Value Theorem implies that $O(3)$ is a smooth manifold of dimension:
$$\dim(M(3, \mathbb{R})) - \dim(\text{Sym}(3, \mathbb{R})) = 9 - 6 = 3$$
Because $SO(3)$ is the subgroup where $\det(A) = 1$ (an open condition in $O(3)$), it is also a smooth $3$-dimensional manifold.

---

## Proof using the Exponential Map


To show $SO(3)$ is a manifold using the exponential map, we demonstrate that the group is locally homeomorphic to a linear vector space.

### 1. The Lie Algebra $\mathfrak{so}(3)$
The tangent space at the identity, denoted $\mathfrak{so}(3)$, consists of $3 \times 3$ skew-symmetric matrices:
$$\mathfrak{so}(3) = \{ X \in M(3, \mathbb{R}) : X^T = -X \}$$
An arbitrary element $X \in \mathfrak{so}(3)$ has the form:
$$X = \begin{pmatrix} 0 & -z & y \\ z & 0 & -x \\ -y & x & 0 \end{pmatrix}$$
This is a linear subspace of $\mathbb{R}^9$ with dimension $3$.

### 2. The Exponential Map
The matrix exponential $\exp: M(3, \mathbb{R}) \to M(3, \mathbb{R})$ is defined by the power series:
$$\exp(X) = \sum_{k=0}^{\infty} \frac{X^k}{k!}$$
If $X$ is skew-symmetric, then $R = \exp(X)$ is orthogonal ($\exp(X)^T = \exp(X^T) = \exp(-X) = \exp(X)^{-1}$) and has $\det(R) = 1$. Thus, $\exp$ maps $\mathfrak{so}(3)$ into $SO(3)$.

### 3. Local Diffeomorphism
The derivative of the exponential map at the origin $0 \in \mathfrak{so}(3)$ is the identity map:
$$D(\exp)_0 = I$$
By the **Inverse Function Theorem**, there exists a neighborhood $U$ of $0$ in $\mathfrak{so}(3)$ and a neighborhood $V$ of $I$ in $SO(3)$ such that $\exp: U \to V$ is a diffeomorphism.

### 4. Manifold Structure
This provides a coordinate chart $(V, \exp^{-1})$ around the identity matrix $I$. For any other point $R \in SO(3)$, we can define a chart around $R$ by shifting the identity chart:
$$\phi_R(A) = \exp^{-1}(R^{-1}A)$$
Because we can cover the entire group with these smooth charts, $SO(3)$ is a smooth manifold of dimension $3$.


---

## Homeomorphism between $SO(3)$ and $\mathbb{R}P^3$


To show $SO(3) \cong \mathbb{R}P^3$, we utilize the axis-angle representation of rotations.

### 1. The Ball Model
Consider the closed ball of radius $\pi$ in $\mathbb{R}^3$:
$$D^3_{\pi} = \{ \vec{v} \in \mathbb{R}^3 : \|\vec{v}\| \le \pi \}$$
For any $\vec{v} \in D^3_{\pi}$, let $\theta = \|\vec{v}\|$ and $\vec{u} = \vec{v}/\theta$. We associate $\vec{v}$ with the rotation $R_{\vec{u}, \theta} \in SO(3)$.

### 2. Boundary Identification
This map is a bijection on the interior of the ball. However, on the boundary where $\|\vec{v}\| = \pi$, the rotation $R_{\vec{u}, \pi}$ is identical to $R_{-\vec{u}, \pi}$ because a rotation by $180^\circ$ is orientation-equivalent to a rotation by $-180^\circ$ (or $180^\circ$ in the opposite direction).
Thus, we define an equivalence relation $\sim$ on $D^3_{\pi}$:
$$\vec{v} \sim -\vec{v} \iff \|\vec{v}\| = \pi$$
The resulting quotient space is $D^3_{\pi} / \sim$.

### 3. Homeomorphism to $\mathbb{R}P^3$
By definition, the real projective space $\mathbb{R}P^3$ can be constructed by taking a $3$-disk $D^3$ and identifying antipodal points on its boundary sphere $S^2$. Therefore:
$$SO(3) \cong D^3_{\pi} / \sim \;\cong \mathbb{R}P^3$$

---

## Killing form

To compute the signature of the Killing form $B(X, Y)$ for $\mathfrak{so}(3)$, we use the adjoint representation.

### 1. The Basis and Commutation Relations
A standard basis for the Lie algebra $\mathfrak{so}(3)$ consists of the skew-symmetric matrices $\{L_1, L_2, L_3\}$:
$$L_1 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}, \quad L_2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ -1 & 0 & 0 \end{pmatrix}, \quad L_3 = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
The commutation relations are given by $[L_i, L_j] = \sum_{k=1}^3 \epsilon_{ijk} L_k$, or specifically:
$$[L_1, L_2] = L_3, \quad [L_2, L_3] = L_1, \quad [L_3, L_1] = L_2$$

### 2. The Adjoint Representation
The Killing form is defined as $B(X, Y) = \text{tr}(\text{ad}_X \text{ad}_Y)$. We first find the matrix representation of $\text{ad}_{L_1}$ acting on the basis $\{L_1, L_2, L_3\}$:
* $\text{ad}_{L_1}(L_1) = [L_1, L_1] = 0$
* $\text{ad}_{L_1}(L_2) = [L_1, L_2] = L_3$
* $\text{ad}_{L_1}(L_3) = [L_1, L_3] = -L_2$

In matrix form:
$$\text{ad}_{L_1} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$$

### 3. Calculating the Trace
To find $B(L_1, L_1)$, we compute $(\text{ad}_{L_1})^2$:
$$(\text{ad}_{L_1})^2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix}$$
The trace is:
$$B(L_1, L_1) = \text{tr}((\text{ad}_{L_1})^2) = 0 - 1 - 1 = -2$$
By symmetry of the commutation relations, it follows that $B(L_2, L_2) = -2$ and $B(L_3, L_3) = -2$. For $i \neq j$, the off-diagonal terms $B(L_i, L_j)$ vanish.

### 4. The Killing Matrix and Signature
The matrix representing the Killing form in this basis is:
$$\mathbf{B} = \begin{pmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}$$
The eigenvalues are $\{-2, -2, -2\}$. The signature is $(0, 3)$, meaning the form is **negative definite**.
