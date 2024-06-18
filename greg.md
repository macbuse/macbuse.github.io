 Today I am in Singapore with Alan Reid. We are working on the next version of the book Knots and Physics. Alan is a mathematician and I am a physicist. We are both interested in the mathematics of knots and how they can be used to describe the physical world. The subject goes back to the 19th century when Lord Kelvin proposed that atoms were knots in the ether. This idea was later abandoned when it was discovered that atoms were not knots but rather point particles. However, the idea of using knots to describe the physical world has persisted and has found applications in many areas of physics and mathematics. In our book, we explore the connections between knots and physics and show how they can be used to describe a wide range of physical phenomena. We hope that our book will be of interest to both mathematicians and physicists and that it will inspire others to explore the connections between knots and physics.

If our book is unsuccesful we will have to find other ways to make a living. I have been thinking about becoming a teacher. I have always enjoyed teaching and I think that I would be good at it. I have a lot of experience in the field of physics and I think that I could make a valuable contribution to the education of young people. I have also been thinking about starting my own business. I have some ideas for products that I think could be successful and I think that I have the skills and experience to make them a reality. Whatever happens, I am confident that I will find a way to make a living and continue to pursue my interests in physics and mathematics. 
```

def torus_knot(p,q):
    def torus_knot_curve(t):
        x = (2 + cos(q*t))*cos(p*t)
        y = (2 + cos(q*t))*sin(p*t)
        z = sin(q*t)
        return (x,y,z)
    return torus_knot_curve


import numpy as np
import matplotlib.pyplot as plt


def plot_torus_knot(p,q):
    torus_knot_curve = torus_knot(p,q)
    curve = [torus_knot_curve(t) for t in np.linspace(0,2*np.pi,100)]
    x,y,z = zip(*curve)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x,y,z)
    plt.show()


def knot_diagram(p,q):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    ax.plot([-3,3],[0,0],'k')
    ax.plot([0,0],[-3,3],'k')
    for t in np.linspace(0,2*np.pi,100):
        x,y,_ = torus_knot(p,q)(t)
        ax.plot(x,y,'ko')
    plt.show()




