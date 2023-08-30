N,M= map(int, input().split())
arr = [list(map(int , input().split())) for _ in range(N)]

virus = []
sm = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            virus.append((i,j))
        elif arr[i][j]==0:
            sm+=1

ans = N**2+1

from collections import deque
s =[]
def combination(n, next, lst):
    global s
    if n==M:
        s.append(lst)
        return

    for i in range(next, len(virus)):
        combination(n+1, i+1, lst+[(virus[i][0],virus[i][1])])

combination(0,0, [])
def bfs(s):
    global sm, ans
    q = deque(s)
    v = [[0]*N for _ in range(N)]
    cnt = 0
    for i,j in s:
        v[i][j]=1
    t = 0
    while q:
        if cnt==sm:
            return t

        if t>=ans:
            return ans

        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==0:
                    v[ni][nj]=1
                    cnt +=1
                    q.append((ni,nj))
                elif 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==2:
                    v[ni][nj]=1
                    q.append((ni,nj))
        t += 1

    if cnt!=sm:
        return -1


for x in s:
    time = bfs(x)
    if time==-1:
        continue
    else:
        ans = time

if ans==N**2+1:
    print(-1)
else:
    print(ans)