N = int(input())

adj =[[] for _ in range(N+1)]
for i in range(1,N+1):
    a = int(input())
    adj[i].append(a)


def dfs(s):
    global V
    stk = [s]
    v = [0]*(N+1)
    V[s]=1
    v[s]=1
    while stk:
        cur = stk.pop()

        nxt = adj[cur][0]

        if V[nxt]==1 and v[nxt]==0:
            return []
        elif V[nxt]==0 and v[nxt]==0:
            v[nxt]=1
            V[nxt]=1
            stk.append(nxt)
        elif v[nxt]==1 and v[nxt]==1:
            while s!=nxt:
                v[s]=0
                s=adj[s][0]
    return v

V = [0]*(N+1)
ans = []
for i in range(1,N+1):
    if V[i]==0:
        lst = dfs(i)
        if lst:
            for j in range(1,N+1):
                if lst[j]==1:
                    ans.append(j)
print(len(ans))
ans.sort()
for x in ans:
    print(x)