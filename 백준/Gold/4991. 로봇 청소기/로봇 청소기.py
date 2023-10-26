from collections import deque
def dfs(si,sj,lst):
    stk = [(si,sj)]
    v = [[0]*M for _ in range(N)]
    v[si][sj]=1
    cnt =0
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj =ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='x':
                v[ni][nj]=1
                stk.append((ni,nj))
                if arr[ni][nj]=='*':
                    cnt+=1
    if cnt==len(lst):
        return False
    return True

def bfs(si,sj,ei,ej):
    q = deque([(si,sj)])
    v = [[0]*M for _ in range(N)]
    cnt = 0
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            if ci==ei and cj==ej:
                return cnt
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] != 'x':
                    v[ni][nj] = 1
                    q.append((ni,nj))
        cnt+=1

def cal(n, cur, sm):
    global ans
    if sm>=ans:
        return

    if n==len(lst):
        ans = min(ans, sm)
        return

    for nxt_cnt, nxt in adj[cur]:
        if v[nxt]==0:
            v[nxt]=1
            cal(n+1, nxt, sm+nxt_cnt)
            v[nxt]=0
while True:
    M, N = map(int, input().split())
    if (M,N)==(0,0):
        break
    arr = [list(input()) for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='o':
                si,sj = i,j
                arr[i][j]='.'
            elif arr[i][j]=='*':
                lst.append((i,j))

    adj  = [[] for _ in range(len(lst)+1)]

    if dfs(si,sj,lst):
        print(-1)
    else:
        ans = 1e9
        visit = [0]*len(lst)
        for i in range(len(lst)):
            ci,cj = lst[i]
            adj[0].append((bfs(si,sj,ci,cj),i+1))

        for i in range(len(lst)-1):
            for j in range(i+1, len(lst)):
                ci,cj=  lst[i]
                ni,nj = lst[j]
                cnt = bfs(ci,cj,ni,nj)
                adj[i+1].append((cnt, j+1))
                adj[j+1].append((cnt, i+1))

        v = [0]*(len(lst)+1)
        cal(0,0,0)
        print(ans)