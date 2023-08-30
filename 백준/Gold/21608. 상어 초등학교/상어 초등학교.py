N = int(input())
arr =[[0]*N for _ in range(N)]
dic = dict()
for _ in range(N**2):
    c,n1,n2,n3,n4 = map(int, input().split())
    dic[c] = set([n1,n2,n3,n4])
    si,sj,mxlike,mxempty = N,N,-1,-1
    for i in range(N):
        for j in range(N):
            if arr[i][j]==0:
                like =0
                empty=0
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] in dic[c]:
                            like+=1
                        if arr[ni][nj]==0:
                            empty+=1

                if like>mxlike:
                    mxlike= like
                    mxempty= empty
                    si,sj = i,j

                elif like==mxlike:
                    if empty>mxempty:
                        mxempty=empty
                        si,sj=i,j
                    elif mxempty==empty:
                        if si>i:
                            si,sj =i,j
                        elif si==i:
                            if sj>j:
                                si,sj =i,j

    arr[si][sj]=c

ans = 0
for i in range(N):
    for j in range(N):
        temp = 0
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in dic[arr[i][j]]:
                    temp +=1

        if temp==1:
            ans +=temp
        elif temp==2:
            ans +=10
        elif temp==3:
            ans +=100
        elif temp==4:
            ans +=1000
print(ans)
