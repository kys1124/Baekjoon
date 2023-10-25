import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
idx = 1
def dfs(si,sj,idx):
    stk = [(si,sj)]
    v[si][sj]=idx
    cnt =1
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                v[ni][nj]=idx
                stk.append((ni,nj))
                cnt+=1
    return cnt

val = [0]

for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and v[i][j]==0:
            cnt = dfs(i,j,idx)
            val.append(cnt)
            idx+=1

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            S = set()
            sm = 1
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj =i+di,j+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1:
                    S.add(v[ni][nj])
            for num in S:
                sm += val[num]
            ans = max(ans, sm)
print(ans)