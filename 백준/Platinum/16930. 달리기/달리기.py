N,M,K = map(int, input().split())
arr = [['#']*(M+2)]+[['#']+list(input())+['#'] for _ in range(N)]+[['#']*(M+2)]
si,sj,ei,ej = map(int, input().split())

def bfs():
    v = [[N*M+1]*(M+2) for _ in range(N+2)]
    v[si][sj]=1
    q =[(si,sj)]
    cnt = 1
    while q:
        new_q =[]
        for i in range(len(q)):
            ci,cj = q[i]
            if (ci,cj)==(ei,ej):
                return v[ci][cj]-1

            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci,cj
                for _ in range(K):
                    ni+=di
                    nj+=dj
                    if v[ni][nj]>cnt+1 and arr[ni][nj]=='.':
                        v[ni][nj]=cnt+1
                        new_q.append((ni,nj))
                    elif v[ni][nj]==cnt+1 and arr[ni][nj]=='.':
                        continue
                    else:
                        break
        q = new_q
        cnt+=1

    return -1
print(bfs())