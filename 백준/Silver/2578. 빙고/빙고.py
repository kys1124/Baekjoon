from collections import deque


def check():
    cnt = 0
    for i in range(5):
        if sum(board[i]) == 0:
            cnt += 1

    for i in range(5):
        if board[i][i]!=0:
            break
    else:
        cnt +=1

    for i in range(5):
        if board[i][4 - i]!=0:
            break
    else:
        cnt +=1

    for i in range(5):
        if sum([x[i] for x in board]) == 0:
            cnt += 1

    if cnt>=3:
        return True
    else:
        return False


board = [list(map(int, input().split())) for _ in range(5)]

bingo = []
for _ in range(5):
    bingo.extend(list(map(int, input().split())))
bingo = deque(bingo)

answer = 0

while bingo:
    cnt = 0
    answer +=1
    cur = bingo.popleft()
    for i in range(5):
        for j in range(5):
            if board[i][j]==cur:
                board[i][j]=0
    if check():
        break

print(answer)