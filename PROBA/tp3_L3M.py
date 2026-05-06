import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat


## Exo 1
c=np.loadtxt("../donnees/circ.txt")
h=np.loadtxt("../donnees/h.txt")
plt.figure()
plt.title('Eucalyptus')
plt.xlabel('Circonférence')
plt.ylabel('Hauteur')
plt.plot(c,h,'bx')
mc=np.mean(c)
mh=np.mean(h)
a=np.mean((c-mc)*(h-mh))/np.mean((c-mc)*(c-mc))
b=mh-mc*a
x=np.linspace(min(c),max(c),100)
y=x*a+b
plt.plot(x,y,'r')
b1=np.quantile(h-a*c,.1)
b2=np.quantile(h-a*c,.9)
plt.plot(c,a*c+b1,'g')
plt.plot(c,a*c+b2,'g')
plt.show()
hpred=a*c+b
r=np.mean((h-mh)*hpred)/np.sqrt(np.mean((h-mh)**2)*np.mean((hpred-mh)**2))
print('Correlation entre la hauteur et son ajustement affine: ',r)
R=np.mean((h-mh)*(c-mc))/np.sqrt(np.mean((h-mh)**2)*np.mean((c-mc)**2))
print('Correlation entre la hauteur et son ajustement affine: ',R)
print('Angle en degrés entre y recentré et x recentré',np.arccos(R)*180/np.pi)

## Exo 2
n1=12
n2=12
n=n1+n2
alpha=.05
muAchap=4.8
sAchap=0.36
muBchap=5.7
sBchap=0.4
schap=np.sqrt(1/(n-2)*((n1-1)*sAchap**2+(n2-1)*sBchap**2))
q=stat.t.ppf(1-alpha/2,n-2)
eps=np.sqrt((1/n1+1/n2))*schap
print(']',muAchap-muBchap-q*eps,';',muAchap-muBchap+q*eps,'[')


## Exo 3

alpha=.05
q=stat.norm.ppf(1-alpha/2)
i=1
plt.figure()
for n in [30,100,1000]:
    p=np.linspace(5/n,1/2,20)
    P1=stat.binom(n,p).cdf(np.floor(n*p+q/2*np.sqrt(n)))-stat.binom(n,p).cdf(np.ceil(n*p-q/2*np.sqrt(n)))
    P2=stat.binom(n,p).cdf(np.floor(n*p+np.sqrt(n)/2/np.sqrt(alpha)))-stat.binom(n,p).cdf(np.ceil(n*p-np.sqrt(n)/2/np.sqrt(alpha)))
    plt.subplot(3,1,i)
    plt.plot(p,P1,'red')
    plt.plot(p,P2,'orange')
    plt.title("n="+str(n))
    plt.hlines(1-alpha,p[0],p[-1])
    i=i+1
plt.show()
