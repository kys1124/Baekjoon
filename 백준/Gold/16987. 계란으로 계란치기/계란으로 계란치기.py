N = int(input())
eggs  = []
for _ in range(N):
    s,w = map(int, input().split())
    eggs.append([s,w])

ans = 0
v = [0]*N
def dfs(n, cnt):
    global ans
    if n==N:
        ans = max(ans, cnt)
        return

    if eggs[n][0]<=0:
        dfs(n+1,cnt)

    else:
        for i in range(N):
            if n!=i and eggs[i][0]>0:
                cs,cw = eggs[n]
                ns,nw = eggs[i]
                eggs[n][0]-=nw
                eggs[i][0]-=cw
                if eggs[n][0]<=0:
                    if eggs[i][0]<=0:
                        dfs(n+1, cnt+2)
                    else:
                        dfs(n+1, cnt+1)
                else:
                    if eggs[i][0]<=0:
                        dfs(n+1, cnt+1)
                    else:
                        dfs(n+1, cnt)
                eggs[n][0]+=nw
                eggs[i][0]+=cw

            elif n!=i and eggs[i][0]<=0:
                dfs(n+1, cnt)

dfs(0,0)
print(ans)
