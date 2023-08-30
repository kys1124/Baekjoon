N, M = map(int, input().split())

dic = {}
snake = set()
for _ in range(N+M):
    a,b = map(int, input().split())
    dic[a]=b

from collections import deque

def bfs():
    cnt = 0
    q = deque([(1,cnt)])
    v = [0]*101
    v[1] =1
    while q:
        c, t = q.popleft()
        if c==100:
           return t

        for i in range(1,7):
            n = c+i
            if n<=100 and v[n]==0:
                v[n]=1
                if n not in dic:
                    q.append((n,t+1))
                else:
                    while n in dic:
                        n = dic[n]
                        v[n]=1
                    q.append((n,t+1))
print(bfs())