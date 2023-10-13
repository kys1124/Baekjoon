N, M, K = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    r,c = map(lambda x:int(x)-1, input().split())
    arr[r][c]=1

v = [[0]*M for _ in range(N)]
def dfs(si,sj):
    stk = [(si,sj)]
    v[si][sj]=1
    cnt = 1
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                v[ni][nj]=1
                stk.append((ni,nj))
                cnt+=1
    return cnt

ans = 0
for i in range(N):
    for j in range(M):
        if v[i][j]==0 and arr[i][j]==1:
            ans = max(ans, dfs(i,j))
print(ans)