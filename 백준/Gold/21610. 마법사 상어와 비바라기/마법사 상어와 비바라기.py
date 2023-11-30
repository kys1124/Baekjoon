
# N * N 격자. 한 칸이 바구니 하나. -> 바구니 당 물의 양 제한은 없다
# (1,1) 왼위, (N,N) 오른 아래 그리고 1과 N이 연결 -> % 연산

# 비바라기 시전 -> N,1 N,2 N-1,1 N-1,2 -> 왼쪽 아래 2*2칸에 비구름 생성.
#구름의 이동 M회 방향 d와 거리 s 주어짐. 8방향
dir = {1:(0,-1),2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)}

# 각 구름에서 비가 내려 바구니 물 1증가
# 구름 삭제.
# 물이 증가한 칸에서 물복사마법 시행 -> 해당 칸에서 대각선 4방향에 물이 있는 바구니 수만큼 증가.
# 이때 이동과는 다르게 1과 N이 이어지지 않음. -> 경계체크 할 것

# 바구니에 물이 2이상인 칸에 구름 생성 , 바구니 물 -2 단 구름 생성 칸은 해당 턴에 삭제된 구름이 있는 칸이 아니다.

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1,0),(N-1,1),(N-2,0), (N-2,1)] #초기 구름 위치

for _ in range(M):
    d,s = map(int, input().split())

    move_cloud = set()
    for ci,cj in cloud:
        ni,nj = (ci+s*dir[d][0])%N, (cj+s*dir[d][1])%N #격자가 이어져있으므로 %연산
        move_cloud.add((ni,nj))
        arr[ni][nj]+=1 #바구니 물 1증가

    new_arr = [arr[i][:] for i in range(N)] #동시 증가이므로 복제된 배열 사용.

    for ci,cj in move_cloud: #이동한 구름 돌면서 인접 대각에 물이 있는 바구니 수 세기
        temp = 0
        for di,dj in ((1,1),(1,-1),(-1,1),(-1,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and new_arr[ni][nj]>0:
                temp+=1
        arr[ci][cj]+= temp

    new_cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and (i,j) not in move_cloud:
                arr[i][j]-=2
                new_cloud.append((i,j))


    cloud = new_cloud

sm = 0
for i in range(N):
    for j in range(N):
        sm+=arr[i][j]

print(sm)