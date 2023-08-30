T = int(input())
from collections import deque

def dfs(board, bug):
    dx = (1,-1,0,0)
    dy = (0,0,1,-1)

    stack = deque([bug])
    while stack:
        cur = stack.pop()
        if cur in check:
            continue
        check.add(cur)

        for i in range(4):
            nx,ny = cur[0]+dx[i], cur[1]+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and board[nx][ny]!=0:
                stack.append((nx,ny))

    return check

for tc in range(1,T+1):
    n,m, k = map(int,input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    bug = deque([])
    cnt = 0
    for _ in range(k):
        i,j = map(int, input().split())
        board[i][j] =1
        bug.append((i,j))

    check = set()
    while bug:
        start = bug.popleft()
        if start in check:
            continue
        check = check.union(dfs(board,start))
        cnt+=1
    print(cnt)