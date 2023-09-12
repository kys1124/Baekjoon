s,t = map(int,input().split())
from collections import deque


def bfs():
    q = deque([(s)])
    S = set([s])
    path = {}
    while q:
        c = q.popleft()
        if c == t:
            return path

        if c<=1000000000 and c * c not in S:
            S.add(c * c)
            path[c * c] = (c, '*')
            q.append(c * c)

        if c<=1000000000 and 2 * c not in S:
            S.add(c * 2)
            q.append(2 * c)
            path[2 * c] = (c, '+')

        if 1 not in S:
            S.add(1)
            q.append(1)
            path[1] = (c, '/')

    return -1
if s==t:
    print(0)
elif t==1:
    print('/')

else:
    path = bfs()
    ans = []
    if path==-1:
        print(-1)
    else:
        while s!=t:
            t, op= path[t]
            ans.append(op)
        ans.reverse()
        print(''.join(ans))