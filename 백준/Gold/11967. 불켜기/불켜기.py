N, M = map(int, input().split())
v = [[0]*N for _ in range(N)]
arr = [[0]*N for _ in range(N)]

adj = [[] for _ in range(N**2)]
for _ in range(M):
    x,y,a,b= map(lambda x:int(x)-1, input().split())
    adj[x*N+y].append(a*N+b)

arr[0][0]=1

from collections import deque
def bfs(si,sj):
    q = deque([(si,sj)])
    cnt= 1
    while q:
        ci,cj = q.popleft()

        for nxt in adj[ci*N+cj]:
            ni,nj = nxt//N, nxt%N
            if arr[ni][nj]==0:
                arr[ni][nj]=1
                cnt+=1
                v = [[0] * N for _ in range(N)]

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
    return cnt

v[0][0]=1
print(bfs(0,0))