import sys
input = sys.stdin.readline

n,m = map(int, input().split())

m_map = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if m_map[i][j]==2:
            ei,ej = i, j

from collections import deque

def bfs(si,sj):
    q = deque([(si,sj)])
    visited = [[0]*m for _ in range(n)]
    visited[si][sj]=1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj]==0 and m_map[ni][nj]!=0:
                visited[ni][nj]=visited[ci][cj]+1
                q.append((ni,nj))            

    return visited

v = bfs(ei,ej)
for i in range(n):
    for j in range(m):
        if m_map[i][j]==1 and v[i][j]==0:
            v[i][j]=-1
        elif v[i][j]>0:
            v[i][j]-=1

for x in v:
    print(*x)