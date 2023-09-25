N,M = map(int, input().split())
si,sj,d = map(int, input().split())
dir = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} # 북 동 남 서 반시계 회전은 (dir-1)%4

arr = [list(map(int, input().split())) for _ in range(N)] # 0이 청소안된 빈칸, 1은 벽
v  = [[0]*M for _ in range(N)]# 청소여부를 체크할 visited 배열
cnt =0
while True:
    if v[si][sj]==0 and arr[si][sj]==0: #로봇 청소기 위치가 빈칸이고, 미청소
        v[si][sj]=1 # 청소
        cnt+=1 #청소한 칸 숫자 세기

    flag= True
    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)): # 4방향 탐색
        ni,nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0: #청소안한 빈칸 찾기
            flag = False

    if flag: # 4방향 모두 청소되지 않은 빈칸이 없음.
        ni,nj = si-dir[d][0], sj-dir[d][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=1:
            si,sj = ni,nj #후진하고 while문 처음으로 돌아가기
            continue
        else: # 후진 불가능하면 반복 종료
            break

    else: # 청소가능한 칸이 있는 경우
        for _ in range(4):
            d = (d-1)%4 # 90도 회전
            ni,nj = si+dir[d][0], sj+dir[d][1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
                si,sj = ni,nj
                break

print(cnt)