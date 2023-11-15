R,C = map(int, input().split()) # RxC
arr = [list(map(str, input())) for _ in range(R)] #. 빈칸 x 미네랄
N = int(input()) # 막대 던진 횟수
lst = list(map(lambda x:R-int(x), input().split())) #막대 던진 높이 1<=높이<=R
group =dict()
def dfs(si,sj,idx):
    stk = [(si,sj)]
    v[si][sj]= idx
    cnt = 1
    while stk:
        ci, cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<R and 0<=nj<C and v[ni][nj]==0 and arr[ni][nj]=='x':
                stk.append((ni,nj))
                v[ni][nj]=idx
                cnt+=1
    group[idx] = cnt


def check(si,sj):
    visited = [[0]*C for _ in range(R)]
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni,nj = si+di,sj+dj
        if 0<=ni<R and 0<=nj<C and arr[ni][nj]=='x' and visited[ni][nj]==0:
            lst =[(ni,nj)]
            stk = [(ni,nj)]
            visited[ni][nj]=1
            flag=True
            while stk:
                ci,cj = stk.pop()
                if ci==R-1:
                    flag =False
                for ddi,ddj in  ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nni, nnj = ddi+ci,ddj+cj
                    if 0<=nni<R and 0<=nnj<C and visited[nni][nnj]==0 and arr[nni][nnj]=='x':
                        visited[nni][nnj]=1
                        stk.append((nni,nnj))
                        lst.append((nni,nnj))
            if flag:
                return lst
    return []

for turn, h in enumerate(lst):
    v = [[0]*C for _ in range(R)]
    idx = 1
    for i in range(R):
        for j in range(C):
            if arr[i][j]=='x' and v[i][j]==0:
                dfs(i,j,idx)
                idx+=1

    if turn%2 == 0:
        si, sj, sd  = h, 0, 1
    else:
        si, sj, sd = h, C-1, -1

    for mul in range(C):
        ni,nj = si, sj+mul*sd
        if v[ni][nj]!=0:
            arr[ni][nj] = '.'
            new_group = check(ni,nj)
            break
    else:
        new_group = []

    if new_group:
        new_group.sort(key=lambda x:(-x[0],x[1]))
        for ci,cj in new_group:
            v[ci][cj]=-1
        mncnt = R
        strat_col = -1
        for ci,cj in new_group:
            if v[ci+1][cj]==-1:
                continue
            cnt = 0
            for i in range(ci+1,R):
                if arr[i][cj]=='.':
                    cnt+=1
                elif i<=ci+mncnt and v[i][cj]==-1:
                    cnt+=1
                else:
                    break
            mncnt = min(mncnt,cnt)
        for ci,cj in new_group:
            arr[ci][cj]='.'
            arr[ci+mncnt][cj]='x'

for x in arr:
    print(*x, sep='')