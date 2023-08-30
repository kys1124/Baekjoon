import sys
input = sys.stdin.readline

M,N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
lst = []
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            lst.append((i,j))


def bfs():
    q = deque(lst)
    x = 0
    while q:
        si,sj =q.popleft()

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<M and box[ni][nj]==0:
                box[ni][nj] = box[si][sj]+1
                x = max(x, box[ni][nj]-1)
                q.append((ni,nj))
    return x


ans =bfs()
n =-1
for i in range(N):
    for j in range(M):
        if box[i][j]==0:
            print(-1)
            exit()
print(ans)