def dfs(si,sj, cnt, dist,v):
    global ans
    if cnt>=ans:
        return

    if dist==empty:
        ans = min(ans, cnt)
        return

    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        for mul in range(1,mx):
            ni,nj = si+mul*di, sj+mul*dj
            if v[ni][nj]=='.':
                v[ni][nj]='*'
            else:
                break
        if mul>1:
            dfs(si+(mul-1)*di, sj+(mul-1)*dj, cnt+1, dist+mul-1, v)
            for mul2 in range(1,mul):
                v[si+mul2*di][sj+mul2*dj]='.'

tc = 1
while True:
    try:
        N,M = map(int, input().split())
        arr =[['*']*(M+2)]+[['*']+list(map(str, input()))+['*'] for _ in range(N)]+[['*']*(M+2)]
        empty=0
        start_lst = []
        ans = 1000001
        v = [arr[i][:] for i in range(N+2)]
        mx = max(N+2, M+2)
        for i in range(1,N+1):
            for j in range(1,M+1):
                if arr[i][j]=='.':
                    empty+=1
                    start_lst.append((i,j))

        for ci,cj in start_lst:
            v[ci][cj]='*'
            dfs(ci,cj,0,1,v)
            v[ci][cj]='.'
        if ans==1000001:
            ans=-1
        print(f'Case {tc}: {ans}')
        tc +=1
    except:
        break