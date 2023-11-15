from collections import deque
T = int(input())

for _ in range(T):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    v = [0]+list(map(int, input().split())) #보물 가치
    degree = [0]*(N+1)
    for _ in range(E):
        a,b,c = map(int, input().split())
        adj[a].append((b,c)) # a->b 연결되어 있고, b에 장비를 넣는데 c만큼의 비용 발생.
        degree[b]+=1

    def bfs():
        profit =[0]*(N+1)
        path = [0]*(N+1)
        q = deque([1])
        profit[1] = v[1]
        while q:
            cur = q.popleft()
            for nxt, nxt_cost in adj[cur]:
                if profit[nxt]==0:
                    path[nxt] = cur
                    profit[nxt] = profit[cur] + v[nxt] - nxt_cost
                else:
                    if profit[nxt] < profit[cur] + v[nxt] - nxt_cost:
                        path[nxt] = cur
                        profit[nxt] = profit[cur] + v[nxt] - nxt_cost
                if degree[nxt]>0:
                    degree[nxt]-=1
                    if degree[nxt]==0:
                        q.append(nxt)
        return profit[1:], path[1:]

    profit, path = bfs()
    mx = max(profit)
    idx = profit.index(mx)+1
    ans = [idx]
    while idx != 1:
        ans.append(path[idx-1])
        idx = path[idx-1]
    ans.reverse()
    print(mx, len(ans))
    print(*ans)