N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            chicken.append((i,j))
        elif arr[i][j]==1:
            house.append((i,j))

def bfs2(si,sj,lst):
    mn = 1e9
    for ci, cj in lst:
        mn = min(mn, abs(ci-si)+abs(cj-sj))
    return mn

def dfs(n, sm, lst):
    global ans
    if sm>=ans:
        return

    if n==len(house):
        ans = min(ans, sm)
        return

    dfs(n+1, sm+bfs2(house[n][0],house[n][1], lst), lst)

def combi(n,s, lst):
    if n==M:
        dfs(0,0,lst)
        return

    for i in range(s,len(chicken)):
        combi(n+1, i+1, lst+[chicken[i]])

ans = 1e9
combi(0,0,[])

print(ans)