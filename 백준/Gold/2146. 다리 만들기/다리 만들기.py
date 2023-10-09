from collections import deque
N= int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


v = [[0]*N for _ in range(N)]
group_lst = {}
def dfs(si,sj,idx):
    stk  =[(si,sj)]
    v[si][sj]=idx
    group_lst[idx]= []
    for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
        ni,nj = di+si,dj+sj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            group_lst[idx].append((si,sj))
            break

    while stk:
        ci,cj = stk.pop()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
                v[ni][nj]=idx
                stk.append((ni,nj))
                for ddi, ddj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    nni, nnj = ddi + ni, ddj + nj
                    if 0 <= nni < N and 0 <= nnj < N and arr[nni][nnj] == 0:
                        group_lst[idx].append((ni, nj))
                        break


def bfs(si,sj,idx):
    global ans
    q = deque([(si,sj)])
    visited = [[0]*N for _ in range(N)]
    visited[si][sj]=1
    cnt = 0
    while q:
        if cnt>=ans:
            return N*2

        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and (arr[ni][nj]==0 or v[ni][nj]>idx):
                    visited[ni][nj]=1
                    q.append((ni,nj))
                    if arr[ni][nj]!=0:
                        return cnt
        cnt+=1



idx = 1
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            dfs(i,j,idx)
            idx+=1


ans = N*N
for i in range(1,idx):
    for ci,cj in group_lst[i]:
        ans = min(ans, bfs(ci,cj,i))

print(ans)