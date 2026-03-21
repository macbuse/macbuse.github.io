# Topology from a differential viewpoint

## Course Schedule


| Date | Name | Title |
| :--- | :--- | :--- |
| January 20, 2026 | Greg Mc| introduction|
| January 27, 2026 | Louve + Emanuel | espace tangent, d'alembert gauss |
| February 3, 2026 | Louis et Théo | 1 manifolds |
| February 10, 2026 |Emanuel et Maryam | Sard |
| February 17, 2026 | **VACANCES**|  |
| February 24, 2026 | Louve   | Brouwer |
| March 3, 2026 | Maryam    | Brouwer  |
| March 10, 2026 | **PARTIELS** | |
| March 17, 2026 | | exercices |
| March 24, 2026 |Théo  | Varieté orientable |
| March 31, 2026 | Louis | Champs de vecteurs |
| April 13, 2026 | Emmanuel | |


---

## 17/03

| | Exercise # | Topic | Key Hint / Strategy |
| :--- | :--- | :--- | :--- |
| **Theo** | **2** | Complex Polynomials | Use the **Fundamental Theorem of Algebra**. For a regular value $w$, $P(z) = w$ has $n$ roots. Since $P$ is holomorphic, the Jacobian determinant of the module of $P'(z)^2$ is always $\ge 0$, so each preimage counts as $+1$ toward the degree. |
| **Theo** | **6** | Brouwer Fixed Point | Use **proof by contradiction**. If $f(x) \neq x$ for all $x$, then $f$ is homotopic to the antipodal map $a(x) = -x$. Since $\text{deg}(a) = (-1)^{n+1}$, any map with a different degree must have a fixed point. |
| **Maryam** | **3** | Non-Antipodal Maps | The condition $\|f(x) - g(x)\| < 2$ means $f(x)$ and $g(x)$ are never opposite. Define a straight-line homotopy $H(t) = (1-t)f(x) + tg(x)$ and normalize it: $H/\|H\|$ to keep it on the sphere. |
| **Louve** | **4** | Smooth Approximation | Extend $f$ to a neighborhood and use the **Stone-Weierstrass Theorem** to find a smooth map $g$ such that $\|f - g\| < \epsilon$. If $\epsilon$ is small, $g(x)/\|g(x)\|$ is a smooth map to $S^p$ homotopic to $f$. |
| **Louve** | **9** | Graphs of Maps | Consider the map $\psi: M \to M \times N$ defined by $\psi(x) = (x, f(x))$. Show this is an embedding. The tangent space $T\Gamma$ is the image of the derivative $d\psi_x(v) = (v, df_x(v))$, which is exactly the graph of $df_x$. |
| **Emanuel** | **7** | Odd Degree Maps | If $f(x)$ never equals $-f(-x)$, then $f$ is homotopic to an even map. Even maps $S^n \to S^n$ have even degree (specifically $0$ for even $n$), which contradicts the "odd degree" premise. |
| **Louis** | **5** | Dimension Mismatch | By **Sard’s Theorem**, if $m < p$, the image $f(M)$ has measure zero in $S^p$. Therefore, $f$ is not surjective. A non-surjective map into $S^p$ maps into a contractible punctured sphere and is thus homotopic to a constant. |


---


## Week 5 files


- [exposé](./expose_5w_Topology_from_the_differentiable_viewpoint___Exposé_Sard_et_Brown.pdf)

---

## Week 4 files

- [exposé](./week4_expose2.pdf)


---

## Week 3 files

- [exposé](./Classification des variétés de dimension 1.pdf))
- [long line, second countablity](./long_line.html)


--

## Week 2 files

Louve + Emanuel
- [exposé](./expose1.pdf)
- [SL(2,R) as a (sub)manifold](./sl2.html)
- [S0(3) as a (sub)manifold](./so3.html)
- [D'Alembert Gauss via homotopy](https://htmlpreview.github.io/?https://github.com/macbuse/ALG_TOP/blob/master/gauss_dalembert.html)
---

## Week 1 files

- [Philosophy](./philosophy.html)
- [Example: the 2 sphere](./sphere_manifold.html)
- [big three theorems](./big_three.html)
- [1-forms and the example the torus](./forms_torus.html)



---



### Summary

The book's "highlight" is its ability to prove profound topological results -like the **Brouwer Fixed Point Theorem** - using almost nothing but the concept of **smooth maps** and **regular values**.

---


###  Bibliography the "Trio"

- [text in pdf](https://math.uchicago.edu/~may/REU2017/MilnorDiff.pdf)
- [Guilleman
Spivak](https://www.cimat.mx/~gil/docencia/2020/topologia_diferencial/%5BGuillemin,Pollack%5DDifferential_Topology%281974%29.pdf)
- [Spivak Calculus on
Manifolds](https://www.cimat.mx/~gil/docencia/2013/topologia_variedades/spivak-calculus-on-manifolds.pdf)

### Supplementary References
- [Comment on Hirsch's proof of Brouwer's
theorem](https://www.ams.org/journals/proc/2000-128-05/S0002-9939-99-05205-3/S0002-9939-99-05205-3.pdf)

---

### Summary of the "Trio"

| Book | Role in your Study |
| :--- | :--- |
| **Milnor** | The **Vision:** Tells you the deep truths (What). |
| **G&P** | The **Intuition:** Shows you the pictures and examples (How). |
| **Spivak** | The **Rigors:** Proves the underlying calculus (Why). |

---

---

### Key Summary Table

| Concept | Significance |
| :--- | :--- |
| **Regular Values** | The tool used to "slice" manifolds and see their internal structure. |
| **Homotopy** | Proving that "deforming" a map doesn't change its fundamental properties (like degree). |
| **Orientability** | How "left-handed" and "right-handed" systems affect the way we count preimages. |
| **Euler Characteristic** | The single number that captures a manifold's most basic shape (holes, etc.). |


louis.bissay@ens-lyon.fr, louve.grosjean--ducateau@ens-lyon.fr, maryam.kouhkan@ens-lyon.fr, theo.feijoo@ens-lyon.fr
