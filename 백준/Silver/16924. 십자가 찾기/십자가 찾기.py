N,M = map(int, input().split())
board= [['.']*(M+2)]+[['.']+ list(input())+['.'] for _ in range(N)]+[['.']*(M+2)]
ans = 0
ans_lst = []
check_lst = []
v = [[0]*(M+2) for _ in range(N+2)] # 십자가를 이루지 않은 별이 있는지 확인 용도

for si in range(1,N+1):
    for sj in range(1,M+1):
        if board[si][sj]=='*':
            check_lst.append((si,sj)) #별 좌표 모으기
            flag = True
            cnt = 1
            while flag:
                for di,dj in ((-1,0),(0,1),(0,-1),(1,0)): #4방향 탐색
                    ni,nj = si+cnt*di, sj+cnt*dj 
                    if 0<ni<N+1 and 0<nj<M+1 and board[ni][nj]=='*': #4방향 모두 별이면 +1
                        continue
                    else:
                        flag = False #아니면 while문 종료
                        break
                else:
                    for di, dj in ((-1, 0), (0, 1), (0, -1), (1, 0)): #십자가를 이루는 별 좌표들 방문 표시
                        ni, nj = si + cnt * di, sj + cnt * dj 
                        v[ni][nj]=1 
                    v[si][sj]=1
                    ans +=1
                    ans_lst.append((si,sj,cnt)) #정답기록
                    cnt +=1

for i,j in check_lst: #방문 안한 별 존재 시 -1
    if v[i][j]==0:
        print(-1)
        break
else: #모두 십자가를 이루고 있으면 정답 출력
    print(ans)
    for x,y,s in ans_lst:
        print(x,y,s)