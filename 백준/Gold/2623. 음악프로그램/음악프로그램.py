from collections import deque
N, M = map(int, input().split())
degree = [0]*(N+1)
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, *lst = map(int, input().split())
    if x>1:
        start = lst[0]
        for i in range(1,len(lst)):
            degree[lst[i]]+=1
            adj[start].append(lst[i])
            start = lst[i]

def bfs():
    q = deque()
    for i in range(1,N+1):
        if degree[i]==0:
            q.append(i)
    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)
        for nxt in adj[cur]:
            degree[nxt]-=1
            if degree[nxt]==0:
                q.append(nxt)
    if len(ans)==N:
        return ans
    else:
        return []
ans = bfs()
if ans==[]:
    print(0)
else:
    for x in ans:
        print(x)