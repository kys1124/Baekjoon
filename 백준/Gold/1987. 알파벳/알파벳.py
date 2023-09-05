R,C = map(int, input().split())

arr = [input() for _ in range(R)]
v = [1]*26
a = ord('A')

for i in range(R):
    for j in range(C):
        if v[ord(arr[i][j])-a]==1:
            v[ord(arr[i][j])-a]=0


ans = 0

def dfs(n,ci,cj, cnt):
    global ans
    if ans>=cnt+(N-n):
        return

    if n==N:
        ans =max(ans, cnt)
        return

    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<R and 0<=nj<C and v[ord(arr[ni][nj])-a]==0:
            v[ord(arr[ni][nj])-a]=1
            dfs(n+1, ni,nj,cnt+1)
            v[ord(arr[ni][nj])-a]=0
    dfs(n+1,ci,cj,cnt)

v[ord(arr[0][0])-a]=1
N = v.count(0)
dfs(0,0,0,1)
print(ans)