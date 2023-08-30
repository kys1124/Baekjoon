N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
wall = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            virus.append((i,j))
        elif arr[i][j]==0:
            wall.append((i,j))

combi = []
def combination(n, s, lst):
    global wall
    if n==3:
        combi.append(lst)
        return

    for i in range(s,len(wall)):
        combination(n+1,i+1, lst+[wall[i]])

from collections import deque

def bfs(combi):
    global ans
    q = deque(virus)
    v = [[0]*M for _ in range(N)]
    safe = len(wall) - 3
    for i,j in combi:
        arr[i][j]=1

    for i,j in virus:
        v[i][j]=1
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()

            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!=1:
                    v[ni][nj]=1
                    q.append((ni,nj))
                    if arr[ni][nj]==0:
                        safe-=1

    for i,j in combi:
        arr[i][j]=0
    return safe


combination(0,0,[])
ans = 0
for x in combi:
    ans = max(ans ,bfs(x))

print(ans)