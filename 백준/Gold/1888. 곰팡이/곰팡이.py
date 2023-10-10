N,M = map(int, input().split())
arr =[list(map(int, input())) for _ in range(N)]

def dfs(si,sj,idx):
    stk = [(si,sj)]
    v[si][sj]=idx
    while stk:
        ci,cj = stk.pop()

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=0 and v[ni][nj]==0:
                v[ni][nj]=idx
                stk.append((ni,nj))

ans = 0
while True:
    idx = 1
    v =[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if v[i][j]==0 and arr[i][j]>0:
                dfs(i,j,idx)
                idx+=1

    if idx==2:
        break
    ans +=1

    new = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if v[i][j]>0:
                k = arr[i][j]
                for si in range(max(0,i-k), min(N,i+k+1)):
                    for sj in range(max(0,j-k), min(M,j+k+1)):
                        if new[si][sj]<k:
                            new[si][sj]=k

    arr = new
print(ans)