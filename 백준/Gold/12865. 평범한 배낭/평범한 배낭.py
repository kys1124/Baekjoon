N, K = map(int, input().split())
value = [0]
weight = [0]
for _ in range(N):
    w,v = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,1+K):
        if weight[i]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value[i]+dp[i-1][j-weight[i]], dp[i-1][j])
print(dp[N][K])