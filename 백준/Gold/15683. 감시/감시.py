N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctv = []
empty= 0 # 빈칸 개수
for i in range(N):
    for j in range(M):
        if arr[i][j]!=0 and arr[i][j]!=6:
            cctv.append((i,j,arr[i][j])) #cctv 리스트에 좌표와 type 저장.
        elif arr[i][j]==0:
            empty+=1
dir4 = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
dir = {0:[(1,0),(-1,0)],1:[(0,-1),(0,1)]}
dir1 = {0:[(-1,0),(0,1)], 1:[(0,1),(1,0)], 2:[(1,0),(0,-1)],3:[(0,-1),(-1,0)]}
dir2 = {0:[(-1,0),(0,1),(1,0)], 1:[(0,1),(1,0),(0,-1)], 2:[(1,0),(0,-1),(-1,0)],3:[(0,-1),(-1,0),(0,1)]}
ans = 0
def type1(i,j,t):
    mul = 1
    cnt = 0
    lst = []
    while True:
        ni, nj = i + mul * dir4[t][0], j + mul * dir4[t][1]
        if 0 > ni or 0 > nj or N <= ni or M <= nj or arr[ni][nj] == 6:
            break
        elif arr[ni][nj] == 0:
            arr[ni][nj] = '#'
            lst.append((ni, nj))
            cnt += 1
        mul += 1
    return cnt, lst

def type2(i,j,t):
    lst = []
    cnt = 0
    for l in range(2):
        mul=1
        while True:
            ni, nj = i + mul * dir[t][l][0], j + mul * dir[t][l][1]
            if 0 > ni or 0 > nj or N <= ni or M <= nj or arr[ni][nj] == 6:
                break
            elif arr[ni][nj] == 0:
                arr[ni][nj] = '#'
                lst.append((ni, nj))
                cnt += 1
            mul += 1
    return cnt, lst

def type3(i,j,t):
    lst = []
    cnt = 0
    for l in range(2):
        mul = 1
        while True:
            ni,nj = i+mul*dir1[t][l][0], j+mul*dir1[t][l][1]
            if 0 > ni or 0 > nj or N <= ni or M <= nj or arr[ni][nj] == 6:
                break
            elif arr[ni][nj] == 0:
                arr[ni][nj] = '#'
                lst.append((ni, nj))
                cnt += 1
            mul += 1
    return cnt, lst

def type4(i,j,t):
    lst = []
    cnt = 0
    for l in range(3):
        mul = 1
        while True:
            ni,nj = i+mul*dir2[t][l][0], j+mul*dir2[t][l][1]
            if 0 > ni or 0 > nj or N <= ni or M <= nj or arr[ni][nj] == 6:
                break
            elif arr[ni][nj] == 0:
                arr[ni][nj] = '#'
                lst.append((ni, nj))
                cnt += 1
            mul += 1
    return cnt, lst

def type5(i,j):
    lst = []
    cnt = 0
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        mul = 1
        while True:
            ni, nj = i + mul * di, j + mul * dj
            if 0 > ni or 0 > nj or N <= ni or M <= nj or arr[ni][nj] == 6:
                break
            elif arr[ni][nj] == 0:
                arr[ni][nj] = '#'
                lst.append((ni, nj))
                cnt += 1
            mul += 1
    return cnt, lst



def dfs(n, sm): #n은 cctv 개수, s는 조합 시작 인덱스, sm은 감시 영역.
    global ans # 감시가능한 영역 최댓값
    if n==len(cctv):
        ans = max(ans, sm)
        return

    ci,cj, type = cctv[n][0],cctv[n][1], cctv[n][2]
    if type==1:
        for k in range(4):
            cnt, lst = type1(ci,cj,k)
            dfs(n+1, sm+cnt)
            for ai,aj in lst:
                arr[ai][aj]=0

    elif type==2:
        for k in range(2):
            cnt, lst = type2(ci,cj,k)
            dfs(n + 1, sm + cnt)
            for ai, aj in lst:
                arr[ai][aj] = 0

    elif type==3:
        for k in range(4):
            cnt, lst =type3(ci,cj,k)
            dfs(n + 1, sm + cnt)
            for ai, aj in lst:
                arr[ai][aj] = 0

    elif type==4:
        for k in range(4):
            cnt, lst = type4(ci,cj,k)
            dfs(n + 1, sm + cnt)
            for ai, aj in lst:
                arr[ai][aj] = 0

    else:
        cnt, lst = type5(ci,cj)
        dfs(n + 1, sm + cnt)
        for ai, aj in lst:
            arr[ai][aj] = 0

dfs(0,0)
print(empty-ans)