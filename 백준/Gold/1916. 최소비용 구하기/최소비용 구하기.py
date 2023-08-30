import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr =[[] for _ in range(N+1)]
for _ in range(M):
    u,v,d = map(int,input().split())
    arr[u-1].append((v-1,d))

s,e = map(int, input().split())
v = [float('inf')]*(N)

import heapq
def bfs():
    lst = []
    heapq.heapify(lst)
    v[s-1]=0
    lst.append((v[s-1],s-1))
    while lst:
        dist, c = heapq.heappop(lst)
        if v[c]<dist:
            continue

        for i,d in arr[c]:
            if v[c]+d<v[i]:
                v[i] = v[c]+d
                heapq.heappush(lst,(v[i],i))

bfs()
print(v[e-1])