N, K = map(int, input().split())
import heapq
di = (1,-1)
visited = [100000]*1000000
def bfs():
    q = [N]
    heapq.heapify(q)
    visited[N]=0
    while q:
        cur = heapq.heappop(q)
        if q==K:
           return

        for i in di:
            ni = cur+i
            if 0<=ni<=100000 and visited[ni]>visited[cur]+1:
                visited[ni]=visited[cur]+1
                heapq.heappush(q,ni)

        ni = cur*2
        if 0 <= ni <= 100000 and visited[ni] > visited[cur] + 1:
            visited[ni] = visited[cur] + 1
            heapq.heappush(q,ni)
bfs()
print(visited[K])