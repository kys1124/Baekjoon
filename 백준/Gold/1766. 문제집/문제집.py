N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for _ in range(M):
    a,b = map(int, input().split())
    degree[b]+=1
    adj[a].append(b)

import heapq
q = []
for i in range(1,N+1):
    if degree[i]==0:
        q.append(i)
ans = []
heapq.heapify(q)
while q:
    cur = heapq.heappop(q)
    ans.append(cur)
    for nxt in adj[cur]:
        degree[nxt]-=1
        if degree[nxt]==0:
            heapq.heappush(q, nxt)
print(*ans)