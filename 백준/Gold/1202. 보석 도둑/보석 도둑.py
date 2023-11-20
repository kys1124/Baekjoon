import heapq
N, K  = map(int, input().split())
pq = []
heapq.heapify(pq)
for _ in range(N):
    M,V = map(int, input().split())
    heapq.heappush(pq, (M,V))

for _ in range(K):
    C = int(input())
    heapq.heappush(pq, (C,1000001))

pq2 = []
heapq.heapify(pq2)
cnt =0
ans = 0
while pq:
    weight, value = heapq.heappop(pq)
    if value!=1000001:
        heapq.heappush(pq2, -value)
    else:
        cnt+=1
        if pq2:
            ans+= -heapq.heappop(pq2)

        if cnt==K:
            break
print(ans)