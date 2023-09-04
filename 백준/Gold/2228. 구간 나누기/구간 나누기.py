N,M = map(int, input().split())
arr = [0]+[int(input()) for _ in range(N)]


cnt = 0
con = [[0]+[-1e9]*M for _ in range(N+1)]
notcon = [[0]+[-1e9]*M for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1, min(M,(i+1)//2)+1):
        con[i][j] = max(con[i-1][j], notcon[i-1][j-1])+arr[i]
        notcon[i][j] = max(con[i-1][j], notcon[i-1][j])


print(max(con[N][M], notcon[N][M]))
