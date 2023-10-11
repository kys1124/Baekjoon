import heapq
N, M = map(int, input().split())
s,e = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    h1,h2,k = map(int, input().split())
    adj[h1].append((h2,-k))
    adj[h2].append((h1,-k))

def dijkstra():
    pq = [(-1000000, s)]
    v = [100000]*(N+1)
    while pq:
        cw, cur = heapq.heappop(pq)
        if cur ==e:
            return -cw

        for nxt, nw in adj[cur]:
            if v[nxt]>max(cw,nw):
                v[nxt] = max(nw,cw)
                heapq.heappush(pq, (max(nw,cw), nxt))
    return 0
print(dijkstra())