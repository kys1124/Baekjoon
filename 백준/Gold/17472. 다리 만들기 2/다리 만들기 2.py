N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

V = [[0]*M for _ in range(N)]

from collections import deque

def bfs(si,sj,idx):
    q = deque([(si,sj)])
    V[si][sj]=idx

    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and V[ni][nj]==0 and arr[ni][nj]==1:
                V[ni][nj]=idx
                q.append((ni,nj))

import heapq
def prim(s):
    q = [(0,s)]
    S = set()
    heapq.heapify(q)
    total = 0
    while q:
        dist, cur = heapq.heappop(q)
        if cur in S:
            continue

        S.add(cur)
        total +=dist

        if len(S)==len(adj)-1:
            return total

        for nxt, nxtdist in adj[cur]:
            if nxt not in S:
                heapq.heappush(q, (nxtdist, nxt))

    return -1

idx = 1
for i in range(N):
    for j in range(M):
        if arr[i][j]!=0 and V[i][j]==0:
            bfs(i,j,idx)
            idx+=1

adj = [[] for _ in range(idx)] # 섬 그래프 인접리스트

# V에는 섬 별로 나누어져 있음.

for ci in range(N):
    for cj in range(M):
        if V[ci][cj]!=0:
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                mul = 1
                while True:
                    ni,nj = ci+mul*di, cj+mul*dj
                    if ni<0 or nj<0 or ni>=N or nj>=M:
                        break
                    elif V[ni][nj]==V[ci][cj]:
                        break
                    elif V[ni][nj]==0:
                        mul+=1
                    else:
                        if mul>=3:
                            adj[V[ci][cj]].append((V[ni][nj], mul-1))
                            break
                        else:
                            break


for i in range(len(adj)):
    if adj[i]:
        s=i
        t = prim(s)
        if t!=-1:
            print(t)
        else:
            print(-1)
        break
else:
    print(-1)