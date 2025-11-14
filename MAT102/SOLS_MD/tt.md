Pour résoudre l'**Exercice 26**, nous devons trouver l'équation paramétrique de la droite $\mathcal{D}$, qui est l'intersection des deux plans $\mathcal{P}_1$ et $\mathcal{P}_2$.

L'intersection est définie par le système d'équations cartésiennes des deux plans :
$$
\mathcal{D}: \begin{cases} \text{Équation de } \mathcal{P}_1 \\ \text{Équation de } \mathcal{P}_2 \end{cases}
$$
Pour trouver la forme paramétrique, nous résolvons ce système en exprimant deux variables en fonction de la troisième (le paramètre $t$).

***

## **Exercice 26 a)** 📐
Plans :
* $\mathcal{P}_1: x + y + z = 3$
* $\mathcal{P}_2: x - 2y + z = 0$

Système :
$$
(S) \begin{cases} x + y + z = 3 \quad (1) \\ x - 2y + z = 0 \quad (2) \end{cases}
$$

**1. Trouver le vecteur directeur** $\vec{v}$ :
Le vecteur directeur $\vec{v}$ de la droite $\mathcal{D}$ est orthogonal aux deux vecteurs normaux $\vec{n}_1$ et $\vec{n}_2$ des plans. On le trouve par le produit vectoriel $\vec{n}_1 \times \vec{n}_2$.
* $\vec{n}_1 = (1, 1, 1)$
* $\vec{n}_2 = (1, -2, 1)$

$$\vec{v} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \times \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} = \begin{pmatrix} (1)(1) - (1)(-2) \\ (1)(1) - (1)(1) \\ (1)(-2) - (1)(1) \end{pmatrix} = \begin{pmatrix} 1 - (-2) \\ 1 - 1 \\ -2 - 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ -3 \end{pmatrix}$$
On peut simplifier le vecteur directeur à $\vec{v}' = (1, 0, -1)$.

**2. Trouver un point** $A$ **de la droite** $\mathcal{D}$ :
Cherchons un point où, par exemple, $y=0$. Substituons $y=0$ dans $(S)$ :
$$
\begin{cases} x + 0 + z = 3 \implies x + z = 3 \\ x - 2(0) + z = 0 \implies x + z = 0 \end{cases}
$$
Ce système n'a **pas de solution** (car $3 \neq 0$). Cela signifie que la droite d'intersection ne coupe pas le plan $y=0$.

Cherchons un point où $x=0$ :
$$
\begin{cases} 0 + y + z = 3 \implies y + z = 3 \quad (3) \\ 0 - 2y + z = 0 \implies z = 2y \quad (4) \end{cases}
$$
Substituons $(4)$ dans $(3)$ :
$$y + (2y) = 3 \implies 3y = 3 \implies y = 1$$
Ensuite, $z = 2(1) = 2$.
Le point d'intersection est $A = (0, 1, 2)$.

**3. Équation Paramétrique de** $\mathcal{D}$ :
En utilisant le point $A(0, 1, 2)$ et le vecteur directeur $\vec{v}'(1, 0, -1)$, l'équation paramétrique est :
$$\mathcal{D}: \begin{cases} x = 0 + 1t \\ y = 1 + 0t \\ z = 2 - 1t \end{cases}, \quad t \in \mathbb{R}$$
$$\mathcal{D}: \begin{cases} \mathbf{x = t} \\ \mathbf{y = 1} \\ \mathbf{z = 2 - t} \end{cases}, \quad t \in \mathbb{R}$$

---

## **Exercice 26 b)** 📐
Plans :
* $\mathcal{P}_1: x + y - z = -1$
* $\mathcal{P}_2: x + 2y + 3z = 0$

Système :
$$
(S) \begin{cases} x + y - z = -1 \quad (1) \\ x + 2y + 3z = 0 \quad (2) \end{cases}
$$

**1. Trouver le vecteur directeur** $\vec{v}$ :
* $\vec{n}_1 = (1, 1, -1)$
* $\vec{n}_2 = (1, 2, 3)$

$$\vec{v} = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \times \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} (1)(3) - (-1)(2) \\ (-1)(1) - (1)(3) \\ (1)(2) - (1)(1) \end{pmatrix} = \begin{pmatrix} 3 + 2 \\ -1 - 3 \\ 2 - 1 \end{pmatrix} = \begin{pmatrix} 5 \\ -4 \\ 1 \end{pmatrix}$$
Vecteur directeur : $\vec{v} = (5, -4, 1)$.

**2. Trouver un point** $A$ **de la droite** $\mathcal{D}$ :
Choisissons $z=0$ (paramètre $t=0$).
$$
\begin{cases} x + y - 0 = -1 \implies x + y = -1 \quad (3) \\ x + 2y + 3(0) = 0 \implies x + 2y = 0 \quad (4) \end{cases}
$$
Soustraire $(3)$ de $(4)$:
$$(x + 2y) - (x + y) = 0 - (-1) \implies y = 1$$
Substituer $y=1$ dans $(3)$:
$$x + 1 = -1 \implies x = -2$$
Le point d'intersection est $A = (-2, 1, 0)$.

**3. Équation Paramétrique de** $\mathcal{D}$ :
En utilisant le point $A(-2, 1, 0)$ et le vecteur directeur $\vec{v}(5, -4, 1)$, l'équation paramétrique est :
$$\mathcal{D}: \begin{cases} x = -2 + 5t \\ y = 1 - 4t \\ z = 0 + 1t \end{cases}, \quad t \in \mathbb{R}$$
$$\mathcal{D}: \begin{cases} \mathbf{x = -2 + 5t} \\ \mathbf{y = 1 - 4t} \\ \mathbf{z = t} \end{cases}, \quad t \in \mathbb{R}$$

---

## **Exercice 26 c)** 📐
Plans :
* $\mathcal{P}_1: 2x - z = 1$
* $\mathcal{P}_2: x + y = 2$

Système :
$$
(S) \begin{cases} 2x - z = 1 \quad (1) \\ x + y = 2 \quad (2) \end{cases}
$$

**1. Trouver le vecteur directeur** $\vec{v}$ :
* $\vec{n}_1 = (2, 0, -1)$ (Attention, $y$ n'apparaît pas, donc son coefficient est 0)
* $\vec{n}_2 = (1, 1, 0)$ (Attention, $z$ n'apparaît pas, donc son coefficient est 0)

$$\vec{v} = \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} \times \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} (0)(0) - (-1)(1) \\ (-1)(1) - (2)(0) \\ (2)(1) - (0)(1) \end{pmatrix} = \begin{pmatrix} 0 - (-1) \\ -1 - 0 \\ 2 - 0 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$$
Vecteur directeur : $\vec{v} = (1, -1, 2)$.

**2. Trouver un point** $A$ **de la droite** $\mathcal{D}$ :
Choisissons $x=0$ (ce choix peut être remplacé par $y=0$ ou $z=0$).
Substituons $x=0$ dans $(S)$:
$$
\begin{cases} 2(0) - z = 1 \implies z = -1 \\ 0 + y = 2 \implies y = 2 \end{cases}
$$
Le point d'intersection est $A = (0, 2, -1)$.

**3. Équation Paramétrique de** $\mathcal{D}$ :
En utilisant le point $A(0, 2, -1)$ et le vecteur directeur $\vec{v}(1, -1, 2)$, l'équation paramétrique est :
$$\mathcal{D}: \begin{cases} x = 0 + 1t \\ y = 2 - 1t \\ z = -1 + 2t \end{cases}, \quad t \in \mathbb{R}$$
$$\mathcal{D}: \begin{cases} \mathbf{x = t} \\ \mathbf{y = 2 - t} \\ \mathbf{z = -1 + 2t} \end{cases}, \quad t \in \mathbb{R}$$
