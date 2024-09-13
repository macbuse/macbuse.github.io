## Calcul direct de \((3 + i)^3\)


Pour développer \((1 + i)^3\), on peut utiliser le binôme de Newton ou multiplier directement.

### Étape 1 : Calculer \((1 + i)^2\)

\[
(1 + i)^2 = (1 + i)(1 + i)
\]

En développant, on obtient :

- \(
= 1^2 + 2 \cdot 1 \cdot i + i^2
\)
- \(
= 1 + 2i + (-1) \quad \text{(puisque \( i^2 = -1 \))}
\)
- \(
= 2i
\)

### Étape 2 : Multiplier le résultat par \( (1 + i) \)

\[
(1 + i)^3 = (1 + i) \cdot (2i)
\]

Développons à nouveau :

- \(
= 1 \cdot 2i + i \cdot 2i
\)
\(
- = 2i + 2i^2
\)
- \(
= 2i + 2(-1) \quad \text{(puisque \( i^2 = -1 \))}
\)
- \(
= 2i - 2
\)

### Conclusion :

\(
(1 + i)^3 = -2 + 2i
\)

---

### Vérification avec la forme polaire


Pour vérifier le résultat de \((1 + i)^3\) en utilisant la forme polaire, nous allons d'abord exprimer \(1 + i\) en coordonnées polaires, puis utiliser la formule de De Moivre pour élever ce nombre à la puissance 3.

### Étape 1 : Conversion de \(1 + i\) en forme polaire

Un nombre complexe \(z = x + yi\) peut être exprimé en forme polaire sous la forme \(z = r(\cos \theta + i \sin \theta)\), où :
- \(r = |z|\) est le module de \(z\),
- \(\theta\) est l'argument de \(z\).

Dans notre cas, \(z = 1 + i\), donc \(x = 1\) et \(y = 1\).

1. **Calcul du module** \(r\) :
\[
r = \sqrt{x^2 + y^2} = \sqrt{1^2 + 1^2} = \sqrt{2}
\]

2. **Calcul de l'argument** \(\theta\) :
\[
\theta = \text{arg}(z) = \tan^{-1}\left(\frac{y}{x}\right) = \tan^{-1}\left(\frac{1}{1}\right) = \frac{\pi}{4}
\]

Donc, la forme polaire de \(1 + i\) est :

\[
1 + i = \sqrt{2} \left( \cos \frac{\pi}{4} + i \sin \frac{\pi}{4} \right)
\]

### Étape 2 : Utilisation de la formule de De Moivre

Pour élever \(1 + i\) à la puissance 3, on utilise la formule de De Moivre :
\[
\left( r \left( \cos \theta + i \sin \theta \right) \right)^n = r^n \left( \cos (n\theta) + i \sin (n\theta) \right)
\]
Ici, \(r = \sqrt{2}\), \(\theta = \frac{\pi}{4}\), et \(n = 3\).

1. **Calcul du module** :
\[
r^3 = (\sqrt{2})^3 = 2^{3/2} = 2\sqrt{2}
\]

2. **Calcul de l'argument** :
\[
n\theta = 3 \times \frac{\pi}{4} = \frac{3\pi}{4}
\]

La forme polaire de \((1 + i)^3\) est donc :

\[
(1 + i)^3 = 2\sqrt{2} \left( \cos \frac{3\pi}{4} + i \sin \frac{3\pi}{4} \right)
\]

### Étape 3 : Conversion en forme algébrique

Nous utilisons les valeurs de \(\cos \frac{3\pi}{4}\) et \(\sin \frac{3\pi}{4}\) :
\[
\cos \frac{3\pi}{4} = -\frac{1}{\sqrt{2}}, \quad \sin \frac{3\pi}{4} = \frac{1}{\sqrt{2}}
\]

Substituons dans l'expression :

\[
(1 + i)^3 = 2\sqrt{2} \left( -\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}} \right)
\]

Simplifions :

- \(
(1 + i)^3 = 2\sqrt{2} \times \left( -\frac{1}{\sqrt{2}} \right) + 2\sqrt{2} \times \left( i \frac{1}{\sqrt{2}} \right)
\)
- \(
(1 + i)^3 = -2 + 2i
\)

### Conclusion :

En utilisant la forme polaire, nous obtenons le même résultat :

\[
(1 + i)^3 = -2 + 2i
\]
