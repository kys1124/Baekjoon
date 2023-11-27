import sys
import heapq
from collections import deque
input= sys.stdin.readline
N, K = map(int, input().split())
wait = deque()
pq = []
heapq.heapify(pq)
t = 0
idx = 1
for _ in range(N):
    num, w = map(int, input().split())
    if idx<=K:
        heapq.heappush(pq, (w, -idx, num))
        idx+=1
    else:
        wait.append((num, w))
ans = 0
cnt = 1
while pq:
    lst = []
    t, cashier, num = heapq.heappop(pq)
    lst.append(-cashier)
    ans += cnt*num
    cnt+=1
    while pq:
        nxt_t, nxt_cashier, nxt_num = heapq.heappop(pq)
        if nxt_t==t:
            lst.append(-nxt_cashier)
            ans += cnt*nxt_num
            cnt+=1
        else:
            heapq.heappush(pq, (nxt_t, nxt_cashier, nxt_num))
            break
    lst.sort()
    for i in lst:
        if wait:
            client_id, weight = wait.popleft()
            heapq.heappush(pq, (t+weight, -i, client_id))
        else:
            break

print(ans)