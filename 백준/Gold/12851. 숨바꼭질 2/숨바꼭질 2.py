import heapq
N, K = map(int, input().split())
def dijkstra():
    global t, ans
    q = [(0,N)]
    heapq.heapify(q)
    v = [-1]*100001
    v[N]=0
    while q:
        ct, c = heapq.heappop(q)
        if c==K:
            t =ct
            ans +=1

        for i in (-1,1):
            n = c+i
            if 0<=n<=100000 and (v[n]==-1 or v[n]>=ct+1):
                v[n]=ct+1
                heapq.heappush(q,(ct+1, n))
        n = 2*c
        if n<=100000 and (v[n]==-1 or v[n]>=ct+1):
            v[n] =ct+1
            heapq.heappush(q,(ct+1,n))

    return t, ans

ans =0
t= 0
a,b= dijkstra()
print(a)
print(b)