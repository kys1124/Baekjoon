from collections import deque
R, C = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]
cmd = input()

jd = {1:(1,-1),2:(1,0),3:(1,1),4:(0,-1),5:(0,0),6:(0,1),7:(-1,-1),8:(-1,0),9:(-1,1)}
robot = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j]=='I':
            si,sj = i,j
        elif arr[i][j]=='R':
            robot.append((i,j))

flag = False
for idx, x in enumerate(cmd, start=1):
    num = int(x)
    ni,nj = si+jd[num][0], sj+jd[num][1]
    if arr[ni][nj]=='R':
        print(f'kraj {idx}')
        break
    arr[si][sj] ='.'
    si,sj = ni,nj
    arr[si][sj]='I'

    new_robot = set()
    remove_set = set()

    for ci,cj in robot:
        arr[ci][cj]='.'

    for _ in range(len(robot)):
        ci,cj = robot.popleft()
        mi, mj, mndist = -1,-1, 100001
        for d in range(1,10):
            if d==5:
                continue
            ni,nj = ci+jd[d][0], cj+jd[d][1]
            if 0<=ni<R and 0<=nj<C:
                dist = abs(ni-si)+abs(nj-sj)
                if dist<mndist:
                    mi,mj = ni,nj
                    mndist = dist

        if arr[mi][mj]=='I':
            flag=True
            break

        if (mi,mj) not in new_robot:
            new_robot.add((mi,mj))
        else:
            remove_set.add((mi,mj))

    if flag:
        print(f'kraj {idx}')
        break

    robot = deque(new_robot-remove_set)
    for ci,cj in robot:
        arr[ci][cj]='R'

else:
    for line in arr:
        print(*line, sep='')