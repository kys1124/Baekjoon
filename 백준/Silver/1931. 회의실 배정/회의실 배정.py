import sys
input =sys.stdin.readline

N = int(input())
time =  sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1],x[0]))

start = time[0][0]
ans = 0
for (x,y) in time:
    if start<=x:
        ans +=1
        start=y
        continue
    else:
        continue
print(ans)
