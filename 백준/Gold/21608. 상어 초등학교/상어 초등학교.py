N = int(input())
dic = {}
arr =[[0]*N for _ in range(N)]
for _ in range(N**2):
    student, *like_lst = list(map(int, input().split()))
    dic[student] = set(like_lst)

    mi,mj,mx_empty, mx_like = N,N,-1,-1
    for i in range(N):
        for j in range(N):
            if arr[i][j]==0:
                empty, like = 0,0
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj]==0:
                            empty+=1
                        elif arr[ni][nj] in dic[student]:
                            like+=1
                if like>mx_like:
                    mx_empty, mx_like, mi, mj = empty, like, i, j
                elif like==mx_like:
                    if empty>mx_empty:
                        mx_empty, mi,mj = empty, i, j
                    elif empty==mx_empty:
                        if i<mi:
                            mi,mj = i,j
                        elif i==mi:
                            if j<mj:
                                mj = j

    arr[mi][mj] = student

ans = 0
for i in range(N):
    for j in range(N):
        like=0
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = di+i, dj+j
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] in dic[arr[i][j]]:
                like+=1
        if like==0:
            continue
        else:
            ans+= 10**(like-1)
print(ans)