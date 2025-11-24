
---

### **Exercice 7 : Inéquations polynomiales**

Pour résoudre ces inéquations, nous allons étudier le signe des polynômes en trouvant leurs racines (là où l'expression vaut 0).

#### **(a) $x^2 - 2x - 3 > 0$**
1.  **Trouver les racines** ($x^2 - 2x - 3 = 0$) :
    * Discriminant $\Delta = b^2 - 4ac = (-2)^2 - 4(1)(-3) = 4 + 12 = 16$.
    * $\Delta > 0$, donc deux racines :
        $$x_1 = \frac{-(-2) - \sqrt{16}}{2} = \frac{2 - 4}{2} = -1$$
        $$x_2 = \frac{-(-2) + \sqrt{16}}{2} = \frac{2 + 4}{2} = 3$$
2.  **Tableau de signes** : Un polynôme du second degré ($ax^2+bx+c$) est du signe de $a$ (ici $1 > 0$, donc positif) à l'extérieur des racines.
3.  **Solution** : On cherche où l'expression est strictement positive ($>0$).
    **$$S = ]-\infty; -1[ \cup ]3; +\infty[$$**

#### **(b) $2x^2 - 7x + 3 \leq 0$**
1.  **Trouver les racines** :
    * $\Delta = (-7)^2 - 4(2)(3) = 49 - 24 = 25$.
    * Racines :
        $$x_1 = \frac{7 - 5}{4} = \frac{2}{4} = \frac{1}{2}$$
        $$x_2 = \frac{7 + 5}{4} = \frac{12}{4} = 3$$
2.  **Signe** : Le coefficient $a=2$ est positif. Le polynôme est négatif ou nul **entre** les racines.
3.  **Solution** :
    **$$S = \left[\frac{1}{2}; 3\right]$$**

#### **(c) $x^4 + 3x^2 - 4 \leq 0$**
C'est une inéquation bicarrée. Posons $X = x^2$ (avec $X \geq 0$).
L'inéquation devient : $X^2 + 3X - 4 \leq 0$.
1.  **Racines de l'équation en X** :
    * Racine évidente : $X_1 = 1$ (car $1+3-4=0$).
    * Produit des racines $P = c/a = -4$, donc $X_2 = -4$.
2.  **Signe en X** : Négatif entre les racines $[-4; 1]$.
    Donc on doit avoir $-4 \leq X \leq 1$.
3.  **Retour à x** :
    * $-4 \leq x^2 \leq 1$.
    * $x^2 \geq -4$ est toujours vrai (un carré est toujours positif).
    * Il reste $x^2 \leq 1$, ce qui équivaut à $-1 \leq x \leq 1$.
4.  **Solution** :
    **$$S = [-1; 1]$$**

---

### **Exercice 8 : Valeurs absolues**

La valeur absolue $|x - a|$ s'interprète graphiquement comme la **distance** entre le point $x$ et le point $a$ sur la droite réelle.

#### **(a) $|x + 3| \geq 1$**
* **Forme canonique** : $|x - (-3)| \geq 1$.
* **Interprétation graphique** : La distance entre $x$ et le point $-3$ doit être supérieure ou égale à 1.
    * On part de $-3$. On recule de 1 (vers $-4$) et on avance de 1 (vers $-2$).
    * On veut être à l'extérieur de cette zone.
* **Résolution algébrique** :
    $x + 3 \geq 1 \Rightarrow x \geq -2$
    OU
    $x + 3 \leq -1 \Rightarrow x \leq -4$
* **Solution** :
    **$$S = ]-\infty; -4] \cup [-2; +\infty[$$**

#### **(b) $1 < |1 - x| \leq 5$**
* Note : $|1 - x| = |x - 1|$.
* **Interprétation graphique** : La distance entre $x$ et le point $1$ doit être strictement supérieure à 1 ET inférieure ou égale à 5.
    * Centre : $1$.
    * Zone interdite (trop proche) : $]1-1; 1+1[ = ]0; 2[$.
    * Zone maximale (éloignement max) : $[1-5; 1+5] = [-4; 6]$.
    * On prend la zone maximale privée du centre.
* **Résolution algébrique** :
    * $|x-1| > 1 \Leftrightarrow x > 2$ ou $x < 0$.
    * $|x-1| \leq 5 \Leftrightarrow -5 \leq x-1 \leq 5 \Leftrightarrow -4 \leq x \leq 6$.
    * Intersection des deux conditions.
* **Solution** :
    **$$S = [-4; 0[ \cup ]2; 6]$$**

#### **(c) $|x + 3| = |x - 5|$**
* **Forme canonique** : $|x - (-3)| = |x - 5|$.
* **Interprétation graphique** : $x$ est à égale distance de $-3$ et de $5$. C'est le point milieu du segment $[-3; 5]$.
    * Milieu $m = \frac{-3 + 5}{2} = \frac{2}{2} = 1$.
* **Résolution algébrique** :
    $x + 3 = x - 5$ (impossible car $3 \neq -5$)
    OU
    $x + 3 = -(x - 5) \Rightarrow x + 3 = -x + 5 \Rightarrow 2x = 2 \Rightarrow x = 1$.
* **Solution** :
    **$$S = \{1\}$$**

#### **(d) $|x + 1| = |x^2 + x - 2|$**
* **Interprétation graphique** : On cherche les abscisses des points d'intersection entre la courbe $y = |x+1|$ et la courbe $y = |x^2+x-2|$.
* **Résolution algébrique** : $|A| = |B| \Leftrightarrow A = B$ ou $A = -B$.

    **Cas 1 : $x^2 + x - 2 = x + 1$**
    $$x^2 - 3 = 0$$
    $$x^2 = 3 \Rightarrow x = \sqrt{3} \text{ ou } x = -\sqrt{3}$$

    **Cas 2 : $x^2 + x - 2 = -(x + 1)$**
    $$x^2 + x - 2 = -x - 1$$
    $$x^2 + 2x - 1 = 0$$
    Calcul du discriminant $\Delta = 2^2 - 4(1)(-1) = 4 + 4 = 8$.
    $$x = \frac{-2 \pm \sqrt{8}}{2} = \frac{-2 \pm 2\sqrt{2}}{2} = -1 \pm \sqrt{2}$$

* **Solution** :
    $$S = \{-\sqrt{3}; \sqrt{3}; -1-\sqrt{2}; -1+\sqrt{2}\}$$

---


