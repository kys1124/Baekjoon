N,M = map(int, input().split())
board = [input() for _ in range(N)]
dic = {'B':'W','W':'B'}

def solve(r,c):
    ans = 0
    for i in range(8):
        if i%2==0:
            top = 'B'
        else:
            top = 'W'
        for j in range(8):
            if top==board[r+i][c+j]:
                top = dic[top]
                ans +=1
            else:
                top = dic[top]
    return min(ans, 64-ans)

ans = 64
for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, solve(i,j))
print(ans)