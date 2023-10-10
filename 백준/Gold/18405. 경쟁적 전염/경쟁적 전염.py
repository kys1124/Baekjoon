from collections import deque

N,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S,X,Y = map(int, input().split())
virus = []
v=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]>0:
            virus.append((arr[i][j],i,j))
            v[i][j]=1
virus.sort()
def bfs(t):
    q= deque(virus)
    while q:
        if t==S:
            return
        for _ in range(len(q)):
            num,ci,cj = q.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj

                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==0:
                    v[ni][nj]=1
                    arr[ni][nj]=num
                    q.append((num, ni, nj))

        t+=1

t = 0
bfs(t)
print(arr[X-1][Y-1])