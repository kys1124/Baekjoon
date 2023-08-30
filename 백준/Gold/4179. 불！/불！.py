from collections import deque
N, M = map(int, input().split())
arr =[list(map(str, input())) for _ in range(N)]


q = deque()
v= [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='J':
            si,sj = i,j
        elif arr[i][j]=='F':
            q.append((i,j,'F'))
            v[i][j]=1

q.append((si, sj,'J'))

def bfs():
    t = 0
    while q:
        for _ in range(len(q)):
            ci,cj, p = q.popleft()
            v[ci][cj]=1

            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and p=='F' and arr[ni][nj]!='#':
                    v[ni][nj]=1
                    arr[ni][nj]='F'
                    q.append((ni,nj,'F'))

                elif 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and p=='J' and arr[ni][nj]=='.':
                    v[ni][nj]=1
                    q.append((ni,nj,'J'))
                    arr[ni][nj]='J'

                elif p=='J' and (ni<0 or ni>=N or nj<0 or nj>=M):
                    return t+1
        t+=1
    return -1
t =bfs()
if t==-1:
    print('IMPOSSIBLE')
else:
    print(t)