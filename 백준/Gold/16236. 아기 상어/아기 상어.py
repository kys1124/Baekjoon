N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            si,sj = i,j

s_size=2
s_cnt = 0
def bfs(si,sj,s_size, s_cnt):
    q =[(si,sj)]
    v = [[0]*N for _ in range(N)]
    v[si][sj]=1
    t = 0
    while q:
        temp_q = []
        lst = []
        for i in range(len(q)):
            ci,cj = q[i]

            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]<=s_size:
                    if arr[ni][nj]<s_size and arr[ni][nj]!=0:
                        lst.append((ni,nj))
                    v[ni][nj]=1
                    temp_q.append((ni,nj))
        t+=1
        q= temp_q
        if lst:
            lst.sort()
            if s_cnt+1==s_size:
                return lst[0][0], lst[0][1], s_size+1, 0, t
            else:
                return lst[0][0], lst[0][1], s_size, s_cnt+1, t
    return -1,-1,-1,-1,-1

T = 0
while True:
    ni,nj,n_size,n_cnt,t = bfs(si,sj,s_size,s_cnt)
    if t!=-1:
        T+=t
        arr[si][sj]=0
        si,sj,s_size,s_cnt = ni,nj,n_size,n_cnt
        arr[si][sj]=9
    else:
        break
print(T)