
---

## Exercice 11

Trois vecteurs $\vec{u}, \vec{v}, \vec{w}$ sont coplanaires si et seulement si le déterminant de la matrice formée par leurs coordonnées est nul (produit mixte nul).

### a) $\vec{u} = (1,2,3)$, $\vec{v} = (-1,3,4)$, $\vec{w} = (1,0,2)$



Calculons le déterminant par développement selon la troisième ligne (qui contient un zéro) :

$$\det(\vec{u}, \vec{v}, \vec{w}) = \begin{vmatrix} 1 & -1 & 1 \\ 2 & 3 & 0 \\ 3 & 4 & 2 \end{vmatrix}$$

Développement par rapport à la 3ᵉ colonne (ou 3ᵉ ligne) :


$$\begin{aligned} \det = 1 \cdot \begin{vmatrix} 2 & 3 \\ 3 & 4 \end{vmatrix} + 2 \cdot \begin{vmatrix} 1 & -1 \\ 2 & 3 \end{vmatrix} &= 1 \cdot (8 - 9) + 2 \cdot (3 - (-2)) \\ &= -1 + 2(5) = 9 \neq 0 \end{aligned}$$

Les 3 vecteurs **ne sont pas coplanaires**.

---

### b) $\vec{u} = (1,-1,1)$, $\vec{v} = (2,2,1)$, $\vec{w} = (0,-4,1)$



$$\det(\vec{u}, \vec{v}, \vec{w}) = \begin{vmatrix} 1 & 2 & 0 \\ -1 & 2 & -4 \\ 1 & 1 & 1 \end{vmatrix}$$

Développement par rapport à la première ligne :


$$\begin{aligned} \det = 1 \cdot \begin{vmatrix} 2 & -4 \\ 1 & 1 \end{vmatrix} - 2 \cdot \begin{vmatrix} -1 & -4 \\ 1 & 1 \end{vmatrix} &= 1 \cdot (2 - (-4)) - 2 \cdot (-1 - (-4)) \\ &= 6 - 2(3) = 0 \end{aligned}$$

Le déterminant étant nul, les 3 vecteurs **sont coplanaires**.

---

## Exercice 12

### a) Matrice identité



$$\begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix} = 1$$

### b) Matrice triangulaire inférieure



Le déterminant d'une matrice triangulaire est le produit des éléments diagonaux :


$$\begin{vmatrix} a & 0 & 0 \\ 6 & b & 0 \\ 7 & 1 & c \end{vmatrix} = a \cdot b \cdot c = abc$$

### c) Matrice triangulaire supérieure



$$\begin{vmatrix} 1 & x & y \\ 0 & 2 & z \\ 0 & 0 & 3 \end{vmatrix} = 1 \cdot 2 \cdot 3 = 6$$

### d)



Développement selon la première colonne :


$$\begin{vmatrix} a & 0 & 5 \\ 0 & 0 & c \\ 0 & b & 0 \end{vmatrix} = a \cdot \begin{vmatrix} 0 & c \\ b & 0 \end{vmatrix} = a(0 - bc) = -abc$$

### e)



Développement selon la troisième ligne :


$$\begin{vmatrix} 0 & b & 7 \\ 11 & 0 & c \\ a & 0 & 0 \end{vmatrix} = a \cdot \begin{vmatrix} b & 7 \\ 0 & c \end{vmatrix} = a(bc - 0) = abc$$

### f)



Développement selon la première colonne :


$$\begin{vmatrix} 1 & 6 & 7 \\ 0 & \cos\beta & -\sin\beta \\ 0 & \sin\beta & \cos\beta \end{vmatrix} = 1 \cdot \begin{vmatrix} \cos\beta & -\sin\beta \\ \sin\beta & \cos\beta \end{vmatrix} = \cos^2\beta - (-\sin^2\beta) = \cos^2\beta + \sin^2\beta = 1$$

### g)



Développement selon la première ligne :


$$\begin{vmatrix} 1 & 0 & 0 \\ 6 & 9 & 2 \\ 4 & -1 & 0 \end{vmatrix} = 1 \cdot \begin{vmatrix} 9 & 2 \\ -1 & 0 \end{vmatrix} = 0 - (-2) = 2$$

### h)



$$\begin{vmatrix} 2 & -1 & 3 \\ -1 & 1 & 3 \\ -2 & 1 & 1 \end{vmatrix}$$

Règle de Sarrus (ou développement $L_1$) :


$$2(1 - 3) - (-1)(-1 - (-6)) + 3(-1 - (-2)) = 2(-2) + 1(5) + 3(1) = -4 + 5 + 3 = 4$$

### i)



Remarquons que la ligne 3 est le double de la ligne 2 ($L_3 = 2 L_2$) : $(2, 4, 6) = 2(1, 2, 3)$.


$$\begin{vmatrix} i & j & k \\ 1 & 2 & 3 \\ 2 & 4 & 6 \end{vmatrix} = 0$$

### j)



Calcul du produit vectoriel $(1,3,2) \wedge (2,1,4)$ via le déterminant formel :


$$\begin{aligned} \begin{vmatrix} i & j & k \\ 1 & 3 & 2 \\ 2 & 1 & 4 \end{vmatrix} &= i(12 - 2) - j(4 - 4) + k(1 - 6) \\ &= 10i + 0j - 5k = 10i - 5k \quad \text{ou } (10, 0, -5) \end{aligned}$$

### k)


$$\begin{aligned} \begin{vmatrix} i & j & k \\ 1 & 0 & 1 \\ 0 & 2 & 3 \end{vmatrix} &= i(0 - 2) - j(3 - 0) + k(2 - 0) \\ &= -2i - 3j + 2k \quad \text{ou } (-2, -3, 2) \end{aligned}$$

### l) Déterminant $4 \times 4$



$$D = \begin{vmatrix} 1 & -1 & 0 & 1 \\ 0 & -1 & 0 & 2 \\ 3 & -2 & 2 & 1 \\ 1 & 4 & 2 & 1 \end{vmatrix}$$

Opération sur les lignes pour faire apparaître un zéro : $L_4 \leftarrow L_4 - L_3$


$$D = \begin{vmatrix} 1 & -1 & 0 & 1 \\ 0 & -1 & 0 & 2 \\ 3 & -2 & 2 & 1 \\ -2 & 6 & 0 & 0 \end{vmatrix}$$

Développement par rapport à la 3ᵉ colonne (qui contient trois 0) :


$$D = 2 \cdot (-1)^{3+3} \begin{vmatrix} 1 & -1 & 1 \\ 0 & -1 & 2 \\ -2 & 6 & 0 \end{vmatrix}$$

Calcul du sous-déterminant $3 \times 3$ (développement par rapport à la 1ʳᵉ colonne) :


$$\begin{aligned} \begin{vmatrix} 1 & -1 & 1 \\ 0 & -1 & 2 \\ -2 & 6 & 0 \end{vmatrix} &= 1 \cdot (0 - 12) - 2 \cdot (-2 - (-1)) \\ &= -12 - 2(-1) = -12 + 2 = -10 \end{aligned}$$

D'où :


$$D = 2 \times (-10) = -20$$
