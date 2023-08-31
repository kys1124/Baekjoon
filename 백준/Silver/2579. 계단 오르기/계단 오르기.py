N = int(input())
stair =[0]+[int(input()) for _ in range(N)]
if N==1:
    print(stair[1])
elif N==2:
    print(stair[2]+stair[1])
else:
    dp = [0]*(N+1)
    dp[1] = stair[1]
    dp[2] = stair[2]+stair[1]

    for i in range(3,N+1):
        dp[i] =max(dp[i-3]+stair[i-1], dp[i-2])+stair[i]

    print(dp[N])