N , M = map(int, input().split())
arr =[list(input()) for _ in range(N)]

dir = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
v = [[[-1]*M for _ in range(N)] for _ in range(2)]
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='B':
            if i==0 and j<M-1:
                sd=0
            elif j==M-1 and i<N-1:
                sd=1
            elif i==N-1 and j>0:
                sd=2
            else:
                sd=3
            q.append((i,j,0,sd))
            v[0][i][j]=0
        elif arr[i][j]=='A':
            q.append((i,j,1,0))
            v[1][i][j]=0

def bfs(q):
    cnt = 0
    while q:
        temp_q = []
        for i in range(len(q)):
            ci,cj,flag,cd = q[i]
            if flag==0: # 가장자리 돌기.
                di,dj = dir[cd]
                ni,nj = ci+di,cj+dj
                if not (0<=ni<N and 0<=nj<M):
                    cd = (cd+1)%4
                    ni,nj =ci+dir[cd][0], cj+dir[cd][1]
                    if v[0][ni][nj]==-1:
                        v[0][ni][nj]=cnt+1
                        if v[1][ni][nj]!=-1 and v[1][ni][nj]%(2*M+2*N-4)==(v[0][ni][nj]):
                            return cnt+1
                        temp_q.append((ni,nj,flag, cd))
                elif v[0][ni][nj]==-1:
                    v[0][ni][nj]=cnt+1
                    if v[1][ni][nj]!=-1 and v[1][ni][nj]%(2*M+2*N-4)==(v[0][ni][nj]):
                        return cnt+1
                    temp_q.append((ni,nj,flag,cd))

            else:
                for i in range(4):
                    di,dj = dir[i]
                    ni,nj= ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<M and v[1][ni][nj]==-1 and arr[ni][nj]!='G':
                        v[1][ni][nj]=cnt+1
                        if v[1][ni][nj]%(2*M+2*N-4)==(v[0][ni][nj]):
                            return cnt+1
                        temp_q.append((ni,nj,flag,cd))


        cnt+=1
        q= temp_q
    return -1
print(bfs(q))
