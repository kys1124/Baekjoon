N = int(input())

S = set([str(i) for i in range(666,3000000)])
lst = []
for x in S:
    if '666' in x:
        lst.append(int(x))

lst.sort()
print(lst[N-1])
