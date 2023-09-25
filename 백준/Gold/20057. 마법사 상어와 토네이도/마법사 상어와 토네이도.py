N = int(input()) # 배열 가로 세로 길이, 홀수
arr = [list(map(int, input().split())) for _ in range(N)] # 모래양이 저장된 배열

v = [[0]*N for _ in range(N)] #토네이도 이동 경로 방문 배열

dir = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)} #토네이도 이동 방향 좌 하 우 상

sand0 = {0:(-1,0),1:(1,0),2:(-1,-1),3:(1,-1),4:(-2,-1),5:(+2,-1),6:(-1,-2),7:(+1,-2),8:(0,-3), 9:(0,-2)} #d==0 기준.
def turn(d, sand):
    if d == 0:
        return sand
    elif d == 1:
        new_sand = {}
        for key, value in sand.items():
            new_sand[key] = (-value[1], value[0])
        return new_sand
sand1 = turn(1, sand0)
sand2 = turn(1, sand1)
sand3 = turn(1, sand2)
sand = [sand0, sand1, sand2, sand3]
percentage = [1,1,7,7,2,2,10,10,5]

si,sj = N//2, N//2 # 격자의 중심이 토네이도 시작 위치.
d = 3 # 초기 토네이도 방향은 왼쪽
sm = 0

for i in range(1,N**2+1):
    v[si][sj]=i
    if v[si+dir[(d+1)%4][0]][sj+dir[(d+1)%4][1]]!=0:
        ni,nj = si+dir[d][0], sj+dir[d][1]
    else:
        d = (d+1)%4
        ni,nj = si+dir[d][0], sj+dir[d][1]

    # si,sj,d # 토네이도 좌표와 이동 방향.
    #모래가 있는 칸: ni,nj
    cur_sand = arr[ni][nj]
    for idx in range(10):
        nni,nnj = si+sand[d][idx][0],sj+sand[d][idx][1]
        if idx==9:
            moving_sand = arr[ni][nj]
        else:
            moving_sand = (cur_sand * percentage[idx]) // 100

        arr[ni][nj] -= moving_sand

        if 0<=nni<N and 0<=nnj<N:
            arr[nni][nnj]+= moving_sand
        else:
            sm+= moving_sand

    si,sj = ni,nj

print(sm)