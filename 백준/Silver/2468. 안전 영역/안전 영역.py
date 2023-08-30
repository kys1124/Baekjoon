N = int(input())
location = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def dfs1(si,sj, h):
    stack= deque([(si,sj)])
    while stack:
        ci, cj = stack.pop()
        check.add((ci,cj))
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = di+ci, dj+cj
            if 0<=ni<N and 0<=nj<N and location[ni][nj]>h and (ni,nj) not in check:
                check.add((ni,nj))
                stack.append((ni,nj))
    return 1

h=0
limit = max(map(max, location))
ans = 0

while h<limit:
    check = set()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if location[i][j]>h and (i,j) not in check:
                check.add((i,j))
                cnt += dfs1(i,j,h)
    ans = max(ans, cnt)
    h+=1
print(ans)






