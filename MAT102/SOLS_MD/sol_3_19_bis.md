La projection orthogonale $P$ d'un point $M$ sur une droite $\mathcal{D}$ est, par définition, le point de $\mathcal{D}$ qui minimise la distance (et donc le carré de la distance) entre $M$ et tout point de $\mathcal{D}$.

Nous allons résoudre la question **19 a)** en minimisant la fonction distance au carré.

---

### Résolution de l'Exercice 19 a) par Minimisation de la Distance

#### Question 19 a) :
* Point : $M = (1, 2)$
* Droite : $\mathcal{D} = \{(2t, 1 + t), t \in \mathbb{R}\}$

1.  **Définir le point générique** $P_t$ sur la droite $\mathcal{D}$:
    $$P_t = (2t, 1 + t)$$

2.  **Calculer la distance au carré** $f(t) = d(M, P_t)^2$:
    La formule de la distance au carré entre $M=(x_M, y_M)$ et $P_t=(x_t, y_t)$ est :
    $$f(t) = (x_t - x_M)^2 + (y_t - y_M)^2$$
    $$f(t) = (2t - 1)^2 + ((1 + t) - 2)^2$$
    $$f(t) = (2t - 1)^2 + (t - 1)^2$$

3.  **Développer la fonction $f(t)$**:
    $$f(t) = (4t^2 - 4t + 1) + (t^2 - 2t + 1)$$
    $$f(t) = 5t^2 - 6t + 2$$

4.  **Minimiser la fonction $f(t)$** (trouver $t$ tel que $f(t)$ est minimum).
    Puisque $f(t)$ est une fonction quadratique de la forme $at^2 + bt + c$ avec $a=5 > 0$, elle admet un minimum unique. Nous trouvons le minimum en annulant la dérivée première $f'(t)$.
    $$f'(t) = \frac{d}{dt} (5t^2 - 6t + 2)$$
    $$f'(t) = 10t - 6$$
    $$f'(t) = 0 \implies 10t - 6 = 0 \implies 10t = 6 \implies t = \frac{6}{10} = \frac{3}{5}$$

    *(Note : Si vous utilisez la formule pour le sommet d'une parabole : $t = -\frac{b}{2a} = -\frac{-6}{2(5)} = \frac{6}{10} = \frac{3}{5}$)*

5.  **Trouver les coordonnées de la projection $P$** en utilisant $t = \frac{3}{5}$:
    $$P = (2t, 1 + t)$$
    $$P = \left(2 \cdot \frac{3}{5}, 1 + \frac{3}{5}\right)$$
    $$P = \left(\frac{6}{5}, \frac{5}{5} + \frac{3}{5}\right)$$
    $$P = \left(\frac{6}{5}, \frac{8}{5}\right)$$

### Conclusion
La projection orthogonale est $\mathbf{P = \left(\frac{6}{5}, \frac{8}{5}\right)}$.

Cette méthode par minimisation du carré de la distance donne bien le même résultat que la méthode par orthogonalité ($\vec{MP} \cdot \vec{u} = 0$), confirmant que les deux approches sont équivalentes en géométrie euclidienne.

