N,M,X = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,t = map(int, input().split())
    arr[u].append((v,t))


import heapq

def dijkstra1(i,e):
    q = [(0,i)]
    heapq.heapify(q)
    v=[-1]*(N+1)
    v[i]=0

    while q:
        cost, cur =heapq.heappop(q)

        if cur==e:
            return cost

        for nextcur, nextcost in arr[cur]:
            if v[nextcur]==-1 or v[nextcur]>=nextcost+cost:
                v[nextcur]=nextcost+cost
                heapq.heappush(q, (v[nextcur], nextcur))
def dijkstra2():
    q = [(0,X)]
    heapq.heapify(q)
    v=[-1]*(N+1)
    v[X]=0

    while q:
        cost, cur =heapq.heappop(q)

        for nextcur, nextcost in arr[cur]:
            if v[nextcur]==-1 or v[nextcur]>=nextcost+cost:
                v[nextcur]=nextcost+cost
                heapq.heappush(q, (v[nextcur], nextcur))

    return v

V = [0]*(N+1)
dist = dijkstra2()
for i in range(1,N+1):
    V[i]+=dijkstra1(i,X)+dist[i]

print(max(V))