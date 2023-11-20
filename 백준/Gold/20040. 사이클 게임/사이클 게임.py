N, M = map(int, input().split())

p = [i for i in range(N)]
def find(x):
    while p[x]!=x:
        x = p[x]
    return x

def union(a,b):
    a= find(a)
    b= find(b)
    if a>b:
        p[a]=b
    else:
        p[b]=a

ans = 0
for k in range(1,M+1):
    a,b = map(int, input().split())
    if find(a)==find(b):
        ans=k
        break
    else:
        union(a,b)
print(ans)