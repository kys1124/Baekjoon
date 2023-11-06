N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
dir = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}

for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            ri,rj = i,j
        elif arr[i][j]=='B':
            bi,bj = i,j

        elif arr[i][j]=='O':
            ei,ej = i,j



ans = 11

def dfs(ri,rj,bi,bj,d, cnt):
    global ans,arr
    if cnt>10:
        return
    
    if ans<=cnt: # 가지치기
        return
    if (bi,bj)==(ei,ej):
        return

    if (ri,rj)==(ei,ej) and (bi,bj)!=(ei,ej): # 파란구슬도 같이 빠지면 정답 갱신 x
        ans = min(ans, cnt) # 빨간 구슬만 빠지면 정답 갱신
        return

    for i in range(4):
        if (d==0 or d==1) and (i==0 or i==1):
            continue
        elif (d==2 or d==3) and (i==2 or i==3):
            continue
        q = [(ri, rj, 0), (bi, bj, 1)]  # 0은 빨간색, 1은 파란색
        if i==0:
            q.sort(key=lambda x:x[0])
        elif i==1:
            q.sort(key=lambda x:-x[0])
        elif i==2:
            q.sort(key=lambda x:x[1])
        else:
            q.sort(key=lambda x:-x[1])
        copy_arr = [arr[i][:] for i in range(N)]
        for _ in range(len(q)):
            ci,cj, color = q.pop()
            arr[ci][cj]='.'
            for mul in range(1,max(M,N)):
                ni,nj = ci+mul*dir[i][0], cj+mul*dir[i][1]
                if arr[ni][nj]=='.':
                    continue
                elif arr[ni][nj]=='O':
                    if color==0:
                        nri,nrj = ni,nj
                    else:
                        nbi,nbj = ni,nj
                    break
                else:
                    if color==0:
                        nri,nrj = ci+(mul-1)*dir[i][0], cj+(mul-1)*dir[i][1]
                        arr[nri][nrj]='R'
                    else:
                        nbi,nbj = ci+(mul-1)*dir[i][0], cj+(mul-1)*dir[i][1]
                        arr[nbi][nbj]='B'
                    break
        dfs(nri,nrj,nbi,nbj, i, cnt+1)
        arr = copy_arr

dfs(ri,rj,bi,bj,-1,0)
if ans==11:
    print(-1)
else:
    print(ans)