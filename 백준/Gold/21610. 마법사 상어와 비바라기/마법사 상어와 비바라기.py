N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = {1:(0,-1),2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)} #구름 이동

cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)] #초기 구름 좌표
def move(ci,cj, d, si):
    ni,nj = (ci+si*dir[d][0])%N, (cj+si*dir[d][1])%N # 구름 이동 좌표.
    return ni,nj


for _ in range(M):
    d,si = map(int, input().split())
    S  = set()
    for ci,cj in cloud:
        cnt = 0
        ni,nj = move(ci,cj, d, si)
        arr[ni][nj]+=1
        S.add((ni,nj))

    for ci, cj in S:
        cnt = 0
        for di,dj in ((1,1),(-1,-1),(-1,1),(1,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0:
                cnt+=1

        arr[ci][cj]+=cnt

    cloud.clear()

    for i in range(N):
        for j in range(N):
            if (i,j) not in S and arr[i][j]>=2:
                cloud.append((i,j))
                arr[i][j]-=2
    S.clear()

sm = 0
for i in range(N):
    for j in range(N):
        sm += arr[i][j]
print(sm)