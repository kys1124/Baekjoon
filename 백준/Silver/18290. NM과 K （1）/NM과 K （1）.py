N,M,K= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = max(map(max, arr))
v= [[0]*M for _ in range(N)]
ans = -10000*K
def dfs(n,sm,v):
    global ans
    if ans>=sm+(K-n)*mx:
        return

    if n==K:
        ans = max(ans, sm)

        return

    for i in range(N*M):
        r,c = i//M,i%M
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = r+di, c+dj
            if not (0<=ni<N and 0<=nj<M) or v[ni][nj]==0:
                continue
            else:
                break
        else:
            if v[r][c]==0:
                v[r][c] = 1
                dfs(n + 1, sm + arr[r][c], v)
                v[r][c] = 0

dfs(0,0,v)
print(ans)