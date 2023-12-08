from collections import deque
N, M = map(int, input().split())
arr =[list(map(int, input())) for _ in range(N)]


def bfs(si,sj,idx):
    q = deque([(si,sj)])
    v[si][sj] =idx
    cnt= 1
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                    v[ni][nj] = idx
                    cnt+=1
                    q.append((ni,nj))

                elif 0<=ni<N and 0<=nj<M and v[ni][nj]== 0 and arr[ni][nj]==1:
                    v[ni][nj]= idx
                    arr[ni][nj] = 0
                    lst.append((ni, nj))
    return lst,cnt

v =[[0]*M for _ in range(N)]
idx = 1
day = 0
sm= 0
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and v[i][j] == 0:
            lst,cnt = bfs(i, j, idx)
            sm+=cnt
            idx += 1

p =[i for i in range(idx)]

def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
check = idx-1
cnt = 0
pre = 0
day = 0
if idx==1:
    print(0,0)
else:
    while True:
        flag= True
        new_lst= []
        for ci,cj in lst:
            cnt+=1
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj =ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]!=0:
                    if find(v[ni][nj])!=find(v[ci][cj]):
                        union(v[ni][nj],v[ci][cj])
                        flag=False

                elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                    v[ni][nj]= v[ci][cj]
                    new_lst.append((ni,nj))

        pre+=1

        for ci,cj in new_lst:
            arr[ci][cj] = 0

        lst = new_lst
        if not flag:
            sm+= cnt
            day+= pre
            cnt=0
            pre=0
        if not new_lst:
            print(day, sm)
            break
        group = 0
        for i in range(1,idx):
            if p[i]==i:
                group+=1

        if group==1:
            print(day,sm)
            break