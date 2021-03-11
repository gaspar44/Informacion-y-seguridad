from math import *

def Entropy(S):
    entr = 0
    for i in (S):
        logarithm = -(i * log2(i))
        entr = entr + logarithm

    return entr
