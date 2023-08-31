import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    adj[a].append((b,c))

import heapq

def dijkstra(s):
    q = [(0,s)]
    heapq.heapify(q)
    v = [-1]*(n)
    v[s-1]=0
    while q:
        cost, cur = heapq.heappop(q)

        for nxt,nxt_cost in adj[cur]:
            if v[nxt-1]==-1 or v[nxt-1]>=nxt_cost+cost:
                v[nxt-1]=nxt_cost+cost
                heapq.heappush(q,(v[nxt-1],nxt))
    return v


for i in range(1,n+1):
    lst = dijkstra(i)
    for i in range(n):
        if lst[i]==-1:
            lst[i]=0
    print(*lst)