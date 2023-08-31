import sys
sys.setrecursionlimit(10000)
n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]


def dfs(c):
    visited[c]=1
    for x in adj[c]:
        if visited[x]==0:
            dfs(x)

for _ in range(m):
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited=[0]*(n+1)
ans = 0
for i in range(1,n+1):
    if visited[i]==0:
        ans +=1
        dfs(i)
print(ans)
