# MNUM


**Pour info** le CC1 aura lieu la semaine du 7 mars

- [F1](./METH_NUM/1_feuille_flottant.pdf) Nombres flottants
	- 21/1 exos 1, 3 et 5  [correction](./METH_NUM/TP_1_corr.pdf) and [my brouillon](./METH_NUM/TP1.ipynb)
	- 28/1 exos 6,7 et 8 [correction](./METH_NUM/1_feuille_flottant_corrigé.pdf) and [my brouillon](./METH_NUM/f1exo8.html)
	- 4/2 finir exo 8 ([convergence](https://www.maa.org/press/periodicals/loci/joma/iterative-methods-for-solving-iaxi-ibi-analysis-of-jacobi-and-gauss-seidel-methods) dans Jacobi) puis passer a F2
	- 11/2 **controle de 20 minutes en classe**
	- 18/2 **DM en classe** [voici le sujet](./METH_NUM/cc1_2021_print.pdf) c'est le CC du mars 2021. Vous pouvez le faire en groupes.
	- [correction](./METH_NUM/cc1_2021_corr.pdf)
- [F2](./METH_NUM/2_feuille_condition.pdf) Systèmes, conditionnement

---
## controle du 11/2

- Vous devez vous mettre en binome 
- 30 minutes pour proposer une démarche et essayer de la programmer.
- Après 30min de travail, je ferai le tour des groupes 
- note A, B ou C. 

- **Sujet 1)** Proposer une méthode de calcul approché d'une primitive d'une fonction donnée sur [a,b]. Par exemple f(x) = exp(-x^2) sur [0, 1]
"Indication" : utiliser des différences finies d'ordre 1 ou 2 en imposant une valeur en 0 (la constante d'intégration)
- **Sujet 2)** Traiter l'approximation de l'équation différentielle de l'exercice 8 en remplaçant le terme c(x) u (x) par c(x) * u'(x). Quelle discrétisation ? Ordre de convergence ?


---

#### notes TP1

Two examples where binary (base 2) arithmetic is best:
- [modexp](https://github.com/secworks/modexp/blob/master/src/model/python/modexp.py)
- [Q_rsqrt](https://en.wikipedia.org/wiki/Fast_inverse_square_root)

Naive evaluation should look like this

```
def naif_eval(x,P):
    val = 0
    for i, coeff in enumerate(P):
        val += coeff*x**i
    return val 
```

Horner should look like this in Python:
```
def horner(x, P):
    val = 0
    for coeff in reversed(P):
        val *= x
        val += coeff
    return val
```
---

#### notes TP2-TP3

You should learn how to use **numpy** notation for matrices
[quickstart](https://numpy.org/doc/stable/user/quickstart.html)

- ```np.array```
- ```shape``` + ```reshape```
- ```np.identity```
- ```np.zeros``` ```np.ones```
- ```np.dot()``` matrix multiplication

Etude de convergence dans la methode de Jacobi.
- C = matrice 2x2 
- V = valeur initiale (1,1)
- solution exacte = (0,1)

```
C = np.array([2,1,1,1]).reshape(2,2)
D = np.array([C[i,i] for i in range(C.shape[0])])
V = np.ones(2)
b = np.ones(2)

E = []
for k in range(40):
    #V = (-LU.dot(V) + b)/D
    V = V + (-C.dot(V) + b)/D
    E.append(np.linalg.norm(V - [0,1]))
plt.plot(np.log(E));
```

