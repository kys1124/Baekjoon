lst = list(map(int, input().split()))

ans = 0
def dfs(n,i_1,i_2, sm):
    global ans
    if 10-n+sm<5:
        return

    if n==10:
        if sm>=5:
            ans+=1
        return

    for i in range(1,6):
        if not (i_1==i and i_2==i):
            if lst[n]==i:
                dfs(n+1,i,i_1,sm+1)
            else:
                dfs(n+1,i,i_1,sm)

dfs(0,0,0,0)
print(ans)