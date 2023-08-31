N = int(input())


def dfs(n, lst):
    if n==N:
        print(*lst)
        return

    for i in range(N):
        if v[i]==0:
            v[i]=1
            dfs(n+1, lst+[i+1])
            v[i]=0
v = [0]*N
dfs(0,[])