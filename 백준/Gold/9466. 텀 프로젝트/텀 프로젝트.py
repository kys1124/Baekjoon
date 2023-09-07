import sys
input = sys.stdin.readline
T = int(input())
def dfs(si):
    stk = [si]
    V[si]=1
    v1[si]=1
    cnt = 1
    while stk:
        cur = stk.pop()
        nxt = arr[cur][0]

        if V[nxt]==1 and v1[nxt]==0:
            return 0
        elif V[nxt]==0 and v1[nxt]==0:
            v1[nxt]=1
            V[nxt]=1
            stk.append(nxt)
            cnt +=1

        elif v1[nxt]==1 and V[nxt]==1:
            while si!=nxt:
                v1[si]=0
                si = arr[si][0]
                cnt-=1

    return cnt

for _ in range(T):
    N = int(input())

    st = [0]+list(map(int,input().split()))
    arr = [[] for _ in range(N+1)]
    V = [0]*(N+1)
    v1 = [0] * (N+1)
    for i in range(1,len(st)):
        arr[i].append(st[i])

    ans = 0
    for i in range(1,N+1):
        if V[i]==0 and V[st[i]]==0:
            ans += dfs(i)

    print(N-ans)