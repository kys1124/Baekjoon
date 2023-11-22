N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
v = [[0] * N for _ in range(N)]

def check(si,sj):
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = si+di,sj+dj
        if 0<=ni<N and 0<=nj<N and arr[si][sj]<arr[ni][nj]:
            return True
    return False

def dfs(si,sj):
    if dp[si][sj]!=0:
        return dp[si][sj]
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N and arr[si][sj]<arr[ni][nj]:
            dp[si][sj] = max(dfs(ni,nj),dp[si][sj])
    dp[si][sj]+=1
    return dp[si][sj]

ans= 0
for i in range(N):
    for j in range(N):
        ans= max(ans, dfs(i,j))
print(ans)