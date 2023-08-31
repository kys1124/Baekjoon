T = int(input())
for _ in range(T):
    N = int(input())
    arr= [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*N for _ in range(3)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = 0
    for j in range(1,N):
        dp[0][j] = max(dp[2][j-1]+arr[0][j], dp[1][j-1]+arr[0][j])
        dp[1][j] = max(dp[2][j-1]+arr[1][j], dp[0][j-1]+arr[1][j])
        dp[2][j] = max(dp[2][j-1], dp[0][j-1], dp[1][j-1])
    print(max(dp[0][N-1], dp[1][N-1], dp[2][N-2]))