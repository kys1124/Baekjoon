board = [input() for _ in range(5)]

ans = ''
for i in range(5):
    for j in range(15-len(board[i][:])):
        board[i]+='.'

for i in range(15):
    for j in range(5):
        ans +=board[j][i]
print(ans.replace('.',''))