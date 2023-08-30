N = int(input())
T = []
P = []
for _ in range(N):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

ans = 0
def dfs(n, sm):
    global ans

    if n>=N:
        ans = max(ans, sm)
        return

    if n+T[n]<=N:
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)

dfs(0,0)
print(ans)