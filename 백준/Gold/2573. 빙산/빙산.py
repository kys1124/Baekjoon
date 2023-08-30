N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def bfs(si, sj):
    q = deque([(si,sj)])
    v = [[0]*M for _ in range(N)]
    v[si][sj]=1
    cnt = 1
    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt


t = 0
while True:
    ice = 0
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                ice += 1
                si,sj = i,j
                temp = 0
                for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    ni,nj = i+di, j+dj
                    if arr[ni][nj]==0:
                        temp+=1
                lst.append((i,j,temp))

    if not lst:
        print(0)
        break
    else:
        if bfs(lst[0][0],lst[0][1])==ice:
            for x,y,z in lst:
                arr[x][y]-=z
                if arr[x][y]<0:
                    arr[x][y]=0
            t+=1
        else:
            print(t)
            break