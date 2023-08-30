K = int(input())
W,H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

si,sj = 0,0
ei,ej = H-1,W-1
from collections import deque

def bfs():
    q = deque([(0,si,sj)])
    v = [[K+1]*W for _ in range(H)]
    t = 0
    v[0][0]=0
    while q:
        for _ in range(len(q)):
            cnt, ci,cj = q.popleft()
            if ci==ei and cj==ej:
                return t

            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<H and 0<=nj<W and v[ni][nj]>cnt and arr[ni][nj]==0:
                    v[ni][nj]=cnt
                    q.append((cnt,ni,nj))

            for di,dj in ((-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<H and 0<=nj<W and cnt<K and v[ni][nj]>cnt+1 and arr[ni][nj]==0:
                    v[ni][nj]=cnt+1
                    q.append((cnt+1, ni,nj))

        t+=1
    return -1

print(bfs())