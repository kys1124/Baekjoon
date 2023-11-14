N, M, H  = map(int, input().split())
arr = [[0]*(2*N+1) for _ in range(2*H+1)]
for i in range(2*H+1):
    for j in range(1,2*N+1,2):
        arr[i][j]=1

for _ in range(M):
    a,b = map(int, input().split())
    arr[2*a-1][2*b]=1

lst = []
for i in range(1,2*H+1,2):
    for j in range(2,2*N,2):
        if arr[i][j-2]==0 and arr[i][j]==0 and arr[i][j+2]==0:
            lst.append((i,j))

def dfs(i,arr):
    stk = [(0,i)]
    v = [[0]*(2*N+1) for _ in range(2*H+1)]
    v[0][i]=1
    while stk:
        ci,cj = stk.pop()
        if ci==2*H:
            if cj==i:
                return True
            else:
                return False

        for di,dj in ((0,1),(0,-1),(1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<2*H+1 and 1<=nj<2*N+1 and arr[ni][nj]==1 and v[ni][nj]==0:
                stk.append((ni,nj))
                v[ni][nj]=1
                break

def check(si,sj, arr):
    if si==1 or si==2*H-1:
        if arr[si][sj-2]==0 and arr[si][sj+2]==0:
            return True
        else:
            return False
    else:
        if arr[si][sj-2]==0 and arr[si][sj+2]==0:
            if arr[si-2][sj-2]==1 or arr[si-2][sj]==1 or arr[si-2][sj+2]==1 or arr[si+2][sj-2]==1 or arr[si+2][sj]==1 or arr[si+2][sj+2]==1:
                return True
        return False

def dfs2(n,k,s, arr):
    global flag
    if flag:
        return
    if n==k:
        for i in range(1,2*N,2):
            if dfs(i,arr):
                continue
            else:
                break
        else:
            flag=True
        return

    for i in range(s, len(lst)):
        si,sj = lst[i]
        if check(si,sj,arr):
            arr[si][sj]=1
            dfs2(n+1, k, i+1, arr)
            arr[si][sj]=0

ans = 4
# for x in arr:
#     print(*x)

for i in range(1,2*N,2):
    if dfs(i, arr):
        continue
    else:
        break
else:
    ans = 0
    print(ans)

if ans==4:
    flag = False
    for k in range(1,4):
        dfs2(0,k,0,arr)
        if flag:
            ans = k
            break
    if ans==4:
        print(-1)
    else:
        print(ans)
