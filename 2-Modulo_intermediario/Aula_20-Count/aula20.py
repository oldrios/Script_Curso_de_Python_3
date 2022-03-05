'''
Count - Itertools
'''
from itertools import count

cont = count(9, -1)

for x in cont:
    print(x)

    if x >= 10 or x <= -10:
        break



