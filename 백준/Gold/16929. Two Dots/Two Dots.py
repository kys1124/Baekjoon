N,M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

ans = False
def dfs(si,sj,cnt,v):
    global i,j,ans
    if ans==True:
        return

    if si==i and sj==j:
        if cnt>=4:
            ans = True
            return

    for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
        ni,nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==arr[si][sj] and v[ni][nj]==0:
            v[ni][nj]=1
            dfs(ni,nj,cnt+1,v)
            v[ni][nj]=0


v=[[0]*M for _ in range(N)]

ans=False
for i in range(N):
    for j in range(M):
        dfs(i,j,0,v)
        if ans:
            break

    if ans:
        print('Yes')
        break
if not ans:
    print('No')