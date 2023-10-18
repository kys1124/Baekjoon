A,B = map(int, input().split())
N,M = map(int, input().split())
arr = [[0]*A for _ in range(B)]
dir_dict = {'N': 0, 'E':1, 'S':2,'W':3}
dir  = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
robot = {}
for i in range(1,N+1):
    x,y,d = map(str, input().split())
    arr[B-int(y)][int(x)-1] = i
    robot[i] = [B-int(y), int(x)-1, dir_dict[d]]
flag =False
for _ in range(M):
    number, cmd, cnt = map(str, input().split())
    number = int(number)
    cnt = int(cnt)
    for _ in range(cnt):
        if cmd=='F':
            ci, cj, cd = robot[number]
            ni,nj = ci+dir[cd][0], cj+dir[cd][1]
            if 0<=ni<B and 0<=nj<A and arr[ni][nj]==0:
                arr[ci][cj]=0
                arr[ni][nj]=number
                robot[number] = [ni,nj,cd]
            elif not (0<=ni<B and 0<=nj<A):
                print(f'Robot {number} crashes into the wall')
                flag =True
                break

            elif arr[ni][nj]!=0:
                print(f'Robot {number} crashes into robot {arr[ni][nj]}')
                flag=True
                break

        elif cmd=='R':
            cd = robot[number][2]
            cd = (cd+1)%4
            robot[number][2] = cd

        else:
            cd = robot[number][2]
            cd = (cd-1)%4
            robot[number][2] = cd

    if flag:
        break
else:
    print('OK')