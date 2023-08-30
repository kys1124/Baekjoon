N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def cal(start):
    l = len(start)
    sm = 0
    for i in range(l-1):
        for j in range(i+1,l):
            sm +=arr[start[i]][start[j]]
            sm +=arr[start[j]][start[i]]

    return sm

def dfs(n, s, lst):
    global ans
    if n==N//2:
        link = list(set([i for i in range(N)]) - set(lst))
        ans = min(ans,abs(cal(link)-cal(lst)))
        return

    for i in range(s,N):
        dfs(n+1, i+1, lst+[i])



ans = 100*(N**2)
dfs(0,0,[])
print(ans)