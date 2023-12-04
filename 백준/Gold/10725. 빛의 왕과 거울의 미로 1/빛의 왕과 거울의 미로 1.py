N,M,x,y = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dir = {0:(0,1),1:(0,-1),2:(-1,0),3:(1,0)}
dir_1 = {0:2,2:0,3:1,1:3}
dir_2 = {0:3,3:0,1:2,2:1}
ans = 0
cmd = ['.','/',"\\"]
v = [[[0]*M for _ in range(N)] for _ in range(4)]
def find(x):
    if 1<=x<=M:
        si,sj,sd = -1,x-1,3
    elif M+1<=x<=M+N:
        si,sj,sd = x-M-1,-1,0
    elif M+N+1<=x<=M+N+N:
        si,sj,sd = x-M-N-1, M,1
    else:
        si,sj,sd = N, x-M-2*N-1,2
    return si,sj,sd

si,sj,sd = find(x)
ei,ej,_ = find(y)

def go(si,sj,sd, ei,ej, arr):
    v =[[[0]*M for _ in range(N)] for _ in range(4)]
    while True:
        ni,nj = si+dir[sd][0], sj+dir[sd][1]
        if (ni,nj)==(ei,ej):
            return True
        if not (0<=ni<N and 0<=nj<M):
            return False
        if v[sd][ni][nj]==1:
            return False
        v[sd][ni][nj]=1
        if arr[ni][nj]=='/':
            sd = dir_1[sd]
        elif arr[ni][nj]=="\\":
            sd = dir_2[sd]
        si,sj= ni,nj

def dfs(n, arr):
    global ans
    if n==N*M:
        if go(si,sj,sd,ei,ej, arr):
            ans+=1
        return

    ci,cj = n//M, n%M
    if arr[ci][cj]=='?':
        for c in cmd:
            arr[ci][cj]=c
            dfs(n+1, arr)
            arr[ci][cj]='?'
    else:
        dfs(n+1, arr)


dfs(0, arr)
print(ans%10007)