import sys
input = sys.stdin.readline
import heapq
N,M = map(int ,input().split())
arr = [list(input()) for _ in range(N)]
mx = -(N*M)
v = [[mx]*M for _ in range(N)]
tree = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='+':
            tree.append((i,j))
            v[i][j]= 0
        elif arr[i][j]=='V':
            si,sj = i,j


cnt = 0
while tree:
    new_tree = []
    for i in range(len(tree)):
        ci,cj = tree[i]
        for di,dj in ((1,0),(0,1),(0,-1),(-1,0)):
            ni,nj = ci+di , cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]< -(cnt+1):
                v[ni][nj]=-(cnt+1)
                new_tree.append((ni,nj))
    tree = new_tree
    cnt+=1


def dijkstra():
    pq = [(v[si][sj], si,sj)]
    heapq.heapify(pq)
    visited = [[0]*M for _ in range(N)]
    visited[si][sj] = v[si][sj]

    while pq:
        val, ci,cj = heapq.heappop(pq)
        if arr[ci][cj]=='J':
            return visited[ci][cj]

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]>max(val, v[ni][nj]):
                visited[ni][nj] = max(val, v[ni][nj])
                heapq.heappush(pq, (visited[ni][nj], ni,nj))
    return 0
print(-dijkstra())