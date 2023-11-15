R,C = map(int, input().split())
arr =[input() for _ in range(R)]
dir = {0:(-1,1), 1:(0,1),2:(1,1)}

def dfs(ni,nj):
    global ans, flag
    if flag:
        return

    if nj==C-1:
        ans +=1
        flag=True
        return

    if 0<=ni<R and 0<=nj<C and v[ni][nj]==0 and arr[ni][nj]!='x':
        v[ni][nj]=1
        for i in range(3):
            dfs(ni+dir[i][0],nj+1)


v = [[0]*C for _ in range(R)]
ans = 0
for i in range(R):
    flag= False
    dfs(i,0)
print(ans)