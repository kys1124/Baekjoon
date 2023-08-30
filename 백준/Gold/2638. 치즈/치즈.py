N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cheese = 0
from collections import deque
def bfs():
    q = deque([(0,0)])
    v=[[0]*M for _ in range(N)]
    v[0][0]=1
    arr[0][0]=2
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(0,-1),(-1,0)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!=1:
                q.append((ni,nj))
                arr[ni][nj]=2
                v[ni][nj]=1

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            cheese+=1


t = 0
while cheese>0:
    lst = []
    bfs()
    for i in range(1,N-1):
        for j in range(1,M-1):
            if arr[i][j]==1:
                temp = 0
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni,nj = di+i, dj+j
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==2:
                        temp+=1

                    if temp>=2:
                        cheese-=1
                        lst.append((i,j))
                        break

    for ci,cj in lst:
        arr[ci][cj]=0
    t+=1
print(t)