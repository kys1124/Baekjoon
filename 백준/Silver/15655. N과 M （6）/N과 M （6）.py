N,M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
def dfs(n,idx, lst):
    if n==M:
        print(*lst)
        return

    for i in range(idx, N):
        dfs(n+1,i+1, lst+[arr[i]])
dfs(0,0,[])