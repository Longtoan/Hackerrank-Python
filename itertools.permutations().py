string,k = input().split()
from itertools import permutations

perlist = list(permutations(sorted(string),int(k)))
for i in perlist:
    print("".join(i))