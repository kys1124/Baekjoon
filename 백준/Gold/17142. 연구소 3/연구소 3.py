N, M = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]

virus = []
empty = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==0:
            empty+=1
        elif arr[i][j]==2:
            virus.append((i,j))

ans = N**2
def dfs(n,s, lst):
    global ans
    if n==M:
        ans = min(ans ,bfs(lst, empty))
        return

    for i in range(s,len(virus)):
        dfs(n+1, i+1, lst+[i])

def bfs(lst, empty):
    v = [[0]*N for _ in range(N)]
    q = []
    for i in lst:
        ci,cj = virus[i]
        q.append((ci,cj))
        v[ci][cj]=1
    t = 0
    if empty==0:
        return 0
    while q:
        temp_q = []
        for i in range(len(q)):
            ci,cj = q[i]
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1:
                    v[ni][nj]=1
                    temp_q.append((ni,nj))
                    if arr[ni][nj]==0:
                        empty-=1
        if empty==0:
            return t+1
        t+=1
        q = temp_q
    return N**2
dfs(0,0,[])
if ans==N**2:
    print(-1)
else:
    print(ans)