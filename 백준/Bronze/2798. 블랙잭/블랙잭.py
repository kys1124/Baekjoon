N,M =map(int, input().split())
numlst = list(map(int, input().split()))
ans =0
def dfs(n, s, sm):
    global  ans
    if sm>M:
        return

    if n==3:
        ans = max(ans, sm)
        return


    for i in range(s,N):
        dfs(n+1,i+1, sm+numlst[i])

dfs(0,0,0)
print(ans)