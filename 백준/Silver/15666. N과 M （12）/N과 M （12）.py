N,M = map(int, input().split())

arr= sorted(map(int, set(input().split())))

def dfs(n, s, lst):
    if n==M:
        print(*lst)
        return

    for i in range(s,len(arr)):
        dfs(n+1,i, lst+[arr[i]])

dfs(0,0,[])
