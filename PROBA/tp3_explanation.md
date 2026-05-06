
### Manipulation des données
*   **`np.loadtxt(path)`** : Lit les données d'un fichier texte (comme `.txt` ou `.csv`). Chaque ligne est traitée comme une ligne et chaque valeur séparée par un espace ou une virgule comme une colonne, retournant un tableau NumPy.
*   **`np.linspace(start, stop, num)`** : Génère un tableau de `num` nombres répartis uniformément sur un intervalle spécifié. C'est idéal pour créer des lignes lisses lors du traçage de fonctions.

### Analyse statistique
*   **`np.polyfit(x, y, deg)`** : Ajuste un polynôme de degré `deg` aux données selon la méthode des moindres carrés. Utiliser `deg=1` renvoie la pente ($a$) et l'ordonnée à l'origine ($b$) pour une régression linéaire ($y = ax + b$).
*   **`np.corrcoef(x, y)`** : Calcule les coefficients de corrélation de Pearson. Il renvoie une matrice où les valeurs hors diagonale représentent la corrélation entre $x$ et $y$.
*   **`np.quantile(a, q)`** : Calcule le $q$-ième quantile des données. Par exemple, `0.5` est la médiane, tandis que `0.1` et `0.9` permettent d'identifier l'étalement ou les limites de la distribution.

### Opérations mathématiques
*   **`np.arccos(x)`** : Fonction arc cosinus (inverse du cosinus). Elle renvoie l'angle en radians pour une valeur de cosinus donnée.
*   **`np.degrees(x)`** : Une fonction pratique qui convertit les angles des radians vers les degrés.
*   **`np.mean(a)`** : Calcule la moyenne arithmétique des éléments d'un tableau.
*   **`np.min(a)` / `np.max(a)`** : Renvoie la valeur minimale ou maximale trouvée dans un tableau.

---

### Comprendre la régression linéaire
Dans le contexte de votre code, ces méthodes collaborent pour trouver la « droite d'ajustement » à travers vos points de données. Les méthodes `polyfit` et `corrcoef` sont les piliers ici, car elles déterminent mathématiquement à quel point la circonférence de l'eucalyptus (variable indépendante) est corrélée à sa hauteur (variable dépendante).
