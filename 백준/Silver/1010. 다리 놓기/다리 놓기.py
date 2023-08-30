T = int(input())
for tc in range(T):
    n,m = map(int, input().split())

    board = [[0]*(m+2) for _ in range(n+2)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j:
                board[i][j]=1
            elif i>j:
                board[i][j]=0
            elif i==1:
                board[i][j]=j
            else:
                for k in range(1,j-i+2):
                    board[i][j] += board[i-1][j-k]

    print(board[n][m])