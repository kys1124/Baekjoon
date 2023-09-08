N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def bfs():
    q =deque([(0,0)])
    v = [[0]*M for _ in range(N)]
    v[0][0] = 1
    t = 0
    ans1 = T+1
    ans2 = T+1
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()

            if ci==N-1 and cj==M-1:
                ans1= t

            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj

                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!=1:
                    v[ni][nj]=1
                    q.append((ni,nj))
                    if arr[ni][nj]==2:
                        ans2 = t+1+abs(N-1-ni)+abs(M-1-nj)

        t +=1
    if min(ans1, ans2)<=T:
        return min(ans1, ans2)
    else:
        return -1

t = bfs()
if t!=-1:
    print(t)
else:
    print('Fail')