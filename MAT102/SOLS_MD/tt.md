To write
$
f(x)=|x+1|-|2x-1|
$
as a **piecewise linear function**, we split at the points where the absolute values change sign:

* $x+1=0 \Rightarrow x=-1$
* $2x-1=0 \Rightarrow x=\tfrac12$

So we consider three intervals.

---

## **1. For (x < -1)**

* $x+1 < 0 \Rightarrow |x+1| = -(x+1)$
* $2x-1 < 0 \Rightarrow |2x-1| = -(2x-1)$

$$
f(x)=-(x+1)-\big(-(2x-1)\big)
= -x -1 +2x -1 = x -2
$$

---

## **2. For $-1 \le x < \frac12)$**

* $x+1 \ge 0 \Rightarrow |x+1| = x+1$
* $2x-1 < 0 \Rightarrow |2x-1| = -(2x-1)$

$$
f(x)= (x+1)-\big(-(2x-1)\big)
= x+1 +2x -1 = 3x
$$

---

## **3. For $x \ge \tfrac12$**

* $x+1 \ge 0 \Rightarrow |x+1| = x+1$
* $2x-1 \ge 0 \Rightarrow |2x-1| = 2x-1$

$$
f(x)= (x+1)-(2x-1)
= x+1 -2x +1 = -x+2
$$

---

## **Final Piecewise Function**

$$
f(x)=
\begin{cases}
x-2, & x < -1,\\
3x, & -1 \le x < \tfrac12,\\
-x+2, & x \ge \tfrac12 .
\end{cases}
$$


