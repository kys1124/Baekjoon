import heapq
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v =[[0]*M for _ in range(N)]
K = int(input())
pq = []
for i in range(N):
    heapq.heappush(pq, (-arr[i][0],i,0))
    if M>1:
        heapq.heappush(pq,(-arr[i][M-1],i,M-1))
        v[i][M - 1] = 1
    v[i][0]=1

for j in range(1,M-1):
    heapq.heappush(pq, (-arr[0][j],0,j))
    v[0][j]=1

    if N>1:
        heapq.heappush(pq, (-arr[N-1][j],N-1,j))
        v[N - 1][j] = 1

for _ in range(K):
    val, ci,cj = heapq.heappop(pq)
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
            v[ni][nj]=1
            heapq.heappush(pq,(-arr[ni][nj], ni,nj))

    print(ci+1,cj+1)