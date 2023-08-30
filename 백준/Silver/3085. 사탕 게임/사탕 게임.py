import sys
input = sys.stdin.readline
N = int(input())

board = [list(map(str, input())) for _ in range(N)]
from collections import deque

def dfsr(si,sj):
    cnt = 1
    color = board[si][sj]
    stk = deque([(si,sj)])

    while stk:
        ci,cj = stk.pop()
        ni,nj = ci+1, cj
        if ni<N and board[ni][nj]==color:
            cnt +=1
            stk.append((ni,nj))
    return cnt


def dfsc(si, sj):
    cnt = 1
    color = board[si][sj]
    stk = deque([(si, sj)])
    while stk:
        ci,cj = stk.pop()
        ni, nj = ci, cj+1
        if nj < N and board[ni][nj] == color:
            cnt += 1
            stk.append((ni, nj))
    return cnt

mx = 0
for i in range(N):
    for j in range(N):
        mx = max(dfsc(i,j), mx, dfsr(i,j))

for i in range(N):
    for j in range(N):
        for di,dj in ((1,0),(0,1)):
            ni,nj = i+di,j+dj
            if ni<N and nj<N and board[ni][nj]!=board[i][j]:
                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                for r in range(N):
                    mx = max(mx, dfsr(r, nj), dfsr(r, j))
                for c in range(N):
                    mx = max(mx, dfsc(ni,c),dfsc(i,c))

                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
print(mx)
