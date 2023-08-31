N,M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

s = set()
def dfs(n, lst):
    if n==M:
        if tuple(lst) not in s:
            s.add(tuple(lst))
            print(*lst)
        return

    for i in range(N):
        dfs(n+1, lst+[arr[i]])

dfs(0,[])