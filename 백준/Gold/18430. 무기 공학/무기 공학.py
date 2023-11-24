N, M = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
ans = 0
dir = {0:[(0,-1),(1,0)],1:[(0,-1),(-1,0)],2:[(-1,0),(0,1)],3:[(1,0),(0,1)]}
def dfs(n, sm, v):
    global  ans
    if n==N*M:
        ans = max(ans, sm)
        return

    ci,cj = n//M, n%M
    if v[ci][cj]==0:
        for i in range(4):
            lst = []
            for di,dj in dir[i]:
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                    lst.append((ni,nj))
                else:
                    break
            else:
                add = arr[ci][cj]*2
                v[ci][cj]=1
                for ni,nj in lst:
                    v[ni][nj]=1
                    add+=arr[ni][nj]
                dfs(n+1, sm+add, v)
                v[ci][cj]=0
                for ni, nj in lst:
                    v[ni][nj] = 0
    dfs(n+1,sm,v)

dfs(0,0,v)
print(ans)