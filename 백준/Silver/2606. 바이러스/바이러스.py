def dfs(start):
    visited[start]=1
    for x in adjlst[start]:
        if visited[x]==0:
            visited[x]=1
            dfs(x)



N = int(input())
M = int(input())
adjlst = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    adjlst[u].append(v)
    adjlst[v].append(u)

visited = [0] * (N + 1)
dfs(1)
print(visited.count(1)-1)