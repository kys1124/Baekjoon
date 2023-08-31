N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def dfs(n,s,lst):

    if n==M:
        print(*lst)
        return

    for i in range(s,N):
        dfs(n+1, i, lst+[arr[i]])

dfs(0,0,[])