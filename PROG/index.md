# Introduction

I suppose you know how to ask Google to translate this page in french - I have
an qwerty keyboard and accents are impossible.

I have COVID till 25/9 so the first class will be just preparation for what we
will do then.
I won't be using the Moodle page so much 
as it is not easy to update unlike GitHub.
You will be learning how to use GitHub later -
it's quite easy.

Please watch the videos. 
You can learn a lot from them.
There will not be so much reading but there will be a lot of watching. 
To begin with the videos will be mostly in french but some subjects are only really explained well in english. 

### Friday 18/9

Here is the [first notebook](./lists.ipynb) I've prepared - you should go
through it once you have installed JuPyTer (see below).

---
### Friday 25/9

Here is the [second notebook](./numpy_intro.ipynb).
There are some difficult things in it 
mainly about matrices.

Watch these videos before starting:

<iframe width="560" height="315" src="https://www.youtube.com/embed/NzDQTrqsxas" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/vw4u9uBFFqU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
### Friday 9/10

I'm still off sick.

Here is the [preliminary version of the notebook](./matplotlib.ipynb) to study
for Friday 16/10.

Watch this video about [Matplotlib](https://matplotlib.org/)
first.

<iframe width="560" height="315" src="https://www.youtube.com/embed/O_OeWxpnUc0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
### Friday 16/10

Here is the [notebook](./matplotlib.ipynb) to study
---

### Friday 23/10

Here is the [notebook](./matplotlib_episode_two.ipynb) to study.
---

### Friday 06/11

Here is a [notebook](./matplotlib_episode_two_corr.ipynb) 
with solutions to last week's exercises

And this is the [notebook](./affine_maps.ipynb) to study for this week.

If you are having problems with the basics then try [this
notebook](./basic_python.ipynb).


### Solutions etc.

- [here](./barnsley_fern.ipynb) is a solution to drawing the fern
- I'll post the other solutions Thursday.
- I like the video that you sent me

<iframe width="560" height="315" src="https://www.youtube.com/embed/bJwJ5FFwk0U" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Friday 13/11

I wanted to do linear regression but had too much to do on convolutions.
I'll do regression and gradient descent next week.

<iframe width="560" height="315"
src="https://www.youtube.com/embed/cpltYCNLIt0" frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen></iframe>

and look at the [preliminary version](./convolutions_etc.ipynb)
of the notebook.

---
### Friday 20/11

I wanted to do linear regression but 
- we didn't finish the convolutions.
- I had some problems with my new computer.

#### Solutions to COVID

I sent a lot of time doing experiments on this

- [for France](./france.ipynb)
- [for the UK](./uk.ipynb)
- [for Scotland](./scot_covid.ipynb)


---
### Friday 27/11

I managed to delete Anaconda on my new PC 
and with it the notebook for regression.
Instead this week we'll be looking at 
a simple example of **scraping** and **crawling**

[notebook](./reg_exp.ipynb)

[my ideas](./gph2sites.ipynb)

---
### Friday 27/11

So I managed to fix the wikipedia crawler

[my ideas](./gph2sites.ipynb)

It was difficult to find a good working example for this week
but here is the 
[notebook](./regression_copy.ipynb)

There are two kinds of regression to study:
- multi variable linear regression
- logistic regression

The example of an application of logistic regression is recognising digits.
There are better ways of doing this now using CNN - maybe we can do that the
final week of term.

When the video first:

<iframe width="560" height="315" src="https://www.youtube.com/embed/BHs_2ttLRXk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


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

I have a [Kaggle](https://www.kaggle.com/) account too but I rarely use it. In theory you can follow the
course using a Kaggle account if you have one.

## Getting started

[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) 
- is a web-based interactive development environment for Jupyter notebooks, code, and data. 
- is flexible: configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning. 
- is a javascript **front end** running in my browser that interfaces with different **kernels**.

I use Linux/OS X and usually start JuPyteR from a terminal

``` jupyter lab```

Lab is a version of JuPyteR scheduled to replace ```jupyter notebooks```
but there are still some bugs (in particular when using interactive widgets).

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

You should read this 
 [tutorial for biomaths](https://python.sdv.univ-paris-diderot.fr/18_jupyter/)
 to get an idea of how notebooks work.

Lots of people use notebooks for swapping and explaining results : 
- [data
science](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/jupyter-notebook/)
- [gravitational
waves](https://blog.jupyter.org/congratulations-to-the-ligo-and-virgo-collaborations-from-project-jupyter-5923247be019)
- [LHC particle
physics](https://cds.cern.ch/record/2687389/files/CERN_SUM_PJ_report_Yixin.pdf)



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



