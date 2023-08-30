N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def dfs(n, sm, lst,cnt):
    global ans,v, mxv
    if ans>= sm + (4-cnt)* mxv:
        return
    
    if n==2:
        mx = 0
        for si,sj in lst:
            for di,dj in ((1,0),(0,1),(0,-1)):
                ni,nj = si+di, sj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]>mx:
                    mx = arr[ni][nj]
        ans = max(ans, sm+mx)
        return

    for si,sj in lst:
        for di,dj in ((1,0),(0,1),(0,-1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                v[ni][nj]=1
                dfs(n+1, sm+arr[ni][nj], lst+[(ni,nj)], cnt+1)
                v[ni][nj]=0

v = [[0]*M for _ in range(N)]
mxv = 0
for i in range(N):
    for j in range(M):
        mxv = max(mxv, arr[i][j])

for i in range(N):
    for j in range(M):
        v[i][j]=1
        dfs(0,arr[i][j], [(i,j)],1)
        v[i][j]=0

print(ans)