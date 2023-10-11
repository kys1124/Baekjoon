import heapq
W,H= map(int, input().split())
arr = [['H']*(W+2)] + [['H']+list(map(str, input()))+['H'] for _ in range(H)] +[['H']*(W+2)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if arr[i][j]=='T':
            si,sj = i,j
            arr[i][j]='0'
        elif arr[i][j]=='E':
            ei,ej = i,j


def dijkstra(si,sj):
    pq = [(0,si,sj)]
    v =[[100000000]*(W+2) for _ in range(H+2)]
    v[si][sj]=0
    while pq:
        ct, ci,cj = heapq.heappop(pq)

        if (ci,cj)==(ei,ej):
            return v[ei][ej]


        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            flag = False
            nxt = 0
            for mul in range(1,max(W+2,H+2)):
                ni,nj = ci+mul*di, cj+mul*dj
                if arr[ni][nj]=='H':
                    break

                elif arr[ni][nj]=='R':
                    ni,nj = ci+(mul-1)*di, cj+(mul-1)*dj
                    flag=True
                    break

                elif arr[ni][nj]=='E':
                    flag=True
                    break
                else:
                    nxt += int(arr[ni][nj])

            if flag:
                if v[ni][nj]>ct+nxt:
                    heapq.heappush(pq,(ct+nxt,ni,nj))
                    v[ni][nj]=ct+nxt

    return -1
print(dijkstra(si,sj))
