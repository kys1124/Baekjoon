lst = list(map(int, input().split()))
sm = 0
for x in lst:
    sm +=x**2
print(sm%10)