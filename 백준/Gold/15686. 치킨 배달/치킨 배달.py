N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house =[]
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            house.append((i,j))
        elif arr[i][j]==2:
            chicken.append((i,j))
ans = 123456789
def dfs(n,s,lst):
    global ans
    if n==M:
        total_dist = 0
        for ci,cj in house:
            dist = N**2
            for di,dj in lst:
                cur = abs(ci-di)+abs(cj-dj)
                if dist>cur:
                    dist=cur
            total_dist+=dist
        ans  = min (ans, total_dist)
        return

    for i in range(s,len(chicken)):
        dfs(n+1, i+1, lst+[chicken[i]])
dfs(0,0,[])
print(ans)