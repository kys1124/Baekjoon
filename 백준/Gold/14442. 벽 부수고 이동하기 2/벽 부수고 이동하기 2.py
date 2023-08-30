N,M,K = map(int, input().split())

arr = [input() for _ in range(N)]
from collections import deque
def bfs():
    q = deque([(0,0,0,1)])
    v = [[-1] * M for _ in range(N)]
    v[0][0]=0
    while q:
        ci,cj,ck, cnt = q.popleft()
        if (cj,ck) == (N-1,M-1):
            return cnt

        for dj,dk in ((-1,0),(1,0),(0,1),(0,-1)):
            nj,nk = cj+dj, ck+dk
            if 0<=nj<N and 0<=nk<M and (v[nj][nk]==-1 or v[nj][nk]>ci) and arr[nj][nk]=='0':
                v[nj][nk]=ci
                q.append((ci,nj,nk,cnt+1))

            elif 0<=nj<N and 0<=nk<M and ci+1<K+1 and (v[nj][nk]==-1 or v[nj][nk]>ci+1) and arr[nj][nk]=='1':
                v[nj][nk]=ci+1
                q.append((ci+1,nj,nk,cnt+1))

    return -1

print(bfs())