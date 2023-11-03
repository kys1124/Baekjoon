N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
def dfs(si,sj):
    stk = [(si,sj)]
    v[si][sj]=1
    cnt = 1
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==1:
                v[ni][nj]=1
                stk.append((ni,nj))
                cnt+=1
    return cnt

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            ans.append(dfs(i,j))
ans.sort()
print(len(ans))
for x in ans:
    print(x)