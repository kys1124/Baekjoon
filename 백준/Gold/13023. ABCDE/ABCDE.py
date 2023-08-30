N,M= map(int, input().split())

adj =[[] for _ in range(N)]
for _ in range(M):
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

V = [0]*N
def dfs(n, pre, cnt):
    global ans
    if n>=4:
        if cnt>=3:
            print(1)
            exit()
        return

    for j in adj[pre]:
        if V[j]==0:
            V[j]=1
            dfs(n+1, j, cnt+1)
            V[j]=0

ans= 0
for k in range(N):
    V[k]=1
    dfs(0,k,1)
    V[k]=0
print(ans)