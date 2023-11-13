from collections import deque
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='D':
            si,sj = i,j
        elif arr[i][j]=='R':
            ei,ej = i,j

dir = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}
dice1 = [0,1,2,3] #위아래
dice2 = [0,4,1,5] #좌우

def move(dice1, dice2, d):
    copy_dice1 = dice1[:]
    copy_dice2 = dice2[:]
    if d==0: # 위 방향
        copy_dice1.insert(0,copy_dice1.pop())
        copy_dice2[0], copy_dice2[2] = copy_dice1[0], copy_dice1[2]
    elif d==1: #아래 방향
        copy_dice1.append(copy_dice1.pop(0))
        copy_dice2[0], copy_dice2[2] = copy_dice1[0], copy_dice1[2]

    elif d==2: #우측
        copy_dice2.insert(0,copy_dice2.pop())
        copy_dice1[0], copy_dice1[2] = copy_dice2[0], copy_dice2[2]
    else:
        copy_dice2.append(copy_dice2.pop(0))
        copy_dice1[0], copy_dice1[2] = copy_dice2[0], copy_dice2[2]
    return copy_dice1, copy_dice2

def under(dice1,dice2):
    if 0 in dice1:
        return dice1.index(0)
    else:
        return 4+dice2.index(0)//2

def bfs():
    q = deque([(si,sj,dice1,dice2)])
    v = [[[0]*M for _ in range(N)] for _ in range(6)]
    v[0][si][sj] = 1
    cnt = 0
    flag=False
    while q:
        for _ in range(len(q)):
            ci,cj,cdice1, cdice2 = q.popleft()

            if (ci,cj)==(ei,ej) and cdice1[0]==0:
                return cnt

            for d in range(4):
                di,dj = dir[d]
                ni,nj = ci+di, cj+dj
                ndice1, ndice2 = move(cdice1, cdice2, d)
                under_num = under(ndice1,ndice2)
                if v[under_num][ni][nj]==0 and arr[ni][nj]!='#':
                    v[under_num][ni][nj]=1
                    if (ei,ej)==(ni,nj) and under_num!=0:
                        continue
                    q.append((ni,nj,ndice1,ndice2))

        cnt+=1
    return -1
print(bfs())