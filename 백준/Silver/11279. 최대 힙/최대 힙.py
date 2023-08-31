import heapq

N = int(input())
lst = []
heapq.heapify(lst)
ans = []
for _ in range(N):
    a = int(input())
    if a:
        heapq.heappush(lst, -a)
    else:
        if lst:
            ans.append(-heapq.heappop(lst))
        else:
            ans.append(0)

for x in ans:
    print(x)
