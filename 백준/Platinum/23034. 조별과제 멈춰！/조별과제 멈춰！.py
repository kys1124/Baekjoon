import heapq
from collections import deque
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
    total  = 0
    while pq:
        dist, cur, pre = heapq.heappop(pq)

        if cur in v:
            continue
        v.add(cur)
        total+= dist
        if pre!=0:
            mst[cur].append((pre,dist))
            mst[pre].append((cur,dist))

        if len(v)==N:
            return mst, total

        for nxt, nxt_dist in adj[cur]:
            if nxt not in v:
                heapq.heappush(pq, (nxt_dist,nxt,cur))

mst,total = prim()

def bfs2(x,y):
    q = deque([(x,0)])
    v = [0]*(N+1)
    v[x]=1
    while q:
        cur,score = q.popleft()
        if cur==y:
            return score
        for nxt, nxt_cost in mst[cur]:
            if v[nxt]==0:
                v[nxt]=1
                q.append((nxt,max(score,nxt_cost)))

for _ in range(int(input())):
    x,y = map(int, input().split())
    print(total-bfs2(x,y))