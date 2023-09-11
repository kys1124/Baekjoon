N = int(input())
target = int(input())

r,c = -1,-1
dir = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
arr = [[0]*N for _ in range(N)]
n = 1
ci,cj = N//2, N//2
cnt = 1
d = 3
while n<=N**2:
    if n==target:
        r,c = ci,cj

    arr[ci][cj]=n

    if cnt <int(n**(1/2)):
        ni,nj  = ci+dir[d][0], cj+dir[d][1]
        cnt+=1
    else:
        d = (d+1)%4
        ni, nj = ci + dir[d][0], cj + dir[d][1]
        cnt=1
    ci,cj = ni,nj
    n+=1

for x in arr:
    print(*x)
print(r+1,c+1)