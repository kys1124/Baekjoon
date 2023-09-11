N,M,K = map(int, input().split())  #N*N 격자, M개 파이어볼, K는 이동명령횟수

dir = {0:(-1,0),1:(-1,1),2:(0,1),3:(1,1),
       4:(1,0),5:(1,-1),6:(0,-1),7:(-1,-1)} # 파이어볼 8방향



fire = []
for _ in range(M): #M개 파이어볼
    r,c,m,s,d = map(int, input().split()) # (r-1,c-1), m 질량, s 속도, d 방향
    fire.append((r-1,c-1,m,s,d)) # 파이어볼 초귀 위치와 질량 속도 방향 저장하기.



sm = 0 # 정답 저장할 변수.

while K!=0: # 이동 한 사이클 돌면 K --
    V = [[[0] * N for _ in range(N)] for _ in range(4)]  # 합쳐질 파이어볼 체크할 visited 배열 질량, 속력, 방향, 개수
    for _ in range(len(fire)):
        ci,cj, m,s,d = fire.pop() # 파이어볼 한개 씩 꺼내서 이동시키자.
        ni,nj = (ci+s*dir[d][0])%N, (cj+s*dir[d][1])%N
        V[0][ni][nj] +=m
        V[1][ni][nj] +=s
        if V[3][ni][nj]==0: # 이동한 자리에 fire볼이 없으면 방향도 그냥 더하기
            V[2][ni][nj] +=d
        else:
            if V[2][ni][nj]!=-1:
                if V[2][ni][nj]%2==d%2:
                    V[2][ni][nj] = d%2
                else:
                    V[2][ni][nj] = -1
        V[3][ni][nj] +=1


    for i in range(N):
        for j in range(N):
            if V[3][i][j]==1:
                fire.append((i,j,V[0][i][j],V[1][i][j],V[2][i][j]))

            elif V[3][i][j]>=2: #합쳐짐.
                if V[0][i][j]//5==0: # 나눠진 질량이 0이면 소멸
                    continue
                else: # 아니라면 다시 fire에 추가.
                    if V[2][i][j]!=-1:
                        for new_d in [0,2,4,6]:
                            fire.append((i,j, V[0][i][j]//5, V[1][i][j]//V[3][i][j], new_d))
                    else:
                        for new_d in [1,3,5,7]:
                            fire.append((i,j, V[0][i][j]//5, V[1][i][j]//V[3][i][j], new_d))

    K-=1 #1회 이동 완료.

for _,_,m,_,_ in fire: #이동이 종료되어 while문 탈출 후 fire에 남은 질량 더하기.
    sm +=m

print(sm)
