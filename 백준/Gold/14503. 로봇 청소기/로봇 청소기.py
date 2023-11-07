N, M = map(int, input().split())
dir = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
si,sj,sd = map(int, input().split()) # 초기 위치, 방향
arr = [list(map(int, input().split())) for _ in range(N)]
# 0인 곳은 청소 x 1은 벽

cnt = 0
v = [[0]*M for _ in range(N)]
def check(si,sj):
    for i in range(4):
        di,dj = dir[i]
        ni,nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
            return True
    return False


while True:
    if v[si][sj]==0 and arr[si][sj]==0: #청소 안한 빈칸
        cnt+=1
        v[si][sj]=1

    if check(si,sj):
        for _ in range(4):
            sd = (sd-1)%4
            ni,nj = si+dir[sd][0], sj+dir[sd][1]
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                si,sj = ni,nj
                break
    else:
        ni,nj = si-dir[sd][0], sj-dir[sd][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=1:
            si,sj = ni,nj
        else:
            break
print(cnt)
