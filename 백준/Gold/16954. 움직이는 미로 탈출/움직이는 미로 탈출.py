from collections import deque

si,sj = 7,0
ei,ej = 0,7

arr = [list(input()) for _ in range(8)]
q = deque([(si,sj,1)])

for i in range(7,-1,-1):
    for j in range(8):
        if arr[i][j]=='#':
            q.append((i,j,0))

v_people = [[123456789]*8 for _ in range(8)]
v_people[si][sj]=0

def bfs():
    cnt = 0
    while q:
        for _ in range(len(q)):
            ci,cj, flag = q.popleft()
            if flag==0:
                ni,nj = ci+1, cj
                arr[ci][cj]='.'
                if 0<=ni<8 and 0<=nj<8:
                    arr[ni][nj]='#'
                    q.append((ni,nj,0))
            else:
                for di,dj in ((0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<8 and 0<=nj<8 and arr[ni][nj]=='.' and v_people[ni][nj]!=cnt+1:
                        if (0<=ni-1<8 and arr[ni-1][nj]=='.') or ni-1<0:
                            q.append((ni,nj,1))
                            v_people[ni][nj]=cnt+1
                            if (ni,nj)==(ei,ej):
                                return 1
        cnt+=1

    return 0

print(bfs())
