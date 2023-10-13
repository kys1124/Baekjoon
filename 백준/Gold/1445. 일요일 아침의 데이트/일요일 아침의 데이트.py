import heapq
N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='S':
            si,sj = i,j
            arr[i][j]='.'
        elif arr[i][j]=='F':
            ei,ej = i,j

def dijkstra():
    pq = [(0,0,si,sj)]
    v = [[(N*M+1,N*M+1)]*M for _ in range(N)]
    v[si][sj]=(0,0)
    while pq:
        g_cnt, gnear_cnt, ci,cj = heapq.heappop(pq)
        if (ci,cj)==(ei,ej):
            return g_cnt, gnear_cnt

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<M):
                continue
            else:
                if arr[ni][nj]=='g' and (v[ni][nj][0]>g_cnt+1 or (v[ni][nj][0]==g_cnt+1 and v[ni][nj][1]>gnear_cnt)):
                    v[ni][nj] = (g_cnt+1,gnear_cnt)
                    heapq.heappush(pq, (g_cnt+1, gnear_cnt, ni,nj))

                elif arr[ni][nj]=='.':
                    flag = False
                    for ddi,ddj in ((1,0),(-1,0),(0,1),(0,-1)):
                        nni,nnj = ni+ddi,nj+ddj
                        if 0<=nni<N and 0<=nnj<M and arr[nni][nnj]=='g':
                            flag=True
                            break
                    if flag: # 쓰레기 옆
                        if (v[ni][nj][0]>g_cnt or (v[ni][nj][0]==g_cnt and v[ni][nj][1]>gnear_cnt+1)):
                            v[ni][nj]= (g_cnt, gnear_cnt+1)
                            heapq.heappush(pq,(g_cnt,gnear_cnt+1, ni,nj))
                    else:
                        if (v[ni][nj][0]>g_cnt or (v[ni][nj][0]==g_cnt and v[ni][nj][1]>gnear_cnt)):
                            v[ni][nj]=(g_cnt, gnear_cnt)
                            heapq.heappush(pq,(g_cnt,gnear_cnt,ni,nj))

                elif arr[ni][nj]=='F':
                    heapq.heappush(pq,(g_cnt, gnear_cnt,ni,nj))
print(*dijkstra())
