def omok(board):
    for si in range(1, 20):
        for sj in range(1, 20):
            if board[si][sj] != 0:
                for di, dj in ((1, 0), (0, 1), (1, 1), (1, -1)):
                    check = [0, 0, 0]

                    for mul in range(5):
                        ni, nj = si + mul * di, sj + mul * dj
                        if board[ni][nj] == 0:
                            break

                        check[board[ni][nj]] += 1

                    if check[1] == 5 or check[2] == 5:
                        ni, nj = si - di, sj - dj
                        check[board[ni][nj]] += 1

                        ni, nj = si + 5 * di, sj + 5 * dj
                        if ni >= 0 and nj >= 0 and ni < 21 and nj < 21:
                            check[board[ni][nj]] += 1
                            if check[1]==5 or check[2] == 5:
                                if di==1 and dj==-1:
                                    return check, si+4,sj-4
                                return check, si, sj
    return 0,0,0


board = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21]

result, si, sj = omok(board)
if result ==0:
    print(0)
else:
    print(result.index(5))
    print(si, sj)