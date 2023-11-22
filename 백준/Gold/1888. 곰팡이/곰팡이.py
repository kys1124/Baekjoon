N,M  = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
def dfs(si,sj, idx):
    stk = [(si,sj)]
    v[si][sj] = idx
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]>0:
                v[ni][nj]=idx
                stk.append((ni,nj))


t = 0
while True:
    idx= 1
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and v[i][j]==0:
                dfs(i,j,idx)
                idx+=1

    if idx==2:
        print(t)
        break
    t+=1

    copy_arr = [arr[i][:] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j]>0:
                k = copy_arr[i][j]
                si,sj = i-k,j-k
                ei,ej = i+k, j+k
                for ci in range(si,ei+1):
                    for cj in range(sj, ej+1):
                        if 0<=ci<N and 0<=cj<M and arr[ci][cj]<k:
                            arr[ci][cj]=k