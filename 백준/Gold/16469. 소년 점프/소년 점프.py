R,C = map(int, input().split())
arr =[input() for _ in range(R)]
x1,y1 = map(int ,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int, input().split())

v = [[[-1]*C for _ in range(R)] for _ in range(3)]

from collections import deque

def bfs():
    q = deque([(x1-1,y1-1,0),(x2-1,y2-1,1),(x3-1,y3-1,2)]) #악당 시작 좌표랑 누구인지 표시
    v[0][x1-1][y1-1]=0
    v[1][x2-1][y2-1]=0
    v[2][x3-1][y3-1]=0
    t = 0
    while q:
        for _ in range(len(q)):
            ci,cj, people = q.popleft()

            for di,dj in ((0,0),(1,0),(0,1),(-1,0),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<R and 0<=nj<C and (v[people][ni][nj]==-1 or v[people][ni][nj]>t+1) and arr[ni][nj]=='0':
                    q.append((ni,nj,people))
                    v[people][ni][nj]=t+1

        t+=1

bfs()
ans = 1e9
cnt = 0
for i in range(R):
    for j in range(C):
        if v[0][i][j]!=-1 and v[1][i][j]!=-1 and v[2][i][j]!=-1:
            t = max(v[0][i][j], v[1][i][j], v[2][i][j])
            if ans>t:
                ans = t
                cnt = 1
            elif ans==t:
                cnt +=1

if cnt>0:
    print(ans)
    print(cnt)
else:
    print(-1)
