N,M=  map(int,input().split())
from collections import deque

def bfs():
    queue = deque([(0,0)])
    check = set([(0,0)])
    while queue:
        cur = queue.popleft()
        if cur==(N-1,M-1):
            return board[N-1][M-1]

        for (di,dj) in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = cur[0]+di, cur[1]+dj
            if ni>=0 and nj>=0 and ni<N and nj<M and board[ni][nj]!=0:
                if (ni,nj) not in check:
                    board[ni][nj]+= board[cur[0]][cur[1]]
                    check.add((ni,nj))
                    queue.append((ni,nj))


board = [[0]*M for _ in range(N)]
for i in range(N):
    miro = input()
    for j in range(M):
        board[i][j] = int(miro[j])
print(bfs())