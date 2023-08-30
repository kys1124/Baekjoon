import sys
input= sys.stdin.readline

N,M,K = map(int, input().split())
arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
ans = -10000*K
v = [[0]*(M+2) for _ in range(N+2)]
def dfs(n, sm):
    global ans
    if n==K:
        ans = max(ans, sm)
        return

    for i in range(1,N+1):
        for j in range(1,M+1):
            if v[i][j]==0 and v[i-1][j]!=1 and v[i+1][j]!=1 and v[i][j-1]!=1 and v[i][j+1]!=1:
                v[i][j]=1
                v[i-1][j]=v[i+1][j]=v[i][j-1]=v[i][j+1]=-1
                dfs(n+1, sm+arr[i][j])
                v[i][j] = 0
                v[i - 1][j] = v[i + 1][j] = v[i][j - 1] = v[i][j + 1] = 0

dfs(0,0)
print(ans)