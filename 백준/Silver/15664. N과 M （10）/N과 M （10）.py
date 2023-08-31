N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

v = set()

def dfs(n, s,lst):
    if n==M:
        if tuple(lst) not in v:
            v.add(tuple(lst))
            print(*lst)
        return

    for i in range(s, N):
        dfs(n+1, i+1, lst+[arr[i]])

dfs(0, 0, [])