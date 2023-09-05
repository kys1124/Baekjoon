n,m,r = map(int, input().split())
t = [0]+list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int, input().split())
    arr[a].append((b,l))
    arr[b].append((a,l))

import heapq
INF = 100*100
def dijkstra(s):
    q = [(0,s)]
    v = [INF]*(n+1)
    v[s]=0
    heapq.heapify(q)
    cnt = 0
    while q:
        cur_dist, cur = heapq.heappop(q)

        for nxt, nxt_dist in arr[cur]:
            if v[nxt]>=cur_dist+nxt_dist:
                v[nxt] = cur_dist+nxt_dist
                heapq.heappush(q, (v[nxt], nxt))

    for x in range(1, n+1):
        if v[x]<=m:
            cnt +=t[x]

    return cnt

ans = 0
for i in range(1,n+1):
    ans = max(ans, dijkstra(i))
print(ans)

