N,M  = map(int, input().split())
dir = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
arr =[list(input()) for _ in range(N)]
cost = [list(map(int, input().split())) for _ in range(N)]

v = [[0]*M for _ in range(N)]
ans = 0

def dfs(si,sj, idx):
    stk =[(si,sj)]
    v[si][sj]=idx
    path = {}
    while stk:
        ci,cj= stk.pop()

        di,dj = dir[arr[ci][cj]]
        ni,nj = ci+di,cj+dj
        if not (0<=ni<N and 0<=nj<M):
            return 0,0
        elif v[ni][nj]==0:
            v[ni][nj]=idx
            stk.append((ni,nj))
            path[(ni,nj)] = (ci,cj)

        elif v[ni][nj]==idx:
            mx = min(cost[ci][cj], cost[ni][nj])
            while path[(ci,cj)]!=(ni,nj):
                ci,cj = path[(ci,cj)]
                mx = min(mx, cost[ci][cj])
            return 1, mx

        elif v[ni][nj]!=idx:
            return 0,0

idx=1
for i in range(N):
    for j in range(M):
        if v[i][j]==0:
            cnt, c = dfs(i,j,idx)
            idx+=1
            if cnt==1:
                ans+=c
print(ans)