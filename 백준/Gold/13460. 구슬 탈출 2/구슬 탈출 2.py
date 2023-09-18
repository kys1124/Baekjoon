N,M = map(int, input().split())
arr = [['#']*(M+2)] + [['#']+list(map(str, input()))+['#'] for _ in range(N)] + [['#']*(M+2)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == 'O':
            ei, ej = i, j
        elif arr[i][j] == 'B':
            bi, bj = i, j

        elif arr[i][j] == 'R':
            ri, rj = i, j

dir = {0:(1,0),1:(-1,0), 2:(0,1),3:(0,-1)}

ans = 11
def dfs(n, bi,bj, ri, rj,d):
    global ans,v
    if n>10:
        return

    if bi==ei and bj==ej:
        return

    if (ri,rj)==(ei,ej) and (bi,bj)!=(ei,ej):
        ans = min(n, ans)
        return

    for  i in range(4):
        if (d==0 or d==1) and (i==0 or i==1):
            continue
        elif (d==2 or d==3) and (i==2 or i==3):
            continue

        q = [(bi,bj,1),(ri,rj,0)] # 0이 빨간 공 1이 파란공
        if i==0:
           q.sort(key=lambda x:-x[0])
        elif i==1:
            q.sort(key=lambda x:x[0])
        elif i==2:
            q.sort(key=lambda x:-x[1])
        else:
            q.sort(key=lambda x:x[1])

        while q:
            for _ in range(len(q)):
                ci,cj, color = q.pop(0)
                ni,nj = ci+dir[i][0], cj+dir[i][1]
                arr[ci][cj]='.'
                if arr[ni][nj]=='.':
                    q.append((ni,nj, color))

                elif arr[ni][nj]=='O':
                    if color==0:
                        nri,nrj = ni,nj
                        re1 = 'O'
                    else:
                        nbi,nbj = ni,nj
                        re2 = 'O'

                else:
                    if color==0:
                        nri,nrj = ci,cj
                        re1 = arr[nri][nrj]
                        arr[nri][nrj]='R'
                    else:
                        nbi,nbj = ci,cj
                        re2 = arr[nbi][nbj]
                        arr[nbi][nbj]='B'

        dfs(n+1, nbi,nbj,nri,nrj,i)
        arr[ri][rj]='R'
        arr[bi][bj]='B'
        arr[nri][nrj]=re1
        arr[nbi][nbj]=re2

dfs(0,bi,bj,ri,rj,-1)
if ans<11:
    print(ans)
else:
    print(-1)