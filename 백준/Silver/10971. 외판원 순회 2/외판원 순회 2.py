N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

v = [0]*N
ans = 1000000*N+1
def dfs(n, pre, cost):
    global ans, start
    if n>=N-1:
        if mat[pre][start]!=0:
            cost = cost+mat[pre][start]
            ans = min(ans, cost)
        return

    for x in range(N):
        if v[x]==0 and mat[pre][x]!=0:
            v[x]=1
            dfs(n+1, x, cost+mat[pre][x])
            v[x]=0

for k in range(N):
    start = k
    v[start]=1
    dfs(0,start,0)
    v[start]=0
print(ans)