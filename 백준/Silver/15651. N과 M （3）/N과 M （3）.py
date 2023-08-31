N,M = map(int, input().split())


def dfs(n,lst  ):
    if n==M:
        print(*lst)
        return

    for i in range(N):
        dfs(n+1,lst+[i+1])

dfs(0,[])
