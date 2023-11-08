N,M = map(int, input().split())
arr = [[6]*(M+2)]+[[6]+list(map(int, input().split()))+[6] for _ in range(N)]+[[6]*(M+2)]

cctv = []
dir = {1:[(1,0),(0,1),(-1,0),(0,-1)],
       2:[[(1,0),(-1,0)],[(0,1),(0,-1)]],
       3:[[(-1,0),(0,1)],[(0,1),(1,0)],[(1,0),(0,-1)],[(0,-1),(-1,0)]],
       4:[[(0,-1),(-1,0),(0,1)],[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]],
       5:[[(0,1),(1,0),(0,-1),(-1,0)]]
       }
empty= 0
v = [[0]*(M+2) for _ in range(N+2)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]!=0 and arr[i][j]!=6:
            cctv.append((i,j,arr[i][j]))
            v[i][j]=1

        elif arr[i][j]==0:
            empty+=1

ans = empty
def dfs(n, v):
    global ans
    if n==len(cctv):
        sm = 0
        for i in range(1,N+1):
            for j in range(1,M+1):
                if arr[i][j]==0:
                    sm+=1

        ans = min(ans, sm)
        return

    ci,cj, type = cctv[n]
    if type==1:
        lst = []
        for di,dj in dir[1]:
            for mul in range(1,max(N,M)):
                ni,nj = ci+mul*di, cj+mul*dj
                if arr[ni][nj]==6:
                    break
                elif v[ni][nj]==0:
                    lst.append((ni,nj))
                    v[ni][nj]=1
                    arr[ni][nj]=-1
            dfs(n+1,v)
            for i,j in lst:
                v[i][j]=0
                arr[i][j]=0
    else:
        for i in range(len(dir[type])):
            lst = []
            for di,dj in dir[type][i]:
                for mul in range(max(N, M)):
                    ni, nj = ci + mul * di, cj + mul * dj
                    if arr[ni][nj] == 6:
                        break
                    elif v[ni][nj] == 0:
                        lst.append((ni, nj))
                        v[ni][nj] = 1
                        arr[ni][nj] = -1
            dfs(n + 1, v)
            for i, j in lst:
                v[i][j] = 0
                arr[i][j] = 0
dfs(0,v)
print(ans)