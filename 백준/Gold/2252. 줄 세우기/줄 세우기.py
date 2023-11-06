from collections import deque

N, M = map(int, input().split())
lst = [0]*(N+1)
adj = [[] for _ in range(1+N)]
for _ in range(M):
    a,b= map(int, input().split())
    lst[b]+=1
    adj[a].append(b)

def bfs():
    q = deque()
    v = [0]*(N+1)
    ans = []
    for i in range(1,N+1):
        if lst[i]==0:
            q.append(i)
            v[i]=1

    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            ans.append(cur)

            for nxt in adj[cur]:
                if v[nxt]==0:
                    lst[nxt]-=1
                    if lst[nxt]==0:
                        q.append(nxt)
                        v[nxt]=1
    return ans

print(*bfs())