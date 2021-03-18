# By Mark Reid,  https://gist.github.com/mreid
# Example Huffman coding implementation
# Distributions are represented as dictionaries of { 'symbol': probability }
# Codes are dictionaries too: { 'symbol': 'codeword' }

def DF_avcwl(dkt_hf, dkt_pr):
        test1 = set(dkt_hf.keys()).difference(set(dkt_pr.keys()))
        test2 = set(dkt_pr.keys()).difference(set(dkt_hf.keys()))
        #print('differences 1', test1)
        #print('differences 2', test2)
        return sum([len(dkt_hf[k])*dkt_pr[k] for k in dkt_pr.keys()])

def huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
    assert(sum(p.values()) < 1.0 + 1e-10 or sum(p.values()) < 1.0 - 1e-10) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        a1, a2 = lowest_prob_pair(p)
        return dict(zip([a1, a2], ['0', '1']))
	#return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda pz: pz[1])
    return sorted_p[0][0], sorted_p[1][0]

def huffman2(dkt_pr):
#        print(dkt_pr.keys())
        dkt_hf = huffman(dkt_pr)
        av_cw = DF_avcwl(dkt_hf, dkt_pr)
        return dkt_hf, av_cw
