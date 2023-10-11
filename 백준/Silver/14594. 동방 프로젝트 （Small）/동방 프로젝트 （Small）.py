N = int(input())
M = int(input())
p = [i for i in range(N+1)]
def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b

for _ in range(M):
    x,y = map(int, input().split())
    for i in range(x,y):
        if find(i)!=find(i+1):
            union(i,i+1)

sm = 0
for i in range(1,N+1):
    if p[i]==i:
        sm+=1
print(sm)