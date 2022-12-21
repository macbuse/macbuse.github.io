 import numpy as np


def row_reduce(M):
     '''Row reduce a matrix M'''
     M = M.astype(float)
     for i in range(M.shape[0]):
         # Find the pivot
         pivot = np.argmax(np.abs(M[i:, i])) + i
         # Swap rows
         M[[i, pivot]] = M[[pivot, i]]
         # Divide by pivot
         M[i] /= M[i, i]
         # Subtract from all other rows
         for j in range(M.shape[0]):
             if j != i:
                 M[j] -= M[i] * M[j, i]
     return M


def gcd_list(l):
     '''Find the greatest common divisor of a list of numbers'''
     if len(l) == 1:
         return l[0]
     else:
         return np.gcd(l[0], gcd_list(l[1:]))


def egcd_list(l):
     '''Find the greatest common divisor of a list of numbers'''
     if len(l) == 1:
         return l[0]
     else:
         return np.gcd(l[0], egcd_list(l[1:]))

def egcd(a, b):
     '''Extended Euclidean algorithm'''
     if a == 0:
         return (b, 0, 1)
     else:
         g, y, x = egcd(b % a, a)
         return (g, x - (b // a) * y, y)


