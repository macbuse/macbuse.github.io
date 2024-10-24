# Introduction

Python avec JuPyteR (un peu comme Maple)

- numpy
- matplotlib
- pandas
- scipy

## Exemples


- [gravitational waves](https://blog.jupyter.org/congratulations-to-the-ligo-and-virgo-collaborations-from-project-jupyter-5923247be019)
- [LHC particle physics](https://cds.cern.ch/record/2687389/files/CERN_SUM_PJ_report_Yixin.pdf)

## Principe de ce cours

Beaucoup de lecture de code **mais** peu d'ecriture.

- google
- github
- youtube
- arxive

Donc pas un cours "classique" comme : 
[cours de Luc](https://membres-ljk.imag.fr/Luc.Biard/L3MI_TP/){:target="_blank}


---

## Exemple

[facemorphing](./face_morph.html)

<iframe width="560" height="315" src="https://www.youtube.com/embed/6JuWjTWp9bo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## Syllabus

- matrices, algèbre linéaire et numpy
- graphes de fonctions et images avec matplotlib
- arbres, fractals et recursion
- applications affines
- (marches) aléatoire, valeurs propres et graphes
- convolutions et scipy
- statistiques avec pandas (COVID)
- webcrawling/PageRank avec requests
- regression linéaire et logistique (reconnaissance de caractères)

## Séances

- une vidéo à regarder ou un texte à lire avant
- eventuellement un "truc" à installer
- une [fiche](./regression_copy.html)
- des exos sur la fiche

## Evaluation sur projet

[projects](./projects.html){:target="_blank"}

### Exemples

- [sudoko](./Sarah_Depernet.html){:target="_blank"}
- [labrinthe](./ProjetLabyrinthe-AlleyssonMathis.html){:target="_blank"}




---

## Installing Anaconda

We will be using [Anaconda](https://www.anaconda.com/)
because it is convenient and it is really **industry standard** for doing
DataScience. It comes with JuPyTer, Numpy, Matplotlib, Pandas.

You can follow the instructions on [this
page](https://docs.anaconda.com/anaconda/install/)
to install Anaconda on your machine.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pVME6JvdD5g" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Google Colab

If Anaconda installation doesn't work then sign up for an account to [Google
Colab](https://colab.research.google.com/). To use this service you will have to
be connected to the internet all the time. 

It is a **good idea** to sign up for this now because Colab is configured for
using GPUs and works well with Deep Learning packages ie Keras/Tensorflow.

<iframe width="560" height="315"
src="https://www.youtube.com/embed/rlSnUXnd5xE" frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen></iframe>


[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) 
- is a web-based interactive development environment for Jupyter notebooks, code, and data. 
- is flexible: configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning. 
- is a javascript **front end** running in my browser that interfaces with different **kernels**.

I use Linux/OS X and usually start JuPyteR from a terminal

``` jupyter lab```

Lab is a version of JuPyteR scheduled to replace ```jupyter notebooks```
but there are still some bugs (in particular when using interactive widgets).

When I run ```jupyter lab``` 
this appears in the navigator:

![img](jlab.png)

The **kernel sessions** list on the left are recent projects that are automatically opened. On the right there is a window with an open project TTS.ipynb. The file format [ipynb](https://fileinfo.com/extension/ipynb) stands for [Iron Python](https://ironpython.net/) Notebook. If you know about these things then it is really a [json](https://www.json.org/json-en.html) file.

You can open a new notebook from the ```File``` menu.

![img](jlab2.png)

The blank retangle is
a [code cell](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
- you can write python code here and execute it with ```shft-enter```.

There are 2 other kinds of cell
- Markdown for formatted text and math formulas.
- Raw

You can change the cell type from the menu:

![img](jlab3.png)


## Notebooks 

You should read this 
 [tutorial for biomaths](https://python.sdv.univ-paris-diderot.fr/18_jupyter/)
 to get an idea of how notebooks work.

Lots of people use notebooks for swapping and explaining results : 
- [data
science](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/jupyter-notebook/)
- [gravitational waves](https://blog.jupyter.org/congratulations-to-the-ligo-and-virgo-collaborations-from-project-jupyter-5923247be019)
- [LHC particle physics](https://cds.cern.ch/record/2687389/files/CERN_SUM_PJ_report_Yixin.pdf)



## Further reading

### Python Idioms

Watch the first part about collections and functions.

Here are the 
[slides](https://files.speakerdeck.com/presentations/c56b00e084950130ac8e22000a1c4bc5/BeautifulCode.pdf) in english. The code is Python 2 - so if you want it to work remember that in Python 3 ```print``` is a function!


<iframe width="560" height="315" src="https://www.youtube.com/embed/anrOzOapJ2E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### Markdown

Read about Markdown [in english](https://daringfireball.net/projects/markdown/syntax) and
[in french](https://blog.wax-o.com/2014/04/tutoriel-un-guide-pour-bien-commencer-avec-markdown/).

<iframe width="560" height="315" src="https://www.youtube.com/embed/6hikjzymd0c" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



