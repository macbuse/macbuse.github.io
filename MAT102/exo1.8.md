## 8.1

Got it ✅ — GitHub Markdown does **not** render LaTeX by default (like `\sin(\theta)`) unless you use **inline code** or plain text math.
So I'll rewrite the solution in a **GitHub-friendly style**:

* Use backticks `` `...` `` for inline math.
* Use plain fractions like `pi/3`, `sqrt(2)/2` instead of `\tfrac{\pi}{3}`.
* No LaTeX environments (`\[` or `$$`).

Here’s **Exercise 8.1 rewritten for GitHub Markdown**:

---

### Exercice 8.1

On cherche les valeurs de sinus et cosinus des angles suivants :
`2pi/3`, `9pi/2`, `-9pi/12`, `-11pi/6`, `-13pi/4`, `7pi/3`, `-8pi/3`.

```math
\pi/3, 9\pi/2, -9\pi/12, -11\pi/6, -13\pi/4, 7\pi/3, -8\pi/3.
```

---

#### 1) `2pi/3`

* Quadrant II → `sin > 0`, `cos < 0`
* Angle de référence : `pi - 2pi/3 = pi/3`
* Résultats :

  * `sin(2pi/3) = sqrt(3)/2`
  * `cos(2pi/3) = -1/2`

---

#### 2) `9pi/2`

* Réduire modulo `2pi`: `9pi/2 = 4pi + pi/2`
* Résultats :

  * `sin(9pi/2) = sin(pi/2) = 1`
  * `cos(9pi/2) = cos(pi/2) = 0`

---

#### 3) `-9pi/12 = -3pi/4`

* Identité : `sin(-θ) = -sin(θ)`, `cos(-θ) = cos(θ)`
* Valeurs usuelles : `sin(3pi/4) = sqrt(2)/2`, `cos(3pi/4) = -sqrt(2)/2`
* Résultats :

  * `sin(-3pi/4) = -sqrt(2)/2`
  * `cos(-3pi/4) = -sqrt(2)/2`

---

#### 4) `-11pi/6`

* Réduire modulo `2pi`: `-11pi/6 + 2pi = pi/6`
* Résultats :

  * `sin(-11pi/6) = sin(pi/6) = 1/2`
  * `cos(-11pi/6) = cos(pi/6) = sqrt(3)/2`

---

#### 5) `-13pi/4`

* Réduire modulo `2pi`:

  * `-13pi/4 + 2pi = -5pi/4`
  * `-5pi/4 + 2pi = 3pi/4`
* Résultats :

  * `sin(-13pi/4) = sin(3pi/4) = sqrt(2)/2`
  * `cos(-13pi/4) = cos(3pi/4) = -sqrt(2)/2`

---

#### 6) `7pi/3`

* Réduire modulo `2pi`: `7pi/3 - 2pi = pi/3`
* Résultats :

  * `sin(7pi/3) = sin(pi/3) = sqrt(3)/2`
  * `cos(7pi/3) = cos(pi/3) = 1/2`

---

#### 7) `-8pi/3`

* Réduire modulo `2pi`: `-8pi/3 + 2pi = -2pi/3`
* Identité : `sin(-θ) = -sin(θ)`, `cos(-θ) = cos(θ)`
* Valeurs de `2pi/3`: `sin(2pi/3) = sqrt(3)/2`, `cos(2pi/3) = -1/2`
* Résultats :

  * `sin(-8pi/3) = -sqrt(3)/2`
  * `cos(-8pi/3) = -1/2`

---

### ✅ Résumé

| Angle     | Sinus        | Cosinus      |
| --------- | ------------ | ------------ |
| `2pi/3`   | `sqrt(3)/2`  | `-1/2`       |
| `9pi/2`   | `1`          | `0`          |
| `-3pi/4`  | `-sqrt(2)/2` | `-sqrt(2)/2` |
| `-11pi/6` | `1/2`        | `sqrt(3)/2`  |
| `-13pi/4` | `sqrt(2)/2`  | `-sqrt(2)/2` |
| `7pi/3`   | `sqrt(3)/2`  | `1/2`        |
| `-8pi/3`  | `-sqrt(3)/2` | `-1/2`       |



---

## 8.2

Perfect 👍 Let’s rewrite **Exercice 8.2** step by step in **GitHub-friendly Markdown**, just like we did for 8.1.

---

### Exercice 8.2

Exprimer les sinus et cosinus des angles suivants **en fonction de** `sin(pi/5)` et `cos(pi/5)` :

`-pi/5`, `6pi/5`, `9pi/5`, `4pi/5`, `pi/2 - pi/5`, `3pi/2 + pi/5`.

---

#### 1) `-pi/5`

* Identités :

  * `sin(-θ) = -sin(θ)`
  * `cos(-θ) = cos(θ)`
* Résultats :

  * `sin(-pi/5) = -sin(pi/5)`
  * `cos(-pi/5) = cos(pi/5)`

---

#### 2) `6pi/5`

* Réduction : `6pi/5 = pi + pi/5`
* Identités :

  * `sin(pi + θ) = -sin(θ)`
  * `cos(pi + θ) = -cos(θ)`
* Résultats :

  * `sin(6pi/5) = -sin(pi/5)`
  * `cos(6pi/5) = -cos(pi/5)`

---

#### 3) `9pi/5`

* Réduction : `9pi/5 = pi + 4pi/5`
* Identités :

  * `sin(pi + θ) = -sin(θ)`
  * `cos(pi + θ) = -cos(θ)`
* Résultats :

  * `sin(9pi/5) = -sin(4pi/5)`
  * `cos(9pi/5) = -cos(4pi/5)`
* Et comme `sin(4pi/5) = sin(pi - pi/5) = sin(pi/5)`, `cos(4pi/5) = -cos(pi/5)` :

  * `sin(9pi/5) = -sin(pi/5)`
  * `cos(9pi/5) = cos(pi/5)`

---

#### 4) `4pi/5`

* Réduction : `4pi/5 = pi - pi/5`
* Identités :

  * `sin(pi - θ) = sin(θ)`
  * `cos(pi - θ) = -cos(θ)`
* Résultats :

  * `sin(4pi/5) = sin(pi/5)`
  * `cos(4pi/5) = -cos(pi/5)`

---

#### 5) `pi/2 - pi/5`

* Identité :

  * `sin(pi/2 - θ) = cos(θ)`
  * `cos(pi/2 - θ) = sin(θ)`
* Résultats :

  * `sin(pi/2 - pi/5) = cos(pi/5)`
  * `cos(pi/2 - pi/5) = sin(pi/5)`

---

#### 6) `3pi/2 + pi/5`

* Identités :

  * `sin(3pi/2 + θ) = -cos(θ)`
  * `cos(3pi/2 + θ) = sin(θ)`
* Résultats :

  * `sin(3pi/2 + pi/5) = -cos(pi/5)`
  * `cos(3pi/2 + pi/5) = sin(pi/5)`

---

### ✅ Résumé

| Angle          | Sinus        | Cosinus      |
| -------------- | ------------ | ------------ |
| `-pi/5`        | `-sin(pi/5)` | `cos(pi/5)`  |
| `6pi/5`        | `-sin(pi/5)` | `-cos(pi/5)` |
| `9pi/5`        | `-sin(pi/5)` | `cos(pi/5)`  |
| `4pi/5`        | `sin(pi/5)`  | `-cos(pi/5)` |
| `pi/2 - pi/5`  | `cos(pi/5)`  | `sin(pi/5)`  |
| `3pi/2 + pi/5` | `-cos(pi/5)` | `sin(pi/5)`  |

---


