import sys
input = sys.stdin.readline
N,L,R,X = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
def dfs(n, sm, l, mx,mn):
    global ans
    if n>=N:
        if l>=2 and sm>=L and sm<=R and mx-mn>=X:
            ans+=1
        return
    
    if sm>R:
        return
    
    dfs(n+1,  sm+arr[n], l+1,max(mx,arr[n]),min(mn,arr[n]))
    dfs(n+1,  sm,l,mx,mn)

dfs(0,0,0,0,10**6)
print(ans)