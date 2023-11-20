import heapq
def prim():
    pq = [(0, 1)]
    heapq.heapify(pq)
    v = set()
    ans = 0
    mx = 0
    while pq:
        cost, cur = heapq.heappop(pq)
        if cur in v:
            continue
        ans += cost
        mx = max(mx, cost)
        v.add(cur)
        if len(v) == N:
            return ans-mx
        for nxt, nxt_cost in adj[cur]:
            if nxt not in v:
                heapq.heappush(pq, (nxt_cost, nxt))

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int, input().split())

    adj[A].append((B,C))
    adj[B].append((A, C))

print(prim())
