# Introduction

I have COVID till 25/9 so the first class will be just preparation for what we
will do then.
I won't be using the Moodle page much 
as it is not easy to update unlike GitHub.

Please watch the videos there will not be so much reading but there will be a lot of watching. 
You can learn a lot from them.
To begin with the videos will be mostly in french but some subjects are only really explained well in english. 

I suppose you know how to ask Google to translate this page in french.

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

## Kaggle

J'ai un compte Kaggle aussi mais j'utilise rarement. Si vous en avaz un déjà
c'est bien.

## Getting started

I use Linux/OS X and usually start JuPyteR from a terminal

``` jupyter lab```

Lab is a version of JuPyteR scheduled to replace ```jupyter notebooks```
but there are still some bugs (in particular when using interactive widgets).

JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning. JupyterLab is a javascript **front end** running in my browser that interfaces with different **kernels**.

When I run ``` jupyter lab``` this appears in the navigator:

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

Lots of people use notebooks.

- [tutorial for biomaths](https://python.sdv.univ-paris-diderot.fr/18_jupyter/)
- [data
science](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/jupyter-notebook/)
- [gravitational
waves](https://blog.jupyter.org/congratulations-to-the-ligo-and-virgo-collaborations-from-project-jupyter-5923247be019)
- [LHC particle
physics](https://cds.cern.ch/record/2687389/files/CERN_SUM_PJ_report_Yixin.pdf)


## Further reading

Read about [Markdown](https://daringfireball.net/projects/markdown/syntax)

<iframe width="560" height="315" src="https://www.youtube.com/embed/6hikjzymd0c" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Watch some videos about [Matplotlib](https://matplotlib.org/)


<iframe width="560" height="315" src="https://www.youtube.com/embed/O_OeWxpnUc0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
