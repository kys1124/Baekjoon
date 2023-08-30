N,M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]
s = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='.':
            arr[i][j]='@'

        if i==0 or j==0 or i==N-1 or j==M-1:
            if arr[i][j]=='@':
                s.append((i,j))

si,sj = s[0][0],s[0][1]
ei,ej =s[1][0], s[1][1]

from collections import deque
def bfs():
    q = deque([(si, sj)])
    v = [[0]*M for _ in range(N)]
    v[si][sj]=1

    path = dict()

    while q:
        ci,cj = q.popleft()
        if ci==ei and cj==ej:
            return path

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='@' and v[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
                path[(ni,nj)]=(ci,cj)

path = bfs()
while (ei,ej)!=(si,sj):
    arr[ei][ej]='.'
    ei,ej = path[(ei,ej)]
arr[ei][ej]='.'
for x in arr:
    print(''.join(x))