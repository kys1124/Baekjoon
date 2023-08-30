from collections import defaultdict
N ,M = map(int, input().split())
book = defaultdict(str)
for i in range(N):
    name = input()
    book[str(i+1)] = name
    book[name] = str(i+1)
Q = [input() for _ in range(M)]


for x in Q:
    print(book[x])