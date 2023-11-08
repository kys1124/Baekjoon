N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[[0]*M for _ in range(N)] for _ in range(2)]

cnt = 1
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            q.append((i,j,1))
            v[0][i][j]=1
        elif arr[i][j]==2:
            q.append((i,j,2))
            v[1][i][j]=1
ans = [1,1,0]
while q:
    temp_q = []
    S = set()
    for i in range(len(q)):
        ci,cj,type = q[i]
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[type-1][ni][nj]==0 and arr[ni][nj]==0:
                v[type-1][ni][nj]=cnt+1
                S.add((ni,nj))

    for ci,cj in S:
        if v[0][ci][cj]==cnt+1 and v[1][ci][cj]==cnt+1:
            arr[ci][cj]=3
            ans[2]+=1
        elif v[0][ci][cj]==cnt+1:
            arr[ci][cj]=1
            ans[0]+=1
            temp_q.append((ci,cj,1))
        elif v[1][ci][cj]==cnt+1:
            arr[ci][cj]=2
            ans[1]+=1
            temp_q.append((ci,cj,2))
    cnt+=1
    q = temp_q
print(*ans)