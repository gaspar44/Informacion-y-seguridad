from sympy import *
import numpy as np
from math import *

def Frequences(cad):
    dict_to_ret = {}

    for letter in cad:
        if letter not in dict_to_ret:
            dict_to_ret[letter] = 1
        
        else:
            dict_to_ret[letter] = dict_to_ret[letter] + 1
    
    return dict_to_ret


def Entropy(S):
    entr = 0
    for i in (S):
        logarithm = -(i * log2(i))
        entr = entr + logarithm
    
    return entr

def Probability(cad):
    frequences = Frequences(cad)
    letters = np.array(list(frequences.values()))
    letters = letters * 1/len(cad)
    return list(frequences.keys()), letters

def AddPrimes(n):
    if n < 0:
        return 0
    sum = 0
    numbers_added = 1
    number_to_calculate_next_prime = 0

    while numbers_added != n + 1:
        number_to_calculate_next_prime = nextprime(number_to_calculate_next_prime)
        sum = sum + number_to_calculate_next_prime
        numbers_added = numbers_added + 1

    return sum

def ProbInStr(cad,carac):
    probability = Probability(cad)
    car = probability[0]
    probability_to_look_after = probability[1]
    p=0
    for x,y in zip(car,probability_to_look_after):
        if x == carac:
            p = y
    return p 

values = [2/5,3/5]
print(Probability("abcc"))