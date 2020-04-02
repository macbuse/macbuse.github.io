---
layout: page
title: Contact Page
---

# Viral Proteins

This is a very badly organised collection 
of correspondences from  [Bob
Penner](https://www.ihes.fr/en/professeur/robert-c-penner-2/).
This is an **early version** of the 
[current paper](virusforalexeii.pdf)
 which will be published shortly in the
Jounal of Computational Biology. The galley proofs are somewhere in my mail.

## statement of problem

Bob has written down what he thinks the 
problem is in this [document](problem.pdf)

## some data

I've uploaded a the data from [6vsb](https://www.rcsb.org/3d-view/6VSB) which
What we are interested in is finding unusual features in the protein chains
which might be good targets for a synthetic vaccine. Bob has a scheme based on
chain the statistics of the hydrogen bonds. Look in the 
[article](virusforalexeii.pdf)
 - at least the introduction for an explanation.

If you want to look at some of the *raw data* 
it's [here](6vsb/6vsb_merged_stress_density_full_graph.csv). The 6vsb is a PDB
file for the spike protein
- there are 3 chains A,B,C
- bonds are numbered according to where they lie in a chain
- there is a number = density/free energy between 0 and 10
- 10 is better because it means it's rarer.

We have lots of these files - and there will
shortly be many, many more because of the current crisis.

---

## a word about the numbers

The numbers are computed from some statistics/density
which is explained in [this paper](ncomms6803.pdf).
The original numbers are a measure of bending along the backbone 
and the densities measure how exotic a particular local configuration is.
Here is the abstract:

*Proteins fold into three-dimensional structures, which determine their diverse
functions. The conformation of the backbone of each structure is locally at each Ca
effectively described by conformational angles resulting in Ramachandran plots. These, however, do not
describe the
conformations around hydrogen bonds, which can be non-local along the backbone
and are of
major importance for protein structure. Here, we introduce the spatial rotation
between
hydrogen bonded peptide planes as a new descriptor for protein structure
locally around a
hydrogen bond. Strikingly, this rotational descriptor sampled over high-quality
structures from
the protein data base (PDB) concentrates into 30 localized clusters, some of
which correlate
to the common secondary structures and others to more special motifs, yet
generally providing a unifying systematic classification of local structure
around protein hydrogen bonds. It
further provides a uniform vocabulary for comparison of protein structure near
hydrogen
bonds even between bonds in different proteins without alignment.*

---

## Recommended reading

- [Finkelstein's book](2016_finkelstein.pdf)
- [Hydrogen bond in Nature communications](ncomms6803.pdf)
