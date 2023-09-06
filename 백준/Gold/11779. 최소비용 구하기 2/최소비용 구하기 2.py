import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int , input().split())
    arr[a].append((b,c))

s,e = map(int, input().split())
INF = 1000*100000
import heapq
def dijkstra(s,e):
    q = [(0,s)]
    heapq.heapify(q)
    v = [INF]*(n+1)
    v[s]=0
    path = dict()
    while q:
        cur_cost, cur = heapq.heappop(q)

        if cur ==e:
            return v[e], path

        for nxt, nxt_cost in arr[cur]:
            if v[nxt]>nxt_cost+cur_cost:
                v[nxt]=nxt_cost+cur_cost
                path[nxt]=cur
                heapq.heappush(q, (v[nxt],nxt))


cost, path = dijkstra(s,e)
ans=[e]
while e!=s:
    e=path[e]
    ans.append(e)
print(cost)
print(len(ans))
ans.reverse()
print(*ans)