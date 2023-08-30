M,N,H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

from collections import deque

def bfs(lst):
    q = deque(lst)
    x = 0
    while q:
        ci,cj,ck =q.popleft()

        for di,dj,dk in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1)):
            ni,nj,nk = ci+di, cj+dj, ck+dk
            if 0<=ni<H and 0<=nj<N and 0<=nk<M and box[ni][nj][nk]==0 and box[ci][cj][ck]>0:
                q.append((ni,nj,nk))
                box[ni][nj][nk]=box[ci][cj][ck]+1
                x = max(x, box[ni][nj][nk]-1)
    return x

lst = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k]==1:
                lst.append((i,j,k))

ans = bfs(lst)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k]==0:
                print(-1)
                exit()
print(ans)