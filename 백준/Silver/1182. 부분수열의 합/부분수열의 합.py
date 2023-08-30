N,S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
def func(n, s):
    global cnt
    if n==N:
        if s==S:
            cnt+=1
        return
    
    func(n+1,s)
    func(n+1, s+lst[n])

func(0, 0)
if S==0: cnt-=1

print(cnt)