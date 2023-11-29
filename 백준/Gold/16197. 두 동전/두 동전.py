N,M = map(int, input().split()) #세로 가로
arr = [list(input()) for _ in range(N)] # o 동전, . 빈칸, # 벽
# 10번 넘으면 -1 출력
coin = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='o':
            coin.append((i,j))
            arr[i][j]='.'

ans =11

def dfs(n, ai,aj,bi,bj):
    global ans
    if n>=ans:
        return

    if n>10 or ((ai,aj)==(-1,-1) and (bi,bj)==(-1,-1)):
        return
    if ((ai,aj)==(-1,-1) and (bi,bj)!=(-1,-1)) or ((ai,aj)!=(-1,-1) and (bi,bj)==(-1,-1)):
        ans = min(ans, n)
        return


    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        nai,naj,nbi,nbj = ai+di, aj+dj, bi+di,bj+dj
        if not(0<=nai<N and 0<=naj<M):
            nai,naj = -1,-1
        elif arr[nai][naj]=='#':
            nai,naj = ai,aj

        if not(0<=nbi<N and 0<=nbj<M):
            nbi,nbj = -1,-1

        elif arr[nbi][nbj]=='#':
            nbi,nbj = bi,bj

        dfs(n+1, nai,naj,nbi,nbj)

dfs(0,coin[0][0],coin[0][1], coin[1][0], coin[1][1])
if ans==11:
    print(-1)
else:
    print(ans)
