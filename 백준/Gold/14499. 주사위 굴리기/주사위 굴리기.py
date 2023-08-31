N,M,x,y, K = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(N)] #지도
cmdlst = list(map(int, input().split()))
dic ={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)} # 동서북남


dice = {1:0,2:0,3:0,4:0,5:0,6:0}# 위 아래 동 서 북 남

def change(dice,cmd): #주사위 굴려서 바뀐 좌표 기록하기
    if cmd==1: #동쪽 굴리기
        dice[1],dice[2],dice[3],dice[4]=dice[4],dice[3],dice[1],dice[2]
    elif cmd==2: #서쪽 굴리기
        dice[1], dice[2], dice[3], dice[4] = dice[3],dice[4],dice[2],dice[1]

    elif cmd==3: #북쪽 굴리기
        dice[1], dice[2],dice[5],dice[6] = dice[6], dice[5], dice[1],dice[2]
    else: #남쪽 굴리기
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[6], dice[2],dice[1]
    return dice


for cmd in cmdlst:
    x,y = x+dic[cmd][0], y+dic[cmd][1] # 바뀐 좌표
    if 0<=x<N and 0<=y<M:
        if arr[x][y]==0: # 바닥 수가 지도로 복사
            arr[x][y] = dice[cmd+2]
            change(dice,cmd)
        else:
            dice[cmd+2] = arr[x][y] #주사위 바닥이 지도 숫자로 복사
            arr[x][y]=0
            change(dice, cmd)
        print(dice[1]) #윗면 출력
    else: #범위 밖이므로 기존 좌표 유지
        x,y = x-dic[cmd][0],y-dic[cmd][1]
        continue