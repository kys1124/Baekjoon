N,M = map(int, input().split())
A = set([input() for _ in range(N)])
B = set([input() for _ in range(M)])
lst = sorted(list(A.intersection(B)))
print(len(lst))
for x in lst:
    print(x)