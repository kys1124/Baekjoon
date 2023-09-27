N,K = map(int , input().split())
arr= [list(map(int, input().split())) for _ in range(N)]

mal = [[-1,-1,-1] for _ in range(K)] # 말의 행 열 방향 저장
v = [[None]*N for _ in range(N)] # 말의 갯수와 순서를 저장할 배열

dir = {0:(0,1),1:(0,-1),2:(-1,0),3:(1,0)} #우좌상하
change = {0:1,1:0, 2:3, 3:2}  #방향 전환


for idx in range(K):
    i,j,d = map(int, input().split())
    mal[idx][0] = i-1
    mal[idx][1] = j-1
    mal[idx][2] = d-1
    v[i-1][j-1] = [(idx, d-1)] # 행,열에 말의 번호와 방향이 리스트로 저장돼있어 계속 추가. len()>=4 면 겜끝.

t= 0 #시간 초기값
flag = True #겜 끝낼 전역변수
while flag:
    t+=1
    if t>1000: #1000턴 초과 종료
        t =-1 #-1 출력
        break

    for i in range(K): # K 말 한번씩 움직임
        ci,cj, cd = mal[i] #현재 내가 움직이려는 말의 좌표와 방향, 번호는 i번말
        lst =[ ] # 옮길 말 다같이 저장했다가 옮기기.
        ni,nj = ci+dir[cd][0], cj+dir[cd][1] #이동좌표
        while v[ci][cj][-1][0]!=i: #내 위로 쌓인 말 다 꺼냄.
            lst.append(v[ci][cj].pop())
        lst.append(v[ci][cj].pop()) # 자신도 꺼냄.

        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0: #흰칸
            for idx,_ in lst:
                mal[idx][0], mal[idx][1] = ni,nj #mal에 저장된 위치 갱신
            lst.reverse() #뒤집어서 내가 제일 아래로 가게.

        elif 0<=ni<N and 0<=nj<N and arr[ni][nj]==1: # 빨간 칸
            for idx, _ in lst:
                mal[idx][0], mal[idx][1] = ni, nj # 뒤집을 필요없이 그냥 위치만 갱신

        else: #파란칸 or 범위 벗어남.
            cd= change[cd] #방향 전환.
            mal[i][2] = cd # 저장된 방향도 바꿔줌.
            ni,nj = ci+dir[cd][0], cj+dir[cd][1] # 바뀐 방향으로 이동
            if not (0<=ni<N and 0<=nj<N) or arr[ni][nj]==2: #돌아봤는데도 파란칸 or 범위 밖
                lst.reverse() #뒤집고, 기존 위치 그대로 있음.
                ni,nj = ci,cj

            else:
                for idx, _ in lst:
                    mal[idx][0], mal[idx][1] = ni,nj #바뀐위치 저장.
                if arr[ni][nj]==0: #흰칸
                    lst.reverse() #뒤집기

        if v[ni][nj]: #기존에 말이 있던 곳이면
            v[ni][nj].extend(lst) #리스트 더하기
        else: #없으면  None이므로 리스트 저장.
            v[ni][nj] = lst

        if len(v[ni][nj])>=4: #움직인 곳의 말이 4개 이상이면 종료
            flag=False
            break

print(t)