[from here](https://math.stackexchange.com/questions/857971/ring-of-integers-is-a-pid-but-not-a-euclidean-domain)

[Dedekind's
criterion](https://kconrad.math.uconn.edu/blurbs/gradnumthy/dedekind-index-thm.pdf)


Here's what I think is a nice way to find a few PIDs that aren't Euclidean. It's not quite elementary, but if you know a bit about number fields I think it's a lot easier and nicer than the normal drudge. </p>

Let $K=\mathbb{Q}(\sqrt{-d})$ for $d>3$ squarefree, with ring of integers $\mathcal{O}_K$. Then the only units in $\mathcal{O}_K$ are $\pm1$.</p>

Suppose $\mathcal{O}_K$ is Euclidean with Euclidean function $\varphi$. Then take $x \in \mathcal{O}_K\setminus\{0,\pm1\}$ with $\varphi(x)$ minimal. By definition, any element of $\mathcal{O}_K$ can be written in the form $px+r$ where $\varphi(r) < \varphi(x)$, so it must be that $r \in \{0,\pm1\}$, i.e. $|\mathcal{O}_K/(x)|$ is $2$ or $3$. In other words $\mathcal{O}_K$ has a principal ideal of norm $2$ or $3$.</p>

So now we know that if $K = \mathbb{Q}(\sqrt{-d})$ has class number one, where $d>3$ is squarefree*, $K$ is a non-Euclidean PID if there are no elements in $\mathcal{O}_K$ of norm $\pm2$ or $\pm3$. As $K$ is a PID (and degree $2$ over $\mathbb{Q}$), this is equivalent to saying that $2$ and $3$ are inert. To find some examples then:</p>

If $d = 3\pmod{4}$, $\mathcal{O}_K = \mathbb{Z}[\frac{1+\sqrt{-d}}{2}]$, the minimal polynomial of $\frac{1+\sqrt{-d}}{2}$ over $\mathbb{Q}$ is $f_d(X)=X^2-X+\frac{1+d}{4}$. Applying Dedekind's criterion gives that $d$ works provided that $f_d(X)$ is irreducible $\pmod{2}$ and $\pmod{3}$. This then gives that $d = 19$ works (which is the usual example), but also shows that $d = 43,67$ or $163$ work as well (I think!).</p>

*It can be shown that this implies $d \in \{1,2,3,7,11,19,43,67,163\}$</p>
