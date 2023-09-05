dice = list(map(int, input().split()))

graph  = [[1],[2],[3],[4],[5],[6,22],[7],[8],[9],[10],
          [11,25],[12],[13],[14],[15],[16,27],[17],[18],
          [19],[20],[21],[21],[23],[24],[30],[26],[30],
          [28],[29],[30],[31],[32],[20],[21]]

# 도착 -> 21
score = [0,2,4,6,8,10,12,14,16,18,20,22,24,
         26,28,30,32,34,36,38,40,0,
         13,16,19,22,24,28,27,26,
         25,30,35] # index 맞추기 위해 앞에 0 패딩, 도착 index 21은 0점


ans = 0
a = [0,0,0,0]
def dfs(n, sm):
    global ans
    if n==10:
        ans= max(ans, sm)
        return

    for i in range(4):
        temp = a[i]
        if a[i] not in (5,10,15):
            for _ in range(dice[n]):
                a[i] = graph[a[i]][0]
        else:
            a[i] = graph[a[i]][1]
            for _ in range(dice[n]-1):
                a[i] = graph[a[i]][0]

        if a[i]==21 or (a[i]!=a[(i+1)%4] and a[i]!=a[(i+2)%4] and a[i]!=a[(i+3)%4]):
            dfs(n+1, sm+score[a[i]])

        a[i]= temp

dfs(0,0)
print(ans)