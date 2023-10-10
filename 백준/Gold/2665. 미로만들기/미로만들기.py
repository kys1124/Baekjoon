import heapq
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
V = [[N**2]*N for _ in range(N)]
si,sj = 0,0
ei,ej = N-1,N-1

def dijkstra(si,sj):
    pq = [(0,si,sj)]
    heapq.heapify(pq)
    V[si][sj] = 0
    while pq:
        cnt, ci,cj  = heapq.heappop(pq)
        
        if (ci,cj)==(N-1,N-1):
            return V[ei][ej]

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj]==1 and V[ni][nj]>cnt:
                    V[ni][nj] = cnt
                    heapq.heappush(pq, (cnt, ni,nj))

                elif arr[ni][nj]==0 and V[ni][nj]>cnt+1:
                    V[ni][nj]= cnt+1
                    heapq.heappush(pq, (cnt+1,ni,nj))

print(dijkstra(si,sj))