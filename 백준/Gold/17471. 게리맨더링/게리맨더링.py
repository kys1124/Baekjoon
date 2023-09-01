N = int(input())
arr = list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
S = set([i for i in range(1,N+1)])
total = sum(arr)
for i in range(1,N+1):
    lst = list(map(int, input().split()))
    for x in lst[1:]:
        adj[i].append(x)


ans = 1e9
def dfs(n, s1, sm):
    global ans
    if n==N+1:
        if check(s1):
            s2 = list(S - set(s1))
            if check(s2):
                ans = min(ans, abs(2*sm-total))
        return

    dfs(n+1, s1+[n], sm+arr[n-1])
    dfs(n+1, s1, sm)


from collections import deque
def check(s1):
    if s1:
        q = deque([s1[0]])
        v=[0]*(N+1)
        v[s1[0]]=1
        s = set(s1)
        cnt = 1
        while q:
            cur = q.pop()
            for nxt in adj[cur]:
                if v[nxt]==0 and nxt in s:
                    v[nxt]=1
                    q.append(nxt)
                    cnt+=1
        if cnt==len(s1):
            return True
        else:
            return False
    else:
        return False


dfs(1,[],0)
if ans==1e9:
    print(-1)
else:
    print(ans)