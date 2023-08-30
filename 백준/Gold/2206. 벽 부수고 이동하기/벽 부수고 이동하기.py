N,M = map(int, input().split())
arr = [input() for _ in range(N)]

si,sj =0,0
ei,ej =N-1,M-1
from collections import deque

def bfs():
    v = [[[0]*M for _ in range(N)] for _ in range(2)]
    q = deque([(0,si,sj,1)])
    v[0][si][sj]=1
    while q:
        ck, ci,cj,cnt = q.popleft()
        if (ci,cj) ==(ei,ej):
            return cnt

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ck][ni][nj]==0 and arr[ni][nj]!='1':
                v[ck][ni][nj]=1
                q.append((ck, ni,nj,cnt+1))

            if 0<=ni<N and 0<=nj<M and ck==0 and v[1][ni][nj]==0 and arr[ni][nj]=='1' :
                v[1][ni][nj]=1
                q.append((1,ni,nj,cnt+1))
    return -1
print(bfs())