import sys
input = sys.stdin.readline

def union(a,b):
    a= find(a)
    b=find(b)
    p[b]=a

def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]

import heapq

def kruskal():
    global ans
    q = [(0,1)]
    idx = 0
    while q:
        d,c = heapq.heappop(q)
        if find(idx)!=find(c):
            union(idx,c)
            ans +=d
        else:
            continue
            
        for n, dist in adj[c]:
            if find(n)!=find(c):
                heapq.heappush(q,(dist,n))
        idx =c



V,E = map(int, input().split())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    A,B,C = map(int, input().split())
    adj[A].append((B,C))
    adj[B].append((A,C))

p = [i for i in range(V+1)]
ans = 0
kruskal()
print(ans)
