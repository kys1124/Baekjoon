lst = list(map(int,input().split()))
mal = [0,0,0,0]

adj = [[1], [2], [3], [4], [5], [6,21],
       [7],[8],[9],[10],[11,24],
       [12],[13],[14],[15],[16,26],
       [17],[18],[19],[20],[32],
       [22],[23],[29],[25],[29],
       [27],[28],[29],[30],[31],[20],[32]]

score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
         34,36,38,40,13,16,19,22,24,28,27,26,25,30,35,0]

ans = 0
def dfs(n, sm):
    global ans, mal
    if n==10:
        ans = max(ans, sm)
        return

    for i in range(4):
        num = lst[n]
        copy_mal = mal[:]
        cur = mal[i]
        if cur in (5, 10, 15):
            cur = adj[cur][1]
            num-=1
        for _ in range(num):
            cur = adj[cur][0]
        mal[i] = cur
        if cur==32 or cur not in (mal[(i+1)%4], mal[(i+2)%4], mal[(i+3)%4]):
            dfs(n+1, sm+score[cur])
        mal = copy_mal
dfs(0,0)
print(ans)