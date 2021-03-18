from img_1 import *
import Huffman2
import IWT


def compression_ratio(original_size, new_size):
    div = new_size / original_size
    return 100 * (1 - div)


dict_prob, entropy = IWT.img_info(img_1)
encoded_by_huffman_dict, average_word_len = Huffman2.huffman2(dict_prob)
original_bits_needed_for_image = 8
original_compression_ratio = compression_ratio(original_bits_needed_for_image, average_word_len)

dict_pro_iwt, entropy_iwt = IWT.iwt(img_1, 1)
encoded_by_huffman_dict_iwt, average_word_len_iwt = Huffman2.huffman2(dict_pro_iwt)
#print("Entropy: " + str(entropy))

#print("Compression ratio: " + str(original_compression_ratio))

iwt_compression_ratio = compression_ratio(original_bits_needed_for_image, average_word_len_iwt)
#print("Entropy IWT: " + str(entropy_iwt))
#print("IWT Average: " + str(average_word_len_iwt))
#print("IWT Compression ratio: " + str(iwt_compression_ratio))


img_2 = img_1 + 20
dict_prob2, _ = IWT.img_info(img_2)
encoded_by_huffman_dict2, average_word_len2 = Huffman2.huffman2(dict_prob2)
print(img_1.max())
print(img_2.max())
print("Original Aqverage: " + str(average_word_len))
print("Average 2: " + str(average_word_len2))
