N,M = map(int, input().split())
si,sj,ei,ej = map(lambda x:int(x)-1, input().split())
arr =[list(input()) for _ in range(N)]

q =[(si,sj)]
v =[[0]*M for _ in range(N)]
v[si][sj]=1
cnt = 1
def bfs(q,cnt):
    lst = []
    while q:
        tem_q = []
        for i in range(len(q)):
            ci,cj = q[i]
            if (ci,cj)==(ei,ej):
                return []
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]=='1':
                    v[ni][nj]=cnt+1
                    lst.append((ni,nj))
                elif 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='1':
                    v[ni][nj]=cnt
                    tem_q.append((ni,nj))
        q = tem_q
    return lst

while True:
    lst = bfs(q, cnt)
    if lst:
        q = lst
        cnt+=1
    else:
        break
print(cnt)