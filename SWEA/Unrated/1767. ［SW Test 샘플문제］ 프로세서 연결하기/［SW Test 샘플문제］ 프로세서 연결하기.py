T = int(input())


def dfs(n, cnt, l):  # cnt 는 코어 갯수, l은 전선 길이
    global max_core, min_len
    if n == num_core:
        if max_core < cnt:
            max_core = cnt
            min_len = l
        elif max_core == cnt:
            min_len = min(min_len, l)

        return

    si, sj = core_lst[n][0], core_lst[n][1]  # 현재 코어
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        lst = check(si,sj,di,dj)
        if lst:
            for ci,cj in lst:
                v[ci][cj]=1
            dfs(n+1, cnt+1, l+len(lst))
            for ci,cj in lst:
                v[ci][cj]=0
    dfs(n+1, cnt, l)


def check(si,sj,di,dj):
    lst = []
    for mul in range(1,N):
        ni,nj = si+mul*di, sj+mul*dj
        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==0:
            lst.append((ni,nj))
        elif 0<=ni<N and 0<=nj<N and (v[ni][nj]==1 or arr[ni][nj]==1):
            return []
        elif not (0<=ni<N and 0<=nj<N):
            break
    return lst


for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v= [[0]*N for _ in range(N)]
    core_lst = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j]==1:
                core_lst.append((i,j))


    max_core = 0
    min_len = N*N+1
    num_core = len(core_lst)

    dfs(0,0,0)
    print(f'#{tc} {min_len}')