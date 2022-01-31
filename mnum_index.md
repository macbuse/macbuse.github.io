# MNUM


- [F1](./METH_NUM/1_feuille_flottant.pdf)
	- 21/1 exos 1, 3 et 5  [correction](./METH_NUM/TP_1_corr.pdf) and [my brouillon](./METH_NUM/TP1.ipynb)
	- 28/1 exos 6,7 et 8 [correction](./METH_NUM/1_feuille_flottant_corrigé.pdf)
	

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

#### notes TP2

You should learn how to use **numpy** notation for matrices
[quickstart](https://numpy.org/doc/stable/user/quickstart.html)

- ```np.array```
- ```np.identity```
- ```np.zeros```
- ```np.dot()``` matrix multiplication


