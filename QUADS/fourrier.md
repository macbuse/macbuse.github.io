Let $0<c_1<c_2<1$ and define, on one period $[0,1]$,

$$
f(t)=
\begin{cases}
a(1-t)+bt=a+\alpha t,& t\in[c_1,c_2],\\[2mm]
0,& \text{otherwise},
\end{cases}\qquad \alpha:=b-a,
$$

extended periodically with period $1$.

# Complex Fourier series (period $1$)

With $f(t)=\sum_{n\in\mathbb Z} c_n e^{i2\pi n t}$ and
$c_n=\int_0^1 f(t)e^{-i2\pi n t}\,dt$, write $\omega=2\pi n$. Then

$$
\boxed{\,c_0=\int_0^1 f(t)\,dt=a(c_2-c_1)+\frac{\alpha}{2}\,(c_2^2-c_1^2)\,}
$$

and, for $n\neq0$,

$$
\boxed{\;
c_n=\!\!\int_{c_1}^{c_2}(a+\alpha t)e^{-i\omega t}\,dt
=(e^{-i\omega c_2}-e^{-i\omega c_1})\!\left(\frac{\alpha}{\omega^2}-\frac{a}{i\omega}\right)
-\frac{\alpha}{i\omega}\,\big(c_2e^{-i\omega c_2}-c_1e^{-i\omega c_1}\big).}
$$

# Real sine–cosine form

With

$$
f(t)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\big(a_n\cos(2\pi n t)+b_n\sin(2\pi n t)\big),
\quad \omega=2\pi n,
$$

$$
\boxed{\,a_0=2\!\int_0^1 f=2a(c_2-c_1)+\alpha\,(c_2^2-c_1^2)\,;}
$$

for $n\ge1$,

$$
\boxed{\;a_n=2\!\int_{c_1}^{c_2}(a+\alpha t)\cos(\omega t)\,dt
=2\!\left[
a\,\frac{\sin(\omega c_2)-\sin(\omega c_1)}{\omega}
+\alpha\!\left(
\frac{c_2\sin(\omega c_2)-c_1\sin(\omega c_1)}{\omega}
+\frac{\cos(\omega c_2)-\cos(\omega c_1)}{\omega^2}
\right)\right],}
$$

$$
\boxed{\;b_n=2\!\int_{c_1}^{c_2}(a+\alpha t)\sin(\omega t)\,dt
=2\!\left[
a\,\frac{\cos(\omega c_1)-\cos(\omega c_2)}{\omega}
+\alpha\!\left(
\frac{-c_2\cos(\omega c_2)+c_1\cos(\omega c_1)}{\omega}
+\frac{\sin(\omega c_2)-\sin(\omega c_1)}{\omega^2}
\right)\right].}
$$

**Notes.**

* At the jump points $t=c_1,c_2$, the Fourier series converges to the midpoint of the one-sided limits.
* Setting $c_1=0$ recovers the “on–from–0–to–$c_2$” case; setting $c_2=1$ recovers the earlier ramp on $[0,1]$.

