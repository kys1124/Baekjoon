C,R = map(int, input().split()) # 가로 세로
K = int(input())
dir = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
arr=  [[0]*C for _ in range(R)]
if K>C*R:
    print(0)
else:
    si,sj = 0,0
    d = 0
    for k in range(1,K+1):
        arr[si][sj] = k
        if k==K:
            break
        ni,nj = si+dir[d][0], sj+dir[d][1]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj]==0:
            si,sj = ni,nj
        else:
            d = (d+1)%4
            si,sj = si+dir[d][0], sj+dir[d][1]

    print(sj+1,si+1)