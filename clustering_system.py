"""

Clustering system.

"""

__version__ = '1.0'
__author__ = 'Peter Sheldon'

from fuzzywuzzy import fuzz

# dict = {"Quentin": 2, "Quentin Tarantino": 4, "Ben": 1, "Affleck": 5, "Leto": 4, "Wells": 1, "Les Mis": 1}
# def merge_lastnames(dict):
#     retdict= dict
#     currdict = list(dict.keys())
#     print(currdict)
#     i = 1
#     j = 0
#     while i < len(currdict):
#         while j < len(currdict):
#             print(currdict[i])
#             if (currdict[i]).__contains__(currdict[j]):
#                 currdict.remove(currdict[j])
#                 retdict[i] = retdict.get(currdict[i]) + retdict.get(currdict[j])
#             j = j + 1
#         i = i + 1  
#     return retdict

#using fuzzy import
def clustering(dictionary):
    unique_keys = {}
    for key in dictionary:
        highest_score = 0
        closest_match = None
        for unique_key in unique_keys:
            score = fuzz.token_set_ratio(key, unique_key)
            if score > highest_score:
                closest_match = unique_key
                highest_score = score
        if highest_score >= 57:
            unique_keys[closest_match] += dictionary[key]
        else:
            unique_keys[key] = dictionary[key]
    return unique_keys

    