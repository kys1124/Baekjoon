N,K = map(int, input().split())
lst = [0]+[list(map(int, input().split())) for _ in range(N)]

v = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if lst[i][0]>j:
            v[i][j] = v[i-1][j]
        else:
            v[i][j]= max(v[i-1][j],v[i-1][j-lst[i][0]]+lst[i][1])

print(v[N][K])