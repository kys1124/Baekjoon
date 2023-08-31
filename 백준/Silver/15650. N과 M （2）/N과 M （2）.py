N,M = map(int, input().split())
arr = [0 for _ in range(M)]
def func(n, idx):
    if n==M:
        print(*arr)
        return

    for i in range(N):
        if idx<i:
            arr[n]=i+1
            func(n+1,i)

func(0,-1)