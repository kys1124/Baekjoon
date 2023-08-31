N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0]*N

def dfs(n, lst):
    if n==M:
        print(*lst)
        return

    for i in range(N):
        if v[i]==0:
            v[i]=1
            dfs(n+1, lst+[arr[i]])
            v[i]=0
dfs(0,[])
