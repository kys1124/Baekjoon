from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            empty.append((i,j))
        elif arr[i][j]==2:
            virus.append((i,j))
total_cnt = len(empty)

def bfs(arr,total_cnt):
    q = deque(virus)
    v = [[0]*M for _ in range(N)]
    for ci,cj in virus:
        v[ci][cj]=1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!=1:
                if arr[ni][nj]==0:
                    total_cnt-=1
                v[ni][nj]=1
                q.append((ni,nj))
    return total_cnt

ans = 0
def dfs(n, s, lst):
    global ans
    if n==3:
        for ci,cj in lst:
            arr[ci][cj]=1
        ans = max(ans, bfs(arr,total_cnt-3))
        for ci,cj in lst:
            arr[ci][cj]=0
        return

    for i in range(s,len(empty)):
        dfs(n+1, i+1, lst+[empty[i]])

dfs(0,0,[])
print(ans)