import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

def bfs(s,e):
    q = deque([s])
    v = [0]*N
    while q:
        c =q.popleft()

        for n in range(N):
            if adj[c][n]==1 and v[n]==0:
                v[n]=1
                q.append(n)
                if n==e:
                    return 1
    return 0

ret = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        ret[i][j] = bfs(i,j)

for x in ret:
    print(*x)