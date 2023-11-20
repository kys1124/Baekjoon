T = int(input())
for tc in range(1,1+T):
    N, L = map(int, input().split())
    score = [0]
    cal = [0]
    for _ in range(N):
        t,k = map(int, input().split())
        score.append(t)
        cal.append(k)
    dp = [[0]*(L+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,L+1):
            if cal[i]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-cal[i]]+score[i],dp[i-1][j])
    print(f'#{tc} {dp[N][L]}')