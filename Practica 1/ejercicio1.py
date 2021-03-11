from math import *
from huffman import *
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

def av_cwlen(huffman_dictionary,probability_dictionary):
    average_len = 0
    huffman_dictionary_keys = list(huffman_dictionary.keys()).sort()
    probability_dictionary_keys = list(probability_dictionary.keys()).sort()

    if probability_dictionary_keys != huffman_dictionary_keys:
        return


    for key, _ in huffman_dictionary.items():
        average_len = average_len + (probability_dictionary[key] * len(huffman_dictionary[key]) )

    return average_len


def Entropy(S):
    entr = 0
    for i in (S):
        logarithm = -(i * log2(i))
        entr = entr + logarithm

    return entr

message = 'A_MAN_A_PLAN_A_CANAL_PANAMA'
probability_dictionary = mk_dct(message)
huffman_dict = huffman(probability_dictionary)
#probabilities_of_a_messages = (list(dict_is.values()))
#entropy_of_message = Entropy(probabilities_of_a_messages)
print(av_cwlen(huffman_dict, probability_dictionary))