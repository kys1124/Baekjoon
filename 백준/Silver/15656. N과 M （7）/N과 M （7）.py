N,M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
def dfs(n,lst):
    if n==M:
        print(*lst)
        return

    for i in range(N):
        dfs(n+1, lst+[arr[i]])

dfs(0,[])