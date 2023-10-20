from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

lst = [0]+list(map(int, input().split()))
look = [0]*(N+1)
for i in range(1,len(lst)):
    look[lst[i]]=i
ans = [0]+[0]*N
def bfs():
    q = deque([1])
    v = [0]+[0]*N
    v[1]=1
    cnt =1
    while q:
        x = q.popleft()
        ans[x]=cnt
        cnt+=1
        if ans[x]!=look[x]:
            return 0

        p = []
        for y in adj[x]:
            if v[y]==0:
                v[y]=1
                p.append((y, look[y]))
        p.sort(key=lambda x:-x[1])
        while p:
            y, _ = p.pop()
            q.append(y)
    return 1

print(bfs())