N,M = map(int, input().split())
candy = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

for i in range(1,N+1):
    for j in range(1,M+1):
        candy[i][j] += max(candy[i-1][j-1],candy[i-1][j], candy[i][j-1])

print(candy[N][M])