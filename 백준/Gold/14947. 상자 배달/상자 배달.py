from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dir = {0:(1,0),1:(-1,0),2:(0,-1),3:(0,1)}
flag = 0 # flag는 0,1,2 세가지 밑면의 모양에 따라 다름. 0 : 1x1 1: 3x1 2: 1x3
# flag 0: sd 0 or 1 -> flag 1, sd 2 or 3 -> flag2
# flag 1: sd 0 or 1 -> flag 0, sd 2 or 3 -> flag1
# flag 2: sd 0 or 1 -> flag 2, sd 2 or 3 -> flag0
# 현재 상태와 움직이는 방향에 따라 변화된 밑면을 기록해 놓자.
def change_shape(flag, sd): #현재 밑면에서 굴리는 방향이 주어졌을 때 변하는 밑면 모양.
    if flag==0 and (sd==0 or sd==1):
        return 1
    elif flag==0 and (sd==2 or sd==3):
        return 2
    elif flag==1 and (sd==0 or sd==1):
        return 0
    elif flag==1 and (sd==2 or sd==3):
        return 1
    elif flag==2 and (sd==0 or sd==1):
        return 2
    else:
        return 0

def bfs(si,sj):
    v =[[[0]*M for _ in range(N)] for _ in range(3)]
    v[0][si][sj]=1
    q = deque([(si,sj, 0)]) #밑면 좌표와 현재 상황. (만약 1*3 or 3*1인 경우 가운데 좌표를 기록.
    t = 0
    while q:
        for _ in range(len(q)):
            ci,cj, flag = q.popleft()
            if flag==0 and (ei,ej)==(ci,cj):
                return t
            elif flag==1:
                if (ei,ej) in ((ci-1,cj), (ci,cj), (ci+1,cj)):
                    return t
            elif flag==2:
                if (ei,ej) in ((ci,cj-1), (ci,cj),(ci,cj+1)):
                    return t

            if flag==0: # 1*1 -> 한번에 3칸 가기 때문에 좌표 세개를 잡아야함.
                for i in range(4):
                    lst = []
                    for mul in range(1,4):
                        ni,nj = ci+mul*dir[i][0], cj+mul*dir[i][1]
                        if not (0<=ni<N and 0<=nj<M): #격자 벗어남.
                            break
                        lst.append((ni, nj))
                    else:
                        n1i,n1j = lst[0]
                        n2i,n2j = lst[1]
                        n3i,n3j = lst[2]
                        n_flag = change_shape(flag, i)

                        # if v[n_flag][n1i][n1j] == 0 or v[n_flag][n2i][n2j] == 0 or v[n_flag][n3i][n3j] == 0:
                        if v[n_flag][n2i][n2j]==0:
                            if arr[n2i][n2j]==1: #가운데 땅이 있다.
                                # v[n_flag][n1i][n1j]=1
                                v[n_flag][n2i][n2j]=1
                                # v[n_flag][n3i][n3j]=1
                                q.append((n2i,n2j,n_flag))
                            elif arr[n2i][n2j]==0 and arr[n1i][n1j]==1 and arr[n3i][n3j]==1: #양옆이 땅이다.
                                # v[n_flag][n1i][n1j] = 1
                                v[n_flag][n2i][n2j] = 1
                                # v[n_flag][n3i][n3j] = 1
                                q.append((n2i, n2j, n_flag))

            elif flag==1: # 3*1
                for i in range(2): # ->위아래로 움직임. flag바뀜. 1*1로 그리고 내 좌표에서 2칸 이동.
                    ni,nj = ci+2*dir[i][0], cj+2*dir[i][1]
                    if not (0 <= ni < N and 0 <= nj < M):  # 격자 벗어남.
                        continue
                    else:
                        if v[0][ni][nj]==0 and arr[ni][nj]==1:
                            v[0][ni][nj]=1
                            q.append((ni,nj,0))

                for i in range(2,4):
                    lst = []
                    for di in (-1,0,1):
                        ni,nj = ci+di+dir[i][0], cj+dir[i][1]
                        if not (0<=ni<N and 0<=nj<M):
                            break
                        lst.append((ni,nj))
                    else:
                        n1i,n1j = lst[0]
                        n2i,n2j = lst[1]
                        n3i,n3j = lst[2]
                        # if v[flag][n1i][n1j] == 0 or v[flag][n2i][n2j] == 0 or v[flag][n3i][n3j] == 0:
                        if v[flag][n2i][n2j]==0:
                            if arr[n2i][n2j]==1: #가운데 땅이 있다.
                                # v[flag][n1i][n1j]=1
                                v[flag][n2i][n2j]=1
                                # v[flag][n3i][n3j]=1
                                q.append((n2i,n2j,flag))
                            elif arr[n2i][n2j]==0 and arr[n1i][n1j]==1 and arr[n3i][n3j]==1: #양옆이 땅이다.
                                # v[flag][n1i][n1j] = 1
                                v[flag][n2i][n2j] = 1
                                # v[flag][n3i][n3j] = 1
                                q.append((n2i, n2j, flag))

            else:
                for i in range(2): #위아래로 움직임. 모양 바뀌지 않음.
                    lst = []
                    for di in (-1, 0, 1):
                        ni, nj = ci + dir[i][0], cj + di + dir[i][1]
                        if not (0 <= ni < N and 0 <= nj < M):
                            break
                        lst.append((ni, nj))
                    else:
                        n1i, n1j = lst[0]
                        n2i, n2j = lst[1]
                        n3i, n3j = lst[2]
                        # if v[flag][n1i][n1j] == 0 or v[flag][n2i][n2j] == 0 or v[flag][n3i][n3j] == 0:
                        if v[flag][n2i][n2j]==0:
                            if arr[n2i][n2j] == 1:  # 가운데 땅이 있다.
                                # v[flag][n1i][n1j] = 1
                                v[flag][n2i][n2j] = 1
                                # v[flag][n3i][n3j] = 1
                                q.append((n2i, n2j, flag))
                            elif arr[n2i][n2j] == 0 and arr[n1i][n1j] == 1 and arr[n3i][n3j] == 1:  # 양옆이 땅이다.
                                # v[flag][n1i][n1j] = 1
                                v[flag][n2i][n2j] = 1
                                # v[flag][n3i][n3j] = 1
                                q.append((n2i, n2j, flag))

                for i in range(2,4): # 좌우로 움직임 1*1로 바뀜.
                    ni, nj = ci + 2 * dir[i][0], cj + 2 * dir[i][1]
                    if not (0 <= ni < N and 0 <= nj < M):  # 격자 벗어남.
                        continue
                    else:
                        if v[0][ni][nj] == 0 and arr[ni][nj] == 1:
                            v[0][ni][nj] = 1
                            q.append((ni, nj, 0))
        t+=1

    return -2

for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            si,sj = i,j
            arr[i][j]=1
        elif arr[i][j]==3:
            ei,ej = i,j
            arr[i][j]=1

print(bfs(si,sj))
