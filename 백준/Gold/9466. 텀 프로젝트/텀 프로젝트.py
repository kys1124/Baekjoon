from collections import deque
T = int(input())
for _ in range(T):
    N =int(input())
    lst = list(map(int, input().split()))
    degree = [0]*(N+1)
    adj = [[] for _ in range(N+1)]
    for idx, val in enumerate(lst, start=1):
        adj[idx].append(val)
        degree[val]+=1

    q = deque()
    v = [0] * (N + 1)
    cnt = 0

    for i in range(1,N+1):
        if degree[i]==0:
            q.append(i)
            v[i]=1
            cnt+=1

    while q:
        for _ in range(len(q)):
            cur = q.popleft()

            for nxt in adj[cur]:
                if v[nxt]==0:
                    degree[nxt]-=1
                    if degree[nxt]==0:
                        v[nxt]=1
                        q.append(nxt)
                        cnt+=1
    print(cnt)