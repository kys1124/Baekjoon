from collections import deque
N,M= map(int, input().split())
arr =[list(map(int, input())) for _ in range(N)]

def bfs(si,sj, h):
    q=  deque([(si,sj)])
    v[si][sj]=1
    lst =[(si,sj)]
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if (0==ni or nj==0 or ni==N-1 or nj==M-1) and h>arr[ni][nj]:
                    return True, lst

                elif 0<ni<N-1 and 0<nj<M-1 and v[ni][nj]==0 and arr[ni][nj]<h:
                    q.append((ni,nj))
                    v[ni][nj]=1
                    lst.append((ni,nj))

    return False, lst

ans = 0
for h in range(1,10):
    v = [[0] * M for _ in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if v[i][j]==0 and h>arr[i][j]:
                flag, lst = bfs(i,j,h)
                if flag:
                    for ci,cj in lst:
                        v[ci][cj]=0

    for i in range(1,N-1):
        for j in range(1,M-1):
            if v[i][j]==1:
                ans+=1

print(ans)