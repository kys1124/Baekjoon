from collections import deque
def bfs(start, end):
    queue = deque([start])
    visited =[0]*(n+1)
    dist = [0]*(n+1)
    visited[start] =1

    while queue:
        cur = queue.popleft()
        if cur==end:
            return dist[end]

        for x in adjlst[cur]:
            if visited[x]==0:
                visited[x]=1
                dist[x] = dist[cur]+1
                queue.append(x)
    return -1



n = int(input())
start, end = map(int, input().split())
m =int(input())

adjlst = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int, input().split())
    adjlst[u].append(v)
    adjlst[v].append(u)

print(bfs(start, end))