V,E=map(int, input().split())
s = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    adj[u].append((v,w))

import heapq

def dij(s):
    v = [-1]*(V+1)
    lst = [(0,s)]
    heapq.heapify(lst)
    v[s]=0

    while lst:
        cd, cv = heapq.heappop(lst)

        for n,nd in adj[cv]:
            if v[n]==-1 or v[n]>=cd+nd:
                v[n]=cd+nd
                heapq.heappush(lst, (cd+nd,n))
    return v

v = dij(s)
for x in range(1,V+1):
    if v[x]==-1:
        print('INF')
    else:
        print(v[x])
