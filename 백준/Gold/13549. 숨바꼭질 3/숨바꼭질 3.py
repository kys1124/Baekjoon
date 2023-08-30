N, K = map(int, input().split())
import heapq

def bfs():
    q =[(0,N)]
    heapq.heapify(q)
    v = [-1]*100001
    v[N]=0

    while q:
        ct, c = heapq.heappop(q)

        if c==K:
            return ct
        if c+1<=100000 and (v[c+1]==-1 or v[c+1]>=ct+1):
            v[c+1]=ct+1
            heapq.heappush(q,(ct+1,c+1))
        if c-1>=0 and (v[c -1] == -1 or v[c -1] >= ct + 1):
            v[c -1] = ct + 1
            heapq.heappush(q, (ct + 1, c - 1))
        if 0<2*c<=100000 and (v[2*c] == -1 or v[2*c] >= ct):
            v[2*c] = ct
            heapq.heappush(q, (ct, 2*c))

print(bfs())
