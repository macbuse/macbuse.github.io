import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import scipy.stats as stats
import math


## Exo 1
exemple1 = npr.random(10)
exemple2 = npr.choice(exemple1, size=(2,3), replace=False)
exemple3 = npr.choice([0,3,4],10,p=[1/4,1/4,1/2])
x = np.linspace(-3, 3, num=100)

plt.figure()
plt.subplot(2,2,1)
plt.title("Densité")
plt.plot(x, stats.norm(loc=0, scale=1).pdf(x))
plt.xlabel("x")
plt.ylabel("Probabilité")

plt.subplot(2,2,2)
plt.title("Fonction de répartition")
plt.plot(x, stats.norm.cdf(x))
plt.xlabel("x")
plt.ylabel("Probabilité")


prob = np.linspace(0, 1, num=100)
plt.subplot(2,2,3)
plt.title("Fonction quantile")
plt.plot(prob, stats.norm.ppf(prob))
plt.xlabel("Probabilité")
plt.ylabel("x")


n = 10; p = 1/2;
x = range(n+1)

plt.subplot(2,2,4)
plt.title("Fonction de masse")
plt.vlines(x, 0, stats.binom(n, p).pmf(x))
plt.xlabel("x")
plt.ylabel("Probabilité")
plt.show()


XY = npr.normal(size=(2,100))

plt.figure()
plt.title("Nuage de points des données")
plt.scatter(XY[0,:], XY[1,:])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

## Exo 2
n=1000

p=3/4
X1=(npr.uniform(size=n)<=p) +0
plt.figure()
plt.subplot(3,1,1)
plt.scatter(np.arange(1,n+1),X1)

p=1/np.arange(1,n+1)
X2=(npr.uniform(size=n)<=p) +0
plt.subplot(3,1,2)
plt.scatter(np.arange(1,n+1),X2)

p=1/np.arange(1,n+1)**2
X3=(npr.uniform(size=n)<=p) +0
plt.subplot(3,1,3)
plt.scatter(np.arange(1,n+1),X3)
plt.show()

## Exo 3
n=1000
U=npr.uniform(size=n)
#q1
l=1.5
X=-np.log(1-U)/l
Xs=sorted(X)
q = np.linspace(0, max(Xs), num=100)
plt.figure()
plt.title("Comparaison des f.r empiriques et théoriques")
plt.plot(q, stats.expon(scale=1/l).cdf(q))
plt.step(Xs,np.linspace(0,1,num=n),color='r',where='post')
plt.ylabel("Probabilité")
plt.xlabel("q")
plt.show()
#q2
a=2
X=(1-U)**(-1/a)
Xs=sorted(X)
q = np.linspace(1, max(Xs), num=100)
plt.figure()
plt.title("Comparaison des f.r empiriques et théoriques")
plt.plot(q, 1-1/q**a)
plt.step(Xs,np.arange(1,n+1)/n,color='r',where='post')
plt.ylabel("Probabilité")
plt.xlabel("q")
plt.show()

## Exo 4
#q1
def geom(N,p):
    Y=np.zeros(N)
    for j in range(0,N):
        X=npr.choice([0,1],p=[1-p,p])
        t=1
        while X!=1:
            X=npr.choice([0,1],p=[1-p,p])
            t=t+1
        Y[j]=t
    return(Y)
#q2
N=100
p=1/3
Y=geom(N,p)
Ys=sorted(Y)
q = np.arange(1, max(Ys)+1)
plt.figure()
plt.title("Comparaison des f.r empiriques et théoriques")
plt.step(q, 1-(1-p)**q,where='post')
plt.step(Ys,np.arange(1,N+1)/N,color='r',where='post')
plt.ylabel("Probabilité")
plt.xlabel("q")
plt.show()
#q3
table = np.unique(Y, return_counts=True)
freq = table[1]/N

x=np.arange(1,max(Y)+1)
plt.figure()
plt.bar(table[0],freq,label="Fréquence empirique") # Diagramme en batons
plt.vlines(x, 0, stats.geom(p).pmf(x), label='Probabilité',color='r')
plt.xlabel("x")
plt.show()

## Exo 5
#q1
N=1000
p=2/5
plt.figure()
for i in range(0,5):
    X=npr.binomial(1,p,size=N)
    Sbar=np.cumsum(X)/np.arange(1,N+1)
    plt.plot(np.arange(1,N+1),Sbar)
    plt.hlines(p,1,N,color='r',linestyles='dashed')
    plt.title('LGN Bernoulli')
plt.show()

#q2
N=1000
l=2
plt.figure()
for i in range(0,5):
    X=npr.poisson(l,size=N)
    Sbar=np.cumsum(X)/np.arange(1,N+1)
    plt.plot(np.arange(1,N+1),Sbar)
    plt.hlines(l,1,N,color='r',linestyles='dashed')
    plt.title('LGN Poisson')
plt.show()

l=0.1
plt.figure()
for i in range(0,5):
    X=npr.poisson(l,size=N)
    Sbar=np.cumsum(X)/np.arange(1,N+1)
    plt.plot(np.arange(1,N+1),Sbar)
    plt.hlines(l,1,N,color='r',linestyles='dashed')
    plt.title('LGN Poisson')
plt.show()

#q3
N=1000
plt.figure()
for i in range(0,5):
    X=npr.uniform(size=N)
    Sbar=np.cumsum(X)/np.arange(1,N+1)
    plt.plot(np.arange(1,N+1),Sbar)
    plt.hlines(1/2,1,N,color='r',linestyles='dashed')
    plt.title('LGN uniforme')
plt.show()

#q4

N=1000
plt.figure()
for i in range(0,5):
    X=stats.cauchy.rvs(size=N)
    Sbar=np.cumsum(X)/np.arange(1,N+1)
    plt.plot(np.arange(1,N+1),Sbar)
    plt.title('LGN Cauchy')
plt.show()

## Exo 6
#q1
Nsim=1000
n=100
p=2/5
Y=np.zeros(Nsim)
for i in range(0,Nsim):
    X=npr.binomial(1,p,size=n)
    Y[i]=(sum(X)/n-p)*np.sqrt(n)/np.sqrt(p*(1-p))
Ys=sorted(Y)
x=np.linspace(min(Y),max(Y),num=100)
plt.figure()
plt.step(Ys,np.arange(1,N+1)/N,color='r',where='post')
plt.plot(x,stats.norm.cdf(x))
plt.title('TCL Bernoulli')
plt.show()

#q2
l=2
Y=np.zeros(Nsim)
for i in range(0,Nsim):
    X=npr.poisson(l,size=n)
    Y[i]=(sum(X)/n-l)*np.sqrt(n)/np.sqrt(l)
Ys=sorted(Y)
x=np.linspace(min(Y),max(Y),num=100)
plt.figure()
plt.step(Ys,np.arange(1,N+1)/N,color='r',where='post')
plt.plot(x,stats.norm.cdf(x))
plt.title('TCL Poisson de paramètre lambda='+str(l))
plt.show()


l=0.01
Y=np.zeros(Nsim)
for i in range(0,Nsim):
    X=npr.poisson(l,size=n)
    Y[i]=(sum(X)/n-l)*np.sqrt(n)/np.sqrt(l)
Ys=sorted(Y)
x=np.linspace(min(Y),max(Y),num=100)
plt.figure()
plt.step(Ys,np.arange(1,N+1)/N,color='r',where='post')
plt.plot(x,stats.norm.cdf(x))
plt.title('TCL Poisson de paramètre lambda='+str(l))
plt.show()

#q3

Y=np.zeros(Nsim)
for i in range(0,Nsim):
    X=npr.uniform(size=n)
    Y[i]=(sum(X)/n-1/2)*np.sqrt(n)/np.sqrt(1/12)
Ys=sorted(Y)
x=np.linspace(min(Y),max(Y),num=100)
plt.figure()
plt.step(Ys,np.arange(1,N+1)/N,color='r',where='post')
plt.plot(x,stats.norm.cdf(x))
plt.title('TCL uniformes')
plt.show()
