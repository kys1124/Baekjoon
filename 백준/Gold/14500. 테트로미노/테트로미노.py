N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def dfs(n, sm, lst):
    global ans
    if ans>=sm+(3-n)*1000:
        return

    if n==3:
        ans = max(ans, sm)
        return


    for ci,cj in lst:
        for di, dj in ((-1, 0), (0, 1), (0, -1)):
            ni,nj = di+ci, dj+cj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                v[ni][nj]=1
                dfs(n+1, sm+arr[ni][nj], lst+[(ni,nj)])
                v[ni][nj]=0

v = [[0]*M for _ in range(N)]


for i in range(N):
    for j in range(M):
        v[i][j]=1
        dfs(0,arr[i][j], [(i,j)])
        v[i][j]=0

print(ans)