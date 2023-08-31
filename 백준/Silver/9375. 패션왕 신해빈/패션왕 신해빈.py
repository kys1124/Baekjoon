T = int(input())
from collections import defaultdict

for _ in range(T):
    n = int(input())
    cloth = defaultdict(int)
    for _ in range(n):
        _,b = input().split()
        cloth[b] +=1

    sm = 1
    for value in cloth.values():
        sm*=(value+1)
    print(sm-1)

