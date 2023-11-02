from collections import deque
M, N = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

def bfs(si,sj):
    q=  deque([(si,sj)])
    v =[[0]*M for _ in range(N)]
    v[si][sj]= 1
    cnt = 0
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]!='#':
                    q.append((ni,nj))
                    v[ni][nj]=1
                    if arr[ni][nj]=='X':
                        adj[dic[(si,sj)]][dic[(ni,nj)]-1]=cnt+1
                    elif arr[ni][nj]=='E':
                        end[dic[(si,sj)]]=cnt+1

        cnt+=1


dic = {}
idx = 1
for i in range(N):
    for j in range(M):
        if arr[i][j]=='X':
            dic[(i,j)] = idx
            idx+=1
        elif arr[i][j]=='S':
            si,sj = i,j
        elif arr[i][j]=='E':
            ei,ej =i,j

end = [0]*idx
dic[(si,sj)]= 0

adj = [[0]*(idx-1) for _ in range(idx)]
for key in dic.keys():
    ci,cj =key
    bfs(ci,cj)

ans = 123456789
visit = [0]*len(adj)
def dfs(n, lst):
    global ans
    if n==len(adj):
        pre= 0
        sm = 0
        for num in lst:
            sm+=adj[pre][num-1]
            pre = num
        sm += end[pre]
        ans = min(ans, sm)
        return

    for i in range(1,len(adj)):
        if visit[i]==0:
            visit[i]=1
            dfs(n+1, lst+[i])
            visit[i]=0
dfs(1,[])
print(ans)