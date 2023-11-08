N = int(input())
arr =[list(map(int, input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
dir = {1:(-1,1),2:(-1,-1),3:(1,-1),4:(1,1)}
ans = 100*N*N

def group1(ei,d1,d2,v):
    g1 = 0
    for i in range(ei-d1-d2+1,ei):
        for j in range(N):
            if v[i][j]==1:
                idx = j
                g1+=arr[i][j]
                for new in range(idx+1,N):
                    if v[i][new]==0:
                        v[i][new]=1
                        g1+=arr[i][new]
                    else:
                        g1+=arr[i][new]
                        break
                break
    return g1,v

def make_group(ei,ej,d1,d2,v):
    q = [(0,0,2),(0,N-1,3),(N-1,0,4),(N-1,N-1,5)]
    g2,g3,g4,g5 = arr[0][0], arr[0][N-1], arr[N-1][0], arr[N-1][N-1]
    v[0][0]=2
    v[0][N-1]=3
    v[N-1][0]=4
    v[N-1][N-1]=5
    while q:
        ci,cj, cd = q.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if cd==2:
                if 0<=ni<ei-d2 and 0<=nj<=ej+d1-d2 and v[ni][nj]==0:
                    v[ni][nj]=2
                    g2+=arr[ni][nj]
                    q.append((ni,nj,2))
            elif cd==3:
                if 0<=ni<=ei-d1 and ej+d1-d2<nj<N and v[ni][nj]==0:
                    v[ni][nj]=3
                    g3+=arr[ni][nj]
                    q.append((ni,nj,3))
            elif cd==4:
                if ei-d2<=ni<N and 0<=nj<ej and v[ni][nj]==0:
                    v[ni][nj]=4
                    g4+=arr[ni][nj]
                    q.append((ni,nj,4))
            else:
                if ei-d1<ni<N and ej<=nj<N and v[ni][nj]==0:
                    v[ni][nj]=5
                    g5+=arr[ni][nj]
                    q.append((ni,nj,5))
    return g2,g3,g4,g5

def dfs(si,sj,d1,d2,d):
    global ei,ej, v, ans
    if si==ei and sj==ej and d==4:
        if d1>0 and d2>0:
            g1,newv = group1(ei,d1,d2,v)
            g1+=arr[ei][ej]
            g1+=arr[ei-d1-d2][ej+d1-d2]
            g2,g3,g4,g5= make_group(ei,ej,d1,d2,newv)
            ans = min(ans, max(g1,g2,g3,g4,g5)-min(g1,g2,g3,g4,g5))
        return

    if not (0<=si<N and 0<=sj<N):
        return

    if d==4:
        copy_v = [v[i][:] for i in range(N)]
        ni,nj = si+dir[4][0], sj+dir[4][1]
        v[si][sj]=1
        dfs(ni,nj,d1,d2,4)
        v = copy_v
    else:
        for num in (0,1):
            copy_v = [v[i][:] for i in range(N)]
            v[si][sj]=1
            ni,nj = si+dir[d+num][0], sj+dir[d+num][1]
            if d==1 and num==0:
                dfs(ni,nj,d1+1,d2,d+num)
            elif d==1 and num==1:
                dfs(ni,nj,d1,d2+1,d+num)
            elif d==2 and num==0:
                dfs(ni,nj,d1,d2+1,d+num)
            else:
                dfs(ni,nj,d1,d2,d+num)
            v = copy_v

for i in range(2,N):
    for j in range(1,N-1):
        ei,ej = i,j
        dfs(i,j,0,0,1)
print(ans)

