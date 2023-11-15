import heapq
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bridge =set()
for i in range(N):
    for j in range(N):
        flag1, flag2 = True, True
        if arr[i][j]==0:
            for di,dj in ((1,0),(-1,0)):
                ni,nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
                    flag1 = False
            for di,dj in ((0,1),(0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    flag2 = False
            if flag1 or flag2:
                bridge.add((i,j))

def bfs():
    pq= [(0,0,0,0)]
    heapq.heapify(pq)
    v = [[[1234567]*N for _ in range(N)] for _ in range(2)]
    v[0][0][0]=0
    while pq:
        cnt, flag, ci, cj=heapq.heappop(pq)
        if (ci,cj)==(N-1,N-1):
            return v[flag][ci][cj]

        if flag==0:
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[0][ni][nj]>cnt+1 and arr[ni][nj]==1:
                    v[0][ni][nj]=cnt+1
                    heapq.heappush(pq,(cnt+1, 0, ni,nj))
                elif 0<=ni<N and 0<=nj<N and (ni,nj) in bridge and v[1][ni][nj]>cnt+M-(cnt%M) and arr[ci][cj]==1:
                        v[1][ni][nj] = cnt+M-(cnt%M)
                        heapq.heappush(pq, (v[1][ni][nj], 1, ni,nj))

                elif 0<=ni<N and 0<=nj<N and arr[ni][nj]>1 and v[0][ni][nj]>cnt+arr[ni][nj]-(cnt%arr[ni][nj]) and arr[ci][cj]==1:
                        v[0][ni][nj] = cnt+arr[ni][nj]-(cnt%arr[ni][nj])
                        heapq.heappush(pq, (v[0][ni][nj], 0, ni,nj))

        else:
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[1][ni][nj]>cnt+1 and arr[ni][nj]==1:
                    v[1][ni][nj]=cnt+1
                    heapq.heappush(pq,(cnt+1, 1, ni,nj))
                elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 1 and v[1][ni][nj] > cnt+arr[ni][nj]-(cnt%arr[ni][nj]) and arr[ci][cj]==1:
                        v[0][ni][nj] = cnt+arr[ni][nj]-(cnt%arr[ni][nj])
                        heapq.heappush(pq, (v[0][ni][nj], 1, ni, nj))

print(bfs())