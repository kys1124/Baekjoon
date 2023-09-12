import sys
input = sys.stdin.readline
R,C,M = map(int, input().split())

shark = [[0]*C for _ in range(R)]
dir = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}
change = {1:2,2:1, 3:4,4:3}
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    if d==1 or d==2:
        shark[r-1][c-1] = (s%(2*(R-1)),d,z)
    else:
        shark[r-1][c-1] = (s%(2*(C-1)),d,z)


sm = 0 # 잡은 상어 크기 누적.
for idx in range(C): # 낙시꾼 위치
    for j in range(R): #해당 낙시꾼 위치에서 상어 찾기

        if shark[j][idx]!=0:
            sm += shark[j][idx][2]
            shark[j][idx]= 0
            break

    # 상어 이동 구현
    new_shark = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if shark[i][j]!=0:
                ci,cj = i,j
                cs,cd,cz = shark[ci][cj]
                ni = ci + cs * dir[cd][0]
                nj = cj + cs * dir[cd][1]
                ns = cs
                while not (0 <= ni < R and 0 <= nj < C):
                    if ni < 0:
                        ns -= ci
                        ci = 0
                    elif ni >= R:
                        ns -= (R - 1) - ci
                        ci = R - 1
                    elif nj < 0:
                        ns -= cj
                        cj = 0
                    elif nj >= C:
                        ns -= (C - 1) - cj
                        cj = C - 1
                    cd = change[cd]
                    ni, nj = ci + ns * dir[cd][0], cj + ns * dir[cd][1]

                ci, cj = ni, nj

                if new_shark[ci][cj]==0:
                    new_shark[ci][cj] = (cs,cd,cz)
                else:
                    if new_shark[ci][cj][2]<cz:
                        new_shark[ci][cj]=(cs,cd,cz)

    shark = new_shark
print(sm)