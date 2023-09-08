N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
aircon = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==9:
            aircon.append((i,j))

dir = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)} # 1,2,3,4는 상하좌우 방향 에어컨 바람의 방향.
type1 = {1:1,2:2, 3:-1, 4:-1}
type2 = {3:3,4:4, 1:-1,2:-1}
type3 = {1:4, 4:1, 2:3, 3:2}
type4 = {4:2,2:4, 1:3,3:1}

v = [[[0]*M for _ in range(N)] for _ in range(4)] # 3차원 배열로 만들고, 방향까지 기록

cnt =  0
for ci,cj in aircon:
    si,sj = ci, cj
    for i in range(4):
        v[i][ci][cj]=1
    for i in range(1,5):
        s_dir = i
        while True:
            if s_dir==-1:
                ci,cj= si,sj
                break
            ni,nj = ci+dir[s_dir][0], cj+dir[s_dir][1]
            if 0<=ni<N and 0<=nj<M:
                if v[s_dir-1][ni][nj]==0:
                    v[s_dir-1][ni][nj]=1
                    ci, cj = ni, nj
                    if arr[ni][nj]==0:
                        continue
                    elif arr[ni][nj]==1:
                        s_dir = type1[s_dir]
                    elif arr[ni][nj] == 2:
                        s_dir = type2[s_dir]
                    elif arr[ni][nj]==3:
                        s_dir = type3[s_dir]
                    else:
                        s_dir = type4[s_dir]
                else:
                    ci, cj = si, sj
                    break
            else:
                ci,cj= si,sj
                break

for i in range(N):
    for j in range(M):
        for k in range(4):
            if v[k][i][j]==1:
                cnt+=1
                break

print(cnt)