from math import *
def Frequences(cad):
    dict_to_ret = {}

    for letter in cad:
        if letter not in dict_to_ret:
            dict_to_ret[letter] = 1

        else:
            dict_to_ret[letter] = dict_to_ret[letter] + 1

    return dict_to_ret

def mk_dct(message):
    dict_actual = Frequences(message)

    for dictionary_key, dictionary_value in dict_actual.items():
        dict_actual[dictionary_key] = dictionary_value / len(message)

    return dict_actual

def Entropy(S):
    entr = 0
    for i in (S):
        logarithm = -(i * log2(i))
        entr = entr + logarithm

    return entr

message = 'A_MAN_A_PLAN_A_CANAL_PANAMA'
dict_is = mk_dct(message)
probabilities_of_a_messages = (list(dict_is.values()))
entropy_of_message = Entropy(probabilities_of_a_messages)
print(entropy_of_message)