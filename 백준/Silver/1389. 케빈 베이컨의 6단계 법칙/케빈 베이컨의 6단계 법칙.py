from collections import deque
N, M = map(int,  input().split())
adjlst = [[] for _ in range(N)]


def bacon(start):
    queue = deque([start])
    check = [False] * N
    depth = 1
    ans =  [(M**2)*(N**2)]*N
    ans[start] = 0

    while queue:
        cur = queue.popleft()
        if check[cur]:
            continue
        check[cur]=True

        for x in adjlst[cur]:
            if not check[x]:
                queue.append(x)
                ans[x] = min(ans[x],ans[cur]+1)
    return ans

for _ in range(M):
    u,v = map(int, input().split())
    adjlst[u-1].append(v-1)
    adjlst[v-1].append(u-1)
board = [[0]*N for _ in range(N)]

ans = M*M*N*N
idx = N
for i in range(N):
    sm = sum(bacon(i))
    if sm<ans:
        ans = sm
        idx = i
    elif sm==ans:
        idx = min(idx, i)
print(idx+1)