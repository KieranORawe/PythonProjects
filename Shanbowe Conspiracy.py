stuff = ["s","h","a","n","b","o","w","e"]

import random
import itertools

perm = itertools.permutations(stuff)
lists = []
for i in list(perm):
    lists.append("".join(i))
f = open("Names.txt", "a")
f.write(str(lists))
f.close()
print("done")