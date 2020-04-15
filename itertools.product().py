a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
from itertools import product

print(*product(a,b))