N,M = map(int, input().split())
arr = [0 for _ in range(M)]
S = set()
v = [0 for _ in range(N)]
def func(n, v):
    if n==M:
        print(*arr)
        return

    for i in range(N):
        if v[i]==0:
            v[i]= 1
            arr[n]=i+1
            func(n+1, v)
            v[i]=0
func(0,v)