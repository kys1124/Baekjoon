from collections import deque


def dfs(start):
    stack = deque([start-1])
    answer = []
    while stack:
        cur = stack.pop()

        if not visited[cur]:
            answer.append(cur + 1)
            visited[cur]=True
            for x in adjlst[cur]:
                stack.append(x)

    return answer

def bfs(start):
    queue = deque([start-1])
    visited[start-1] = True
    answer = []
    while queue:
        cur = queue.popleft()

        answer.append(cur+1)

        for x in adjlst[cur]:
           if not visited[x]:
               visited[x] = True
               queue.append(x)

    return answer

n,m,v = map(int, input().split())

adjlst = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    adjlst[a-1].append(b-1)
    adjlst[b-1].append(a-1)

for x in adjlst:
    x.sort(reverse=True)

visited = [False]*n
print(*dfs(v))
for x in adjlst:
    x.sort()
visited = [False]*n
print(*bfs(v))
