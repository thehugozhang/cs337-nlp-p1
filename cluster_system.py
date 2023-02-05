from fuzzywuzzy import fuzz

Str_A = 'Daniel Day Lewis' 
Str_B = 'Daniel Day-Lewis'
ratio = fuzz.partial_ratio(Str_A.lower(), Str_B.lower())


print('Similarity score: {}'.format(ratio))

def cluster_results_by_similarity:
    