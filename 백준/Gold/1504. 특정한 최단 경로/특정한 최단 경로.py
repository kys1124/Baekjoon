N,E = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
v1,v2 = map(int, input().split())

import heapq

def dijkstra(s):
    q = [(0,s)]
    v = [-1]*(N+1)

    heapq.heapify(q)
    v[0]=0
    while q:
        cd, c = heapq.heappop(q)

        for n,nd in adj[c]:
            if v[n]==-1 or v[n]>=cd+nd:
                v[n]=cd+nd
                heapq.heappush(q,(cd+nd,n))

    return v
V = dijkstra(1)
D = dijkstra(v1)
R = dijkstra(v2)
if -1 in (V[v1],D[v2],R[N]) and -1 in (V[v2],R[v1],D[N]):
    print(-1)
elif -1 not in (V[v1],D[v2],R[N]) and -1 in (V[v2],R[v1],D[N]):
    print(V[v1]+D[v2]+R[N])
elif -1 not in (V[v2],R[v1],D[N]) and -1 in (V[v1],D[v2],R[N]):
    print((V[v2],R[v1],D[N]))

else:
    if v1==1 and v2==N:
        print(V[N])
    elif v1==1 and v2!=N:
        print(V[v2]+R[N])
    elif v1!=1 and v2==N:
        print(V[v1]+D[N])
    else:
        print(min(V[v2]+R[v1]+D[N], V[v1]+D[v2]+R[N]))