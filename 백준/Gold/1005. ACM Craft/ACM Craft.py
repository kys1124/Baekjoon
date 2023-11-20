from collections import deque
T = int(input())

def bfs():
    q = deque()
    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
            dp[i]+=time_lst[i]

    while q:
        cur = q.popleft()
        if cur == e:
            return dp[cur]

        for nxt in adj[cur]:
            dp[nxt] = max(dp[cur], dp[nxt])
            if degree[nxt] > 0:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
                    dp[nxt] +=time_lst[nxt]

for _ in range(T):
    N, K = map(int, input().split())
    time_lst = [0]+list(map(int, input().split()))
    adj =  [[] for _ in range(N+1)]
    degree = [0]*(N+1)
    for _ in range(K):
        a, b = map(int, input().split())
        adj[a].append(b)
        degree[b]+=1
    e = int(input())
    dp = [0]*(N+1)
    print(bfs())