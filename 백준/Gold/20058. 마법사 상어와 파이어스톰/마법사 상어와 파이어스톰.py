N, Q=  map(int, input().split())
N=2**N
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

def rotate(arr, L):
    new_arr = [[0]*N for _ in range(N)]
    for si in range(0,N,L):
        for sj in range(0,N,L):
            for i in range(L):
                for j in range(L):
                    new_arr[si+i][sj+j] = arr[si+(L-1-j)][sj+i]
    return new_arr



for l in lst:
    L = 2**l
    arr = rotate(arr, L)
    lst= []
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:
                temp = 0
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = i+di,j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0:
                        temp+=1
                if temp<3:
                    lst.append((i,j))
    for ci,cj in lst:
        arr[ci][cj]-=1

def dfs(si,sj,idx):
    stk = [(si,sj)]
    v[si][sj]=idx
    amt = arr[si][sj]
    cnt=1
    while stk:
        ci,cj = stk.pop()

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj =ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>0:
                stk.append((ni,nj))
                v[ni][nj]=idx
                amt+=arr[ni][nj]
                cnt+=1
    return amt, cnt

idx =1
ans1 = 0
ans2 = 0
v = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if v[i][j]==0 and arr[i][j]>0:
            amt, cnt = dfs(i,j,idx)
            ans1+=amt
            ans2 = max(ans2, cnt)
            idx+=1

print(ans1)
print(ans2)