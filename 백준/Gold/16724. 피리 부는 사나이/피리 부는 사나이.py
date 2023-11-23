dic = {'U':(-1,0), 'D':(1,0),'L':(0,-1),'R':(0,1)}
N, M = map(int, input().split())
arr =[list(input()) for _ in range(N)]
v = [[0]*M for _ in range(N)]

def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    a= find(a)
    b =find(b)
    if a<b:
        p[b]= a
    else:
        p[a] =b


S = set()
def dfs(si,sj, idx):
    stk = [(si,sj)]
    v[si][sj]=idx
    while stk:
        ci,cj = stk.pop()

        di,dj = dic[arr[ci][cj]]
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
            v[ni][nj]=idx
            stk.append((ni,nj))
        elif 0<=ni<N and 0<=nj<M and v[ni][nj]!=idx:
            if (idx,v[ni][nj]) not in S and (v[ni][nj],idx) not in S:
                S.add((idx,v[ni][nj]))

idx = 1
for i in range(N):
    for j in range(M):
        if v[i][j]==0:
            dfs(i,j,idx)
            idx+=1

p = [i for i in range(idx)]
for cur, nxt in S:
    if find(cur)!= find(nxt):
        union(cur,nxt)

ans = 0
for i in range(1,idx):
    if p[i]==i:
        ans+=1
print(ans)