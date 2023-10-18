N, M, H = map(int, input().split()) # 세로선 수, 가로 연결 수, 가로 선 수
arr = [[0]*(2*N+1) for _ in range(2*H+1)]
col,row = 2*N+1, 2*H+1

for i in range(row):
    for j in range(1,col,2):
        arr[i][j]=1

for _ in range(M):
    a,b = map(int, input().split())
    arr[2*a-1][2*b]=1

line = []
for i in range(1,row-1,2):
    for j in range(2,col-1,2):
        if arr[i][j-2]==0 and arr[i][j+2]==0 and arr[i][j]==0:
            line.append((i,j))

def check(sj):
    stk = [(0,sj)]
    v = [[0]*col for _ in range(row)]
    v[0][sj]=1
    while stk:
        ci,cj = stk.pop()
        if ci==2*H:
            if cj==sj:
                return True
            else:
                return False
        for di,dj in ((0,1),(0,-1),(1,0)):
            ni,nj = di+ci,dj+cj
            if 0<=ni<row and 0<=nj<col and v[ni][nj]==0 and arr[ni][nj]==1:
                stk.append((ni,nj))
                v[ni][nj]=1
                break

def check_line(ci,cj):
    if arr[ci][cj-2]==0 and arr[ci][cj+2]==0:
        if ci==1 or ci==row-2:
            return True
        elif arr[ci-2][cj-2]==1 or arr[ci-2][cj]==1 or arr[ci-2][cj+2]==1\
            or arr[ci+2][cj-2]==1 or arr[ci+2][cj]==1 or arr[ci+2][cj+2]==1:
            return True
    return False


def dfs(n, s, lst,t):
    global flag, ans
    if flag:
        ans = t
        return

    if n==t:
        for num in range(1,col,2):
            if not check(num):
                break
        else:
            flag=True
        return

    for i in range(s, len(line)):
        ci,cj =  line[i]
        if check_line(ci,cj):
            arr[ci][cj]=1
            dfs(n+1, i+1, lst+[line[i]],t)
            arr[ci][cj]=0
t = 0
ans = 4
while t<=3:
    flag = False
    dfs(0,0,[],t)
    if flag:
        ans = t
        break
    else:
        t+=1

if ans==4:
    print(-1)
else:
    print(ans)