import heapq

N= int(input())

lst  = list(map(int, input().split()))
lst = list(zip(lst, [x for x in range(N)]))
ans = [0]*N

heapq.heapify(lst)
idx = 0
mn = -10**9-1
while lst:
    u,v = heapq.heappop(lst)
    if mn!=u:
        ans[v] = idx
        idx +=1
        mn = u

    else:
        ans[v] = idx-1

print(*ans)
