# N*M 지도  (1,1)왼위->(N,M)오른아래
# 주사위 1이 위, 3이 동쪽 1,1 에 있음.
N,M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir  = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
dice1 = [1,5,6,2] #남북 굴리기
dice2 = [1,3,6,4] #동서 굴리기
def move(d):
    if d==0: #동 idx ++
        dice2.insert(0,dice2.pop())
        dice1[0],dice1[2] = dice2[0], dice2[2]
    elif d==1: #남 idx++
        dice1.insert(0,dice1.pop())
        dice2[0],dice2[2] = dice1[0], dice1[2]
    elif d==2: #서 idx--
        dice2.append(dice2.pop(0))
        dice1[0],dice1[2] = dice2[0], dice2[2]
    elif d==3: #북 idx++
        dice1.append(dice1.pop(0))
        dice2[0], dice2[2] = dice1[0], dice1[2]

si,sj,sd = 0,0,0
ans = 0
def cal(si,sj):
    stk = [(si,sj)]
    v= [[0]*M for _ in range(N)]
    v[si][sj]=1
    cnt=1
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==arr[si][sj] and v[ni][nj]==0:
                v[ni][nj]=1
                stk.append((ni,nj))
                cnt+=1
    return cnt

for _ in range(K):
    ni,nj = si+dir[sd][0], sj+dir[sd][1]
    if not (0<=ni<N and 0<=nj<M):
        sd = (sd+2)%4
        ni,nj = si+dir[sd][0], sj+dir[sd][1]
    si,sj = ni,nj
    move(sd)
    B = arr[si][sj]
    C = cal(si,sj)
    A = dice1[2]
    ans +=B*C
    if A>B:
        sd=(sd+1)%4
    elif A<B:
        sd=(sd-1)%4
print(ans)