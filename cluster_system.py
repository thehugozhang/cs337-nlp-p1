from fuzzywuzzy import fuzz

Str_A = 'Daniel Day Lewis' 
Str_B = 'Daniel Day-Lewis'
ratio = fuzz.partial_ratio(Str_A.lower(), Str_B.lower())


print('Similarity score: {}'.format(ratio))

import re

string = 'This is laughing laugh'

a = re.search(r'\b(lsdugh)\b', string)
print(a)
print(a.start())


