W,H = map(int, input().split())

arr = [list(map(str, input())) for _ in range(H)]

cc =[]
for i in range(H):
    for j in range(W):
        if arr[i][j]=='C':
            cc.append((i,j))

si,sj = cc[0][0],cc[0][1]
ei,ej = cc[1][0],cc[1][1]

v = [[H*W+1]*W for _ in range(H)]
V = [[[0]*W for _ in range(H)] for _ in range(4)]
d = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}

import heapq
def dijkstra():
    q = [(0,0,si,sj),(0,1,si,sj),(0,2,si,sj),(0,3,si,sj)]
    heapq.heapify(q)
    v[si][sj] = 0
    for i in range(4):
        V[i][si][sj]=1

    while q:
        cur_cnt,cur_d, ci,cj = heapq.heappop(q)

        if ci==ei and cj==ej:
            return v[ei][ej]

        for i in range(4):
            ni,nj = ci+d[i][0], cj+d[i][1]
            if i==cur_d:
                if 0<=ni<H and 0<=nj<W and arr[ni][nj]!='*' and v[ni][nj]>=cur_cnt:
                    v[ni][nj]=cur_cnt
                    heapq.heappush(q, (cur_cnt, cur_d, ni,nj))

            else:
                if 0<=ni<H and 0<=nj<W and arr[ni][nj]!='*' and v[ni][nj]>=cur_cnt+1 and V[i][ni][nj]==0:
                    V[i][ni][nj]=1
                    v[ni][nj]=cur_cnt+1
                    heapq.heappush(q,(cur_cnt+1, i,ni,nj))

print(dijkstra())