board = [list(map(int, input().split())) for _ in range(9)]
mx = [0,0,0]
for i in range(9):
    for j in range(9):
        if mx[0]<=board[i][j]:
            mx[0] = board[i][j]
            mx[1] = i
            mx[2] = j
print(mx[0])
print(f'{mx[1]+1} {mx[2]+1}')