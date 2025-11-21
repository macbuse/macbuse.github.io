
## 📐 Exercice 1 : Plan, droite orthogonale et projection

Le plan $P$ est donné par :

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} + s\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} + t\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \quad s,t \in \mathbb{R} $$

Le point est $M = (3, 0, 3)$.

### 1\. Équation cartésienne du plan $P$

1.  **Vecteur Normal ($\vec{n}$)** : On calcule le produit vectoriel des deux vecteurs directeurs, 
$\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$ et $\vec{v} = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$.

$$\vec{n} = \vec{u} \times \vec{v}
 \begin{pmatrix} (2)(1) - (0)(1) \\ (0)(0) - (1)(1) \\ (1)(1) - (2)(0) \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$$

2.  **Équation $ax + by + cz = d$** : L'équation est de la forme **$2x - y + z = d$**.
3.  **Détermination de $d$** : On utilise le point $A(1, -2, 1)$ du plan :
    $$2(1) - (-2) + 1 = 2 + 2 + 1 = 5$$

L'équation cartésienne du plan $P$ est : $\mathbf{2x - y + z = 5}$.

-----

### 2\. Équation paramétrique de la droite $D$

La droite $D$ passe par $M(3, 0, 3)$ et a pour vecteur directeur le vecteur normal de $P$, $\vec{n} = \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$.

L'équation paramétrique de la droite $D$ est :

$$
\begin{cases}
x = 3 + 2t \\
y = -t \\
z = 3 + t
\end{cases}, \quad t \in \mathbb{R}
$$

-----

### 3\. Projection orthogonale $H = D \cap P$

On substitue les coordonnées de $D$ dans l'équation de $P$ ($2x - y + z = 5$) :
$$2(3 + 2t) - (-t) + (3 + t) = 5$$
$$6 + 4t + t + 3 + t = 5$$
$$9 + 6t = 5 \implies 6t = -4 \implies t = -\frac{2}{3}$$
On substitue $t = -2/3$ dans l'équation de $D$ :

$$x_H = 3 + 2\left(-\frac{2}{3}\right) = 3 - \frac{4}{3} = \frac{5}{3}$$

$$y_H = -\left(-\frac{2}{3}\right) = \frac{2}{3}$$

$$ z_H = 3 + \left(-\frac{2}{3}\right) = 3 - \frac{2}{3} = \frac{7}{3}$$

La projection orthogonale est le point $\mathbf{H = \left(\frac{5}{3}, \frac{2}{3}, \frac{7}{3}\right)}$.

-----

-----

## ✖️ Exercice 2 : Intersection de droites

On résout le système linéaire formé par les deux droites :
$$\begin{cases} 8x + 7y = -8 \quad (1) \\ x + y = 2 \quad (2) \end{cases}$$

De l'équation (2), on tire $y = 2 - x$. On substitue dans (1) :
$$8x + 7(2 - x) = -8$$
$$8x + 14 - 7x = -8$$
$$x + 14 = -8 \implies x = -22$$
On trouve $y$ :
$$y = 2 - (-22) = 24$$

L'intersection des droites $D_1$ et $D_2$ est le point $\mathbf{(-22, 24)}$.

-----

-----

## ▲ Exercice 3 : Aire du triangle

On utilise les points $X = (-1, 4)$, $Y = (2, -1)$, $Z = (0, 3)$.
L'aire $A$ est donnée par $A = \frac{1}{2} |\det(\vec{XY}, \vec{XZ})|$.

1.  **Vecteurs** :
$$\vec{XY} = (2 - (-1), -1 - 4) = (3, -5)$$
$$\vec{XZ} = (0 - (-1), 3 - 4) = (1, -1)$$
2.  **Déterminant** :
$$\det(\vec{XY}, \vec{XZ}) = \begin{vmatrix} 3 & 1 \\ -5 & -1 \end{vmatrix} = (3)(-1) - (1)(-5) = -3 + 5 = 2$$
3.  **Aire** :
$$A = \frac{1}{2} |2| = 1$$

L'aire du triangle $XYZ$ est de **1 unité carrée**.

-----

-----

## 🧮 Exercice 4 : Calcul de déterminants

### Déterminant de la matrice $D$

$$D = \begin{pmatrix}
3 & 1 & 1 \\
6 & 2 & 1 \\
12 & 4 & 1
\end{pmatrix}
$$

Puisque la colonne $C_1$ est égale à $3 \times C_2$, soit $C_1 = 3 C_2$ (car $\begin{pmatrix} 3 \\ 6 \\ 12 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}$), le déterminant est **nul**.
$$\det(D) = 0$$

### Déterminant de la matrice $E$

$$
E = \begin{pmatrix}
i & j & k \\
1 & 2 & 0 \\
0 & 1 & 1
\end{pmatrix}
$$

On développe par la première ligne ($i, j, k$ étant les vecteurs unitaires) :
$$\det(E) = i \begin{vmatrix} 2 & 0 \\ 1 & 1 \end{vmatrix} - j \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} + k \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix}$$
$$\det(E) = i(2\cdot 1 - 0\cdot 1) - j(1\cdot 1 - 0\cdot 0) + k(1\cdot 1 - 2\cdot 0)$$
$$\det(E) = 2i - j + k$$
Le déterminant est le vecteur $\mathbf{\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}}$.

### Déterminant de la matrice $F$ (Sans opération sur les lignes)

$$F = \begin{pmatrix}
1 & 1 & 1 \\
1 & 3 & 9 \\
1 & 2 & 4
\end{pmatrix} $$

On développe par la première ligne ($L_1$) :
$$\det(F) = 1 \cdot \begin{vmatrix} 3 & 9 \\ 2 & 4 \end{vmatrix} - 1 \cdot \begin{vmatrix} 1 & 9 \\ 1 & 4 \end{vmatrix} + 1 \cdot \begin{vmatrix} 1 & 3 \\ 1 & 2 \end{vmatrix}$$

1.  **Premier terme** : $1 \cdot ((3)(4) - (9)(2)) = 1 \cdot (12 - 18) = -6$
2.  **Deuxième terme** : $-1 \cdot ((1)(4) - (9)(1)) = -1 \cdot (4 - 9) = -1 \cdot (-5) = 5$
3.  **Troisième terme** : $1 \cdot ((1)(2) - (3)(1)) = 1 \cdot (2 - 3) = -1$

$$\det(F) = -6 + 5 - 1 = -2$$
Le déterminant de $F$ est $\mathbf{-2}$.

-----

