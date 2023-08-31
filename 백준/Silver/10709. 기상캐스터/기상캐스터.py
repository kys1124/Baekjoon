h, w = map(int, input().split())

city = [list(map(','.join, input())) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if city[i][j]=='c':
            city[i][j]=0
        else:
            city[i][j]=-1

for i in range(h):
    time = -1
    for j in range(w):
        if city[i][j]==0:
            time = max(time, j)
            continue
        else:
            if time<0:
                city[i][j] = -1
            else:
                city[i][j] = j-time
    print(*city[i])
