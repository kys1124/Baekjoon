N,M,K = map(int, input().split())
dice1 = [1,3,6,4] #동 서 움직임. +1, -1
dice2 = [1,5,6,2] #남 북 움직임. +1, -1
arr = [list(map(int, input().split())) for _ in range(N)]
dir = {0:(0,1), 1:(1,0), 2:(0,-1),3:(-1,0)} # 동 남 서 북
change = {0:2,2:0, 1:3,3:1}
si,sj, sd, score =0,0,0, 0
def dfs(si,sj):
    V = [[0]*M for _ in range(N)]
    stk = [(si,sj)]
    cnt = 0
    V[si][sj]=1
    while stk:
        ci,cj = stk.pop()
        cnt +=1

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and V[ni][nj]==0 and arr[ni][nj]==arr[si][sj]:
                V[ni][nj]=1
                stk.append((ni,nj))
    return cnt



for _ in range(K):
    ni,nj = si+dir[sd][0], sj+dir[sd][1]
    if not (0<=ni<N and 0<=nj<M): #경계밖이면 방향 전환
        sd = change[sd]
        ni,nj = si+dir[sd][0], sj+dir[sd][1]

    B = arr[ni][nj]
    if sd==0: #동 이동 dice1 +=1
        dice1.insert(0,dice1.pop()) #맨 끝 값을 떼서 앞으로 삽입.
        dice2[0],dice2[2] = dice1[0],dice1[2]
    elif sd==2: # 서족 이동  dice1 -=1
        dice1.append(dice1.pop(0)) # 맨 앞에 값을 떼서 뒤로 붙임.
        dice2[0], dice2[2] = dice1[0], dice1[2]
    elif sd==1: # 남쪽 이동. dice2 +=1
        dice2.insert(0,dice2.pop())
        dice1[0],dice1[2] = dice2[0],dice2[2]
    else: # 북쪽 이동
        dice2.append(dice2.pop(0))
        dice1[0],dice1[2] = dice2[0], dice2[2]

    # 맨 바닥 값은 항상 dice1 or dice2의 2번째 index에 있음.
    A = dice1[2] #주사위 바닥면 값

    if A>B:
        sd = (sd+1)%4
    elif A<B:
        sd = (sd-1)%4
    si,sj,sd = ni,nj, sd

    C = dfs(ni,nj)
    score += B*C

print(score)