N,M = map(int, input().split())
arr =[list(map(int ,input().split())) for _ in range(N)]

from collections import deque

def bfs():
    q = deque([(0,0)])
    v = [[0]*M for _ in range(N)]
    v[0][0]=1
    arr[0][0]=2

    while q:
        ci,cj = q.popleft()

        for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!=1:
                v[ni][nj]=1
                arr[ni][nj]=2
                q.append((ni,nj))


cheese = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheese += 1

t = 0
ans = cheese
while cheese>0:
    bfs()
    temp = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                for di, dj in ((1,0),(-1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if arr[ni][nj]==2:
                        arr[i][j]=0
                        cheese-=1
                        break
                else:
                    temp +=1
    if temp!=0:
        ans = temp
    t+=1
### 정답 출력
print(t)
print(ans)