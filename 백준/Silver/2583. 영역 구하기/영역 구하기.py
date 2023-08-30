from collections import deque

def dfs(ci,cj):
    stack = deque([(ci,cj)])
    check.add((ci,cj))
    ans = 1
    while stack:
        si, sj = stack.pop()
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<M and 0<=nj<N and board[ni][nj]==0 and (ni,nj) not in check:
                stack.append((ni,nj))
                check.add((ni,nj))
                ans +=1
    return ans

M,N,K = map(int, input().split())

board = [[0]*N for _ in range(M)]

for _ in range(K):
    c1,r1,c2,r2 = map(int, input().split())
    for i in range(r1,r2):
        for j in range(c1,c2):
            board[i][j]=1

check = set()
ans = []
for i in range(M):
    for j in range(N):
        if board[i][j]==0 and (i,j) not in check:
            ans.append(dfs(i,j))
ans.sort()
print(len(ans))
print(*ans)
