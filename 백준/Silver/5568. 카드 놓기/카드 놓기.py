N = int(input())
k = int(input())

lst = [(input()) for _ in range(N)]
S = set()
ans = 0
def dfs(n, num):
    global ans, S
    if n==k:
        if num not in S:
            S.add(num)
            ans +=1
        return


    for i in range(N):
        if v[i]==0:
            v[i]=1
            dfs(n+1, num+lst[i])
            v[i]=0

v = [0]*N
dfs(0,'')
print(ans)