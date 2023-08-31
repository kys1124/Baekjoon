lst = list(map(int, input().split()))
chess = [1,1,2,2,2,8]

ans = []
for i in range(6):
    ans.append(chess[i]-lst[i])

print(*ans)
