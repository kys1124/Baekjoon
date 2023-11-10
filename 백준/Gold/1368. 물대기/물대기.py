import heapq
N = int(input())

pq =[]
for i in range(N):
    pq.append((int(input()),i))

arr = [list(map(int, input().split())) for _ in range(N)]

def prim(pq):
    v = [0]*N
    total = 0
    heapq.heapify(pq)
    cnt= 0
    while pq:
        cur_cost, cur = heapq.heappop(pq)
        if v[cur]==1:
            continue
        v[cur]=1

        total+=cur_cost
        cnt+=1
        if cnt==N:
            return total

        for i in range(N):
            if v[i]==0 and i!=cur:
                heapq.heappush(pq, (arr[cur][i], i))

print(prim(pq))