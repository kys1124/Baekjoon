N = int(input())
M = int(input())
S = set([i for i in range(0,10)])
if M!=0:
    S -= set(map(int, input().split()))
S = list(S)
cur =100

ans = 500001
def dfs1(n,num):
    global ans
    if len(str(N))==n:
        ans = min(abs(int(num)-N)+n, ans)
        return

    for x in S:
        dfs1(n+1, num+str(x))


def dfs2(n,num):
    global ans
    if len(str(N))-1==n:
        ans = min(abs(int(num)-N)+n, ans)
        return

    for x in S:
        dfs2(n+1, num+str(x))

def dfs3(n,num):
    global ans
    if len(str(N))+1==n:
        ans = min(abs(int(num)-N)+n, ans)
        return

    for x in S:
        dfs3(n+1, num+str(x))


dfs1(0,'')
if len(str(N))!=1:
    dfs2(0,'')
dfs3(0,'')
print(min(ans,abs(N-cur)))