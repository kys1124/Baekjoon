N, M = map(int,input().split())
arr =[list(map(int, input().split())) for _ in range(N)]

dp =[[0]*M for _ in range(N)]
v = [[0]*M for _ in range(N)]
def dfs(si,sj): # si,sj 에서 N-1, M-1까지 가는 경우의 수
    if (si,sj)==(N-1,M-1):
        return 1

    if v[si][sj]!=0:
        return dp[si][sj]

    v[si][sj]=1
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]<arr[si][sj]:
             dp[si][sj]+=dfs(ni,nj)
    return dp[si][sj]

print(dfs(0,0))