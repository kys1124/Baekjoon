N =int(input())
arr= [list(map(int, input().split())) for _ in range(N)]


lst2 = [[] for _ in range(2*N-1)]

v1=[0]*(2*N) # 왼위->오른아래 대각

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            lst2[i+j].append((i,j))

ans=0
def dfs(n, cnt):
    global ans
    if ans>=2*N-1-n+cnt:
        return
    if n==2*N-1:
        ans = max(ans, cnt)
        return

    for ci,cj in lst2[n]:
        if v1[ci-cj]==0:
            v1[ci-cj]=1
            dfs(n+1, cnt+1)
            v1[ci-cj]=0
    dfs(n+1,cnt)

dfs(0,0)
print(ans)