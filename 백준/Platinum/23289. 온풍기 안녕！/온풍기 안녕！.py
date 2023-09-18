R,C,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dir ={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)} #온풍기 방향
on = []
search = []
for i in range(R):
    for j in range(C):
        if arr[i][j]!=0 and arr[i][j]!=5:
            on.append((i,j,arr[i][j])) # 온풍기 좌표와 방향 기록
        elif arr[i][j]==5:
            search.append((i,j))

wall = dict()
W = int(input()) #벽의 걔수
for _ in range(W):
    x,y,t = map(int, input().split())
    if t==0:
        wall[(x-1,y-1,x-2,y-1)]=1
    else:
        wall[(x-1,y-1,x-1,y)] = 1 #벽은 dictionary 키로 저장.

def spread1(si,sj,cd): # cd==1 오른 방향 온풍기
    v = [[0] * C for _ in range(R)]
    q = [(si + dir[cd][0], sj + dir[cd][1])]
    v[si + dir[cd][0]][sj + dir[cd][1]] = 1
    new[si + dir[cd][0]][sj + dir[cd][1]] +=5

    for k in range(4, 0, -1):
        for _ in range(len(q)):
            ci, cj = q.pop(0)
            for d in (1,-1):
                ni, nj = ci +d, cj + dir[cd][1]
                if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                    if not wall.get((ni, min(cj,nj), ni, max(cj,nj))) and not wall.get((max(ni,ci), cj, min(ci,ni), cj)):
                        v[ni][nj] = 1
                        new[ni][nj]+=k
                        if k>1:
                            q.append((ni, nj))


            ni, nj = ci, cj + dir[cd][1]
            if 0 <= nj < C and v[ni][nj] == 0 and not (wall.get((ni, min(cj,nj), ni, max(cj,nj)))):

                v[ni][nj] = 1
                new[ni][nj]+=k
                if k>1:
                    q.append((ni, nj))

def spread2(si,sj, cd): # cd==3,4 위 아래
    v = [[0] * C for _ in range(R)]
    q = [(si + dir[cd][0], sj + dir[cd][1])]
    v[si + dir[cd][0]][sj + dir[cd][1]] = 1
    new[si + dir[cd][0]][sj + dir[cd][1]] +=5
    for k in range(4, 0, -1):
        for _ in range(len(q)):
            ci, cj = q.pop(0)

            for d in (1,-1):
                ni, nj = ci+dir[cd][0], cj+d
                if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                    if  not wall.get((max(ni,ci), nj, min(ni,ci), nj)) and not wall.get((ci, min(cj,nj) , ci, max(cj,nj))):
                        v[ni][nj] = 1
                        new[ni][nj]+= k
                        if k>1:
                            q.append((ni, nj))

            ni, nj = ci+dir[cd][0], cj
            if 0 <= ni < R and v[ni][nj] == 0 and not (wall.get((max(ni,ci), cj, min(ci,ni), cj))):
                v[ni][nj] = 1
                new[ni][nj]+=k
                if k>1:
                    q.append((ni, nj))

k =0
new = [[0] * C for _ in range(R)]
while k<=100:
    # 온풍기 작동
    for si,sj,cd in on:
        if cd==1 or cd==2:
            spread1(si,sj,cd)
        else:
            spread2(si,sj,cd)

    new_arr = [new[i][:] for i in range(R)]

    # 온도 조절
    for i in range(R):
        for j in range(C):
            ci,cj = i,j

            for d in (1,4):
                ni,nj = ci+dir[d][0], cj+dir[d][1]
                if d==1:
                    if 0 <= nj < C and not (wall.get((ci, min(cj,nj), ci, max(cj,nj)))):
                        temp = abs(new[ci][cj]-new[ni][nj])//4
                        if new[ni][nj]>new[ci][cj]:
                            new_arr[ni][nj]-=temp
                            new_arr[ci][cj]+=temp
                        elif new[ni][nj]<new[ci][cj]:
                            new_arr[ci][cj]-=temp
                            new_arr[ni][nj]+=temp
                else:
                    if 0<= ni < R and not wall.get((max(ci,ni), nj, min(ci,ni), nj)):
                        temp = abs(new[ci][cj] - new[ni][nj]) // 4
                        if new[ni][nj] > new[ci][cj]:
                            new_arr[ni][nj] -= temp
                            new_arr[ci][cj] += temp
                        elif new[ni][nj] < new[ci][cj]:
                            new_arr[ci][cj] -= temp
                            new_arr[ni][nj] += temp

    # 바깥 온 도 -1 ( 양수일때만)
    for i in range(R):
        if new_arr[i][0]>0:
            new_arr[i][0]-=1
        if new_arr[i][C-1]>0:
            new_arr[i][C-1]-=1

    for j in range(1,C-1):
        if new_arr[0][j]>0:
            new_arr[0][j]-=1
        if new_arr[R-1][j]>0:
            new_arr[R-1][j]-=1

    k +=1 # 초콜릿 먹기

    for ci,cj in search:
        if new_arr[ci][cj]>=K:
           continue
        else:
            break
    else:
        break
    new = new_arr
print(k)