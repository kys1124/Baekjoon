import heapq
N, M = map(int, input().split())
arr =[list(input()) for _ in range(N)]
adj = [[] for _ in range(M+1)]
def bfs(si,sj, idx):
    q = [(si,sj)]
    v = [[0]*N for _ in range(N)]
    v[si][sj]=1
    cnt = 0
    while q:
        temp_q = []
        for i in range(len(q)):
            ci,cj = q[i]
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!='1':
                    temp_q.append((ni,nj))
                    v[ni][nj]=1
                    if arr[ni][nj]!='0' and idx<dic[(ni,nj)]:
                        adj[idx].append((cnt+1, dic[(ni,nj)]))
                        adj[dic[(ni,nj)]].append((cnt+1, idx))
        cnt+=1
        q = temp_q

def prim():
    S = set()
    pq = [(0,0)]
    sm = 0
    while pq:
        dist, cur = heapq.heappop(pq)
        if cur in S:
            continue
        S.add(cur)
        sm+=dist
        if len(S) == M+1:
            return sm

        for nxt_dist, nxt in adj[cur]:
            if nxt not in S:
                heapq.heappush(pq, (nxt_dist, nxt))
    return -1

idx = 1
lst = [(-1,-1)]
dic = {}
for i in range(N):
    for j in range(N):
        if arr[i][j]=='K':
            dic[(i,j)] = idx
            lst.append((i,j))
            idx+=1

        elif arr[i][j]=='S':
            dic[(i,j)] = 0
            lst[0] = (i,j)

for i in range(N):
    for j in range(N):
        if arr[i][j]=='S' or arr[i][j]=='K':
            bfs(i,j,dic[(i,j)])
print(prim())