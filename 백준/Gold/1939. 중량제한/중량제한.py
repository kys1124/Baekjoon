N,M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int, input().split())
    arr[A].append((B,C))
    arr[B].append((A,C))

s,e = map(int, input().split())
INF = -1000000000
v = [-INF]*(N+1)

import heapq
def dijkstra(s,e):
    q = [(INF,s)]
    heapq.heapify(q)

    while q:
        w, cur= heapq.heappop(q)
        if cur ==e:
            return -w

        for nxt, nw in arr[cur]:
         if v[nxt] > -nw:
                v[nxt] = -nw
                heapq.heappush(q, (max(-nw, w), nxt))

print(dijkstra(s,e))