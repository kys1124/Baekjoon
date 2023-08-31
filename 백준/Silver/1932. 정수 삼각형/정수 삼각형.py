N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(1,len(arr[i])-1):
        arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])
    arr[i][0]+=arr[i-1][0]
    arr[i][-1]+=arr[i-1][-1]

print(max(arr[-1]))