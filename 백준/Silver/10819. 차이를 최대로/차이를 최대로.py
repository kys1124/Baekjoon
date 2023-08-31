N = int(input())
arr = list(map(int, input().split()))

v = [0]*N
ans = 0
def dfs(n, sm ,lst):
    global ans
    if n ==N:
        ans = max(ans, sm-abs(lst[1]))
        return

    for i in range(N):
        if v[i]==0:
            v[i]=1
            dfs(n+1,sm+abs(lst[-1]-arr[i]), lst+[arr[i]])
            v[i]=0

dfs(0,0,[0])

print(ans)