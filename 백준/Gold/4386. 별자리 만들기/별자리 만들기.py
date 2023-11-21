import heapq
N = int(input())
adj = [[] for _ in range(N)]
point = []
for _ in range(N):
    x,y= map(float, input().split())
    point.append((x,y))

for i in range(N-1):
    for j in range(i+1, N):
        x1,y1 = point[i]
        x2,y2 = point[j]
        dist = ((x1-x2)**2+(y1-y2)**2)**(0.5)
        adj[i].append((j,dist))
        adj[j].append((i,dist))

def prim():
    pq =[(0,0)]
    heapq.heapify(pq)
    S = set()
    ans  =0
    while pq:
        dist, cur = heapq.heappop(pq)
        if cur in S:
            continue
        S.add(cur)
        ans+=dist
        if len(S)==N:
            return ans

        for nxt, nxt_dist in adj[cur]:
            if nxt not in S:
                heapq.heappush(pq, (nxt_dist, nxt))
print(round(prim(),2))