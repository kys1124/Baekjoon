import sys
input = sys.stdin.readline


n,m = map(int,input().split())
p = [i for i in range(n+1)]

def find(x):
    if p[x]==x:
        return p[x]

    p[x] = find(p[x])
    return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    p[b] = a

for _ in range(m):
    num, a, b = map(int, input().split())
    if num==0:
        union(a,b)

    else:
        if find(a)==find(b):
            print('yes')
        else:
            print('no')
