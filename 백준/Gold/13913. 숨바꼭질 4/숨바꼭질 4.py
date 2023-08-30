import heapq

N,K = map(int, input().split())

def dijkstra():
    q = [(0,N)]
    v = [[-1,-1] for _ in range(100001)]
    heapq.heapify(q)
    v[N][0]=0
    v[N][1]=N

    while q:
        ct, c = heapq.heappop(q)
        if c==K:
            return ct, v

        for i in (-1,1):
            n = i+c
            if 0<=n<=100000 and (v[n][0]==-1 or v[n][0]>=ct+1):
                v[n][0]=ct+1
                v[n][1] = c
                heapq.heappush(q, (ct+1, n))

        n =c*2
        if n<=100000 and (v[n][0]==-1 or v[n][0]>=ct+1):
            v[n][1]=c
            v[n][0]=ct+1
            heapq.heappush(q, (ct+1, n))

t, v = dijkstra()
print(t)
if t==0:
    print(N)
else:
    s = v[K][1]
    ans = [K]
    while s!=N:
        ans.append(s)
        s=v[s][1]
    ans.append(N)
    print(*ans[::-1])