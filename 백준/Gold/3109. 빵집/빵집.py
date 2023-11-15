R,C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
v = [[0]*C for _ in range(R)]
def dfs(si,sj):
    stk = [(si,sj)]
    while stk:
        ci,cj = stk.pop()
        if v[ci][cj]==1:
            continue
        if cj==C-1:
            return 1
        v[ci][cj]=1

        for di,dj in ((1,1),(0,1),(-1,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and v[ni][nj]==0 and arr[ni][nj]=='.':
                stk.append((ni,nj))
    return 0

ans = 0
for i in range(R):
    ans += dfs(i,0)
print(ans)