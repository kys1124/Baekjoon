N,M = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0]*(N+1)
sm = 0
for i in range(N):
    sm += lst[i]
    arr[i+1] = sm

ans = []
for _ in range(M):
    i,j = map(int, input().split())
    ans.append(arr[j]-arr[i-1])

for x in ans:
    print(x)
