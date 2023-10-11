R,C =map(int, input().split())

L1, L2= -1,-1
arr = [list(map(str, input())) for _ in range(R)]
v= [[0]*C for _ in range(R)]


def find(x):
    if p[x]!=x:
        p[x]= find(p[x])
    return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        p[find(b)] = find(a)
    else:
        p[find(a)] = find(b)


def dfs(si,sj,idx):
    global L1, L2
    stk = [(si,sj)]
    v[si][sj]=idx

    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<R and 0<=nj<C and v[ni][nj]==0 and (arr[ni][nj]=='.' or arr[ni][nj]=='L'):
                v[ni][nj]=idx
                if arr[ni][nj]=='L':
                    if L1==-1:
                        L1 = idx
                    else:
                        L2 = idx
                v[ni][nj]=idx
                stk.append((ni,nj))

t = 0
idx = 1
q=[]
for i in range(R):
    for j in range(C):
        if (arr[i][j] == '.' or arr[i][j]=='L') and v[i][j] == 0:
            if arr[i][j]=='L':
                if L1==-1:
                    L1=idx
                else:
                    L2=idx
            dfs(i, j, idx)
            idx += 1
        elif arr[i][j] == 'X':
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and (arr[ni][nj] == '.' or arr[ni][nj]=='L'):
                    q.append((i,j))
                    break

if L1==L2:
    print(0)
else:
    p = [i for i in range(idx)]
    while q:
        t+=1
        for ci,cj in q:
            arr[ci][cj]='.'
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < R and 0 <= nj < C and (arr[ni][nj]=='.' or arr[ni][nj]=='L') and v[ni][nj]!=0:
                    if v[ci][cj]==0:
                        v[ci][cj]=v[ni][nj]

                    elif v[ci][cj]==v[ni][nj]:
                        continue

                    else:
                        a,b= v[ci][cj], v[ni][nj]
                        if find(a)!=find(b):
                            union(a, b)


        if find(L1)==find(L2):
            break

        S = set()
        for i,j in q:
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 'X' and v[ni][nj]==0 and (ni,nj) not in S:
                    S.add((ni, nj))
        q = list(S)
    print(t)
