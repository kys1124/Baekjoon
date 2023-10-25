N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

arr2  =[list(map(int, input().split())) for _ in range(N)]

idx = 1
v = [[0]*M for _ in range(N)]
def dfs(si,sj, idx):
    stk = [(si,sj)]
    v[si][sj]=idx
    group = [(si,sj)]
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==arr[si][sj]:
                group.append((ni,nj))
                stk.append((ni,nj))
                v[ni][nj]=idx
    return group

def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if v[i][j]==0:
                group = dfs(i,j,idx)
                number = arr2[group[0][0]][group[0][1]]
                if arr[i][j]==number:
                    for ci,cj in group:
                        if arr2[ci][cj]!=number:
                            return 'NO'
                else:
                    cnt+=1
                    for ci,cj in group:
                        if arr2[ci][cj]!=number:
                            return 'NO'
    if cnt>1:
        return 'NO'
    else:
        return 'YES'
print(check())

