from collections import deque
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            virus.append((i,j))
        elif arr[i][j]==0:
            empty+=1
empty+=len(virus)-M

ans = N**2
def dfs(n,s, lst):
    global ans
    if n==M:
        ans = min(ans, bfs(lst,empty))
        return

    for i in range(s,len(virus)):
        dfs(n+1,i+1, lst+[virus[i]])

def bfs(lst,empty):
    q = deque(lst)
    v = [[0]*N for _ in range(N)]
    if empty==0:
        return 0
    for ci,cj in lst:
        v[ci][cj]=1
    t= 0
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1:
                    q.append((ni,nj))
                    v[ni][nj]=1
                    empty-=1
        t+=1
        if empty==0:
            return t
    return N**2

dfs(0,0,[])
if ans==N**2:
    print(-1)
else:
    print(ans)