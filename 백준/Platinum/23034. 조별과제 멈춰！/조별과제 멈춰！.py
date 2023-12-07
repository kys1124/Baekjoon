import sys
import heapq
N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def prim():
    v = set()
    mst = [[] for _ in range(N+1)]
    pq = [(0,1,0)]
    while pq:
        dist, cur, pre = heapq.heappop(pq)

        if cur in v:
            continue
        v.add(cur)
        if pre!=0:
            mst[cur].append((pre,dist))
            mst[pre].append((cur,dist))

        if len(v)==N:
            return mst

        for nxt, nxt_dist in adj[cur]:
            if nxt not in v:
                heapq.heappush(pq, (nxt_dist,nxt,cur))

mst = prim()
def bfs(x,y):
    q = [(0,x),(0,y)]
    v = [0]*(N+1)
    heapq.heapify(q)
    cnt= 0
    total = 0
    while q:
        cost, cur = heapq.heappop(q)
        if v[cur]==1:
            continue
        v[cur]=1
        cnt+=1
        total+=cost

        if cnt==N:
            return total
        for nxt,nxt_cost in mst[cur]:
            if v[nxt]==0:
                heapq.heappush(q,(nxt_cost,nxt))

for _ in range(int(input())):
    x,y = map(int, input().split())
    print(bfs(x,y))