N,M = map(int, input().split())
def dfs(n,s,lst):
    if n==M:
        print(*lst)
        return


    for i in range(s,N):
        dfs(n+1,i,lst+[i+1])

dfs(0,0,[])