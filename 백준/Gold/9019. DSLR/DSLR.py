T= int(input())

from collections import deque

def bfs(A,B):
    q = deque([(A,0,'')])
    v = [99999]*10000
    v[A]=0
    path = ['']*10000

    while q:
        cur, dist, chr= q.popleft()
        if cur ==B:
            return path[B]

        for cmd in ('D','S','L','R'):
            next_num = change(cur, cmd)
            if v[next_num]>dist+1:
                v[next_num]=dist+1
                path[next_num] = path[cur]+cmd
                q.append((next_num,dist+1,cmd))

def change(A,cmd):
    if cmd=='D':
        return (A*2)%10000

    elif cmd=='S':
        if A==0:
            return 9999
        return A-1

    elif cmd=='L':
        A = str(A)
        A = '0'*(4-len(A)) + A
        return int(A[1:]+A[0])

    else:
        A = str(A)
        A = '0'*(4-len(A))+A
        return int(A[3]+A[:3])



for _ in range(T):
    A,B = map(int, input().split())
    ans = 10000
    print(bfs(A,B))