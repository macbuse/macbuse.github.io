import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import scipy.stats as stats
import math


## Exo 1
r=1
b=1
N=1000
plt.figure()
for i in range(0,5):
    urne=np.concatenate((np.ones(r),np.zeros(b)))
    X=np.zeros(N)
    for i in range(0,N):
        I=np.array([npr.choice(urne)])
        urne=np.concatenate((urne,I))
        X[i]=np.mean(urne)
    plt.plot(np.arange(1,N+1),X)
plt.title('Urne de Polya pour r= '+str(r) + ' et b= ' + str(b))
plt.show()
# Il semble bien que la proportion converge, mais vers une limite aléatoire
Nsim=1000
N=100
r=1
b=1
Y=np.zeros(Nsim)
for i in range(0,Nsim):
    urne=np.concatenate((np.ones(r),np.zeros(b)))
    for j in range(0,N):
        I=np.array([npr.choice(urne)])
        urne=np.concatenate((urne,I))
    Y[i]=np.mean(urne)
Ys=sorted(Y)
x=np.linspace(min(Y),max(Y),num=100)
plt.figure()
plt.step(Ys,np.arange(1,Nsim+1)/Nsim,color='r',where='post')
plt.plot(x,stats.beta(r,b).cdf(x))
plt.title('Convergence en loi de la proportion dans une urne de Polya\n  pour r= '+str(r) + ' et b= ' + str(b))
plt.show()

#
Nsim=1000
N=100
r=3
b=5
Y=np.zeros(Nsim)
for i in range(0,Nsim):
    urne=np.concatenate((np.ones(r),np.zeros(b)))
    for j in range(0,N):
        I=np.array([npr.choice(urne)])
        urne=np.concatenate((urne,I))
    Y[i]=np.mean(urne)
Ys=sorted(Y)
x=np.linspace(min(Y),max(Y),num=100)
plt.figure()
plt.step(Ys,np.arange(1,Nsim+1)/Nsim,color='r',where='post')
plt.plot(x,stats.beta(r,b).cdf(x))
plt.title('Convergence en loi de la proportion dans une urne de Polya\n pour r= '+str(r) + ' et b= ' + str(b))
plt.show()

## Exo 2
#q1
def WF(x0,n,N,Nsim):
    X=x0*np.ones((Nsim,n+1))
    for i in range(0,Nsim):
        for j in range(1,n+1):
            X[i,j]=npr.binomial(N,X[i,j-1]/N)
    return X


Nsim=20
N=5
x0=2
n=80
X=WF(x0,n,N,Nsim)
absc=np.arange(0,n+1)
plt.figure()
plt.plot(absc,X.T)
plt.title('Trajectoires pour N='+str(N))
plt.show()

N=10
x0=5
n=80
X=WF(x0,n,N,Nsim)
absc=np.arange(0,n+1)
plt.figure()
plt.plot(absc,X.T)
plt.title('Trajectoires pour N='+str(N))
plt.show()


N=30
x0=10
n=80
X=WF(x0,n,N,Nsim)
absc=np.arange(0,n+1)
plt.figure()
plt.plot(absc,X.T)
plt.title('Trajectoires pour N='+str(N))
plt.show()

# q2
Nsim=1000
N=10
def WFabs(x0,N,Nsim):
    XX=np.zeros(Nsim)
    for i in range(0,Nsim):
        X=x0
        while X!=0 and X!=N:
            X=npr.binomial(N,X/N)
        XX[i]=X==N
    return np.mean(XX)
p=np.zeros(N+1)
for x0 in np.arange(0,N+1):
        p[x0]=WFabs(x0,N,Nsim)
plt.figure()
absc=np.arange(0,N+1)
plt.plot(absc,p,label='estimation')
plt.plot(absc,p+1.96*np.sqrt(p*(1-p))/np.sqrt(Nsim),'--g')
plt.plot(absc,p-1.96*np.sqrt(p*(1-p))/np.sqrt(Nsim),'--g')
plt.plot(absc,absc/N,'r',label='theorique')
plt.xlabel('x0')
plt.title('Estimation de P_X0(X_T=N) pour N='+str(N)+' et Nsim='+str(Nsim))
plt.legend()
plt.show()

#q3

Nsim=1000
N=20
def WFtps(x0,N,Nsim):
    TT=np.zeros(Nsim)
    for i in range(0,Nsim):
        X=x0
        t=0
        while X!=0 and X!=N:
            X=npr.binomial(N,X/N)
            t=t+1
        TT[i]=t
    return [np.mean(TT),np.std(TT)]
tps=np.zeros(N+1)
s=np.zeros(N+1)
for x0 in np.arange(0,N+1):
    a=WFtps(x0,N,Nsim)
    tps[x0]=a[0]
    s[x0]=a[1]
plt.figure()
absc=np.arange(0,N+1)
plt.plot(absc,tps)
plt.plot(absc,tps+1.96*s/np.sqrt(Nsim),'--g')
plt.plot(absc,tps-1.96*s/np.sqrt(Nsim),'--g')
plt.xlabel('x0')
plt.title('Estimation de E_X0(T) pour N='+str(N)+' et Nsim='+str(Nsim))
plt.show()