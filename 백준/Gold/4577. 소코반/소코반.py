dic = {'U':(-1,0),'L':(0,-1),'R':(0,1),'D':(1,0)}
change = {'w':'.', 'W':'+'}

def check():
    sm = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'B':
                sm += 1
    if sm==total_B:
        return True
    else:
        return False

turn = 1
while True:
        N, M = map(int, input().split())
        if N==0 and M==0:
            break
        total_B = 0
        arr =[list(map(str, input())) for _ in range(N)]
        cmd_lst = input()
        for i in range(1,N-1):
            for j in range(1,M-1):
                if arr[i][j]=='w' or arr[i][j]=='W':
                    si,sj = i,j
                elif arr[i][j]=='b' or arr[i][j]=='B':
                    total_B +=1

        for cmd in cmd_lst:
            cur = arr[si][sj]
            arr[si][sj] = change[cur]
            ni,nj = si+dic[cmd][0], sj+dic[cmd][1]
            if arr[ni][nj]=='.':
                arr[ni][nj]='w'

            elif arr[ni][nj]=='+':
                arr[ni][nj]='W'

            elif arr[ni][nj]=='b': #박스
                nni,nnj = ni+dic[cmd][0], nj+dic[cmd][1]
                if arr[nni][nnj]=='.': #밀수있음
                    arr[ni][nj]='w' #여기 원래 빈칸이므로 w
                    arr[nni][nnj]='b' #민 곳 b
                elif arr[nni][nnj]=='+': # 목표지점
                    arr[ni][nj]='w' #
                    arr[nni][nnj]='B' #B
                    if check():
                        print(f'Game {turn}: complete')
                        for x in arr:
                            print(*x, sep='')
                        break

                else: # 나머지 경우는 못 민다.
                    arr[si][sj] = cur
                    ni,nj = si,sj

            elif arr[ni][nj]=='B': #박스가 목표지점.
                nni,nnj = ni+dic[cmd][0], nj+dic[cmd][1]
                if arr[nni][nnj]=='.': #밀수있음
                    arr[ni][nj]='W' #여기 원래 +이므로 W
                    arr[nni][nnj]='b' #민 곳 b
                elif arr[nni][nnj]=='+': # 목표지점
                    arr[ni][nj]='W' #
                    arr[nni][nnj]='B' #B
                    if check():
                        print(f'Game {turn}: complete')
                        for x in arr:
                            print(*x, sep='')
                        break

                else: # 나머지 경우는 못 민다.
                    arr[si][sj] = cur
                    ni,nj = si,sj

            else:
                arr[si][sj] = cur
                ni,nj = si,sj

            si,sj = ni,nj

        else:
            if check():
                print(f'Game {turn}: complete')
            else:
                print(f'Game {turn}: incomplete')
            for x in arr:
                print(*x, sep='')


        turn+=1
