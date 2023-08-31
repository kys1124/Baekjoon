N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

cnt = 0
for x in coin[::-1]:
    if K//x:
        cnt += K//x
        K %= x

    if K==0:
        break
print(cnt)