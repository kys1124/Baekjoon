N = int(input())
P = list(map(int, input().split()))

time = [0]*(N+1)
time[0] = 0
P.sort()
sm = 0
for i in range(N):
    time[i+1]=time[i]+P[i]
    sm +=time[i]
print(sm+time[-1])