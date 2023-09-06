import sys
input = sys.stdin.readline

from collections import deque

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            empty.append((i,j))
        elif arr[i][j]==2:
            virus.append((i,j))

l = len(empty)


def dfs(n,s, lst):
    global ans
    if n==3:
        for i in lst:
            arr[empty[i][0]][empty[i][1]]=1
        cnt = bfs()
        ans = max(ans, cnt)
        for i in lst:
            arr[empty[i][0]][empty[i][1]]=0
        return


    for i in range(s,l):
        dfs(n+1, i+1, lst+[i])


def bfs():
    q = deque(virus)
    v = [[0]*M for _ in range(N)]
    cnt = l-3
    for ci,cj in virus:
        v[ci][cj]=1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
                cnt -=1
    return cnt

ans = 0
dfs(0,0,[])
print(ans)