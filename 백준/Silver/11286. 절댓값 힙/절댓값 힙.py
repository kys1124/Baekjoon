N = int(input())
lst = []
import heapq
heapq.heapify(lst)
ans =[]
for _ in range(N):
    x = int(input())
    if x!=0:
        heapq.heappush(lst, (abs(x),x))

    else:
        if lst:
            _,value = heapq.heappop(lst)
            ans.append(value)
        else:
            ans.append(0)

for x in ans:
    print(x)