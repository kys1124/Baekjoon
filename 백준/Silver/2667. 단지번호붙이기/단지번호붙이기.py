N = int(input())

board = [[0]*(N+2)]+[[0]+ list(map(int, input()))+[0] for _ in range(N)]+[[0]*(N+2)]

from collections import deque
check = set()
def bfs(start):
    queue =deque([start])
    visit = set((start))
    check.add((start))
    ans = 0
    while queue:
        sx,sy = queue.popleft()
        ans +=1
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny= sx+dx, sy+dy
            if board[nx][ny]==1 and (nx,ny) not in visit and (nx,ny) not in check:
                visit.add((nx,ny))
                check.add((nx,ny))
                queue.append((nx,ny))
    return ans

ans = []
for i in range(1,N+1):
    for j in range(1, N+1):
        if board[i][j]==1 and (i,j) not in check:
            ans.append(bfs((i,j)))
ans.sort()
print(len(ans))
for x in ans:
    print(x)