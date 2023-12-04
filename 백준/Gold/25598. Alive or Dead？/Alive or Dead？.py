N = int(input())
cmd_lst = input()
arr = [[0]*N for _ in range(N)]
si,sj = map(lambda x:int(x)-1, input().split())
dir ={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1),'S':(0,0)}
change = {'U':'D','D':'U', 'L':'R','R':'L'}
W = int(input())
for _ in range(W):
    wi,wj = map(lambda x:int(x)-1, input().split())
    arr[wi][wj] = 1

Z = int(input())
zombie = []
for _ in range(Z):
    zi,zj, kind, zd, zs = input().split()
    zombie.append((int(zi)-1, int(zj)-1, int(kind), zd, int(zs)))

D = int(input())

flag =True

for day in range(D):
    cmd = cmd_lst[day]
    di,dj = dir[cmd]
    ni,nj = si+di,sj+dj
    if not (0<=ni<N and 0<=nj<N) or arr[ni][nj]==1:
        ni,nj = si,sj

    si,sj = ni,nj

    for idx, (ci,cj,kind,cd,cs) in enumerate(zombie):
        if kind==0: #하급 좀비
            di,dj = dir[cd]
            for _ in range(cs):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
                    ci,cj = ni,nj
                else:
                    cd = change[cd]
                    break
            if (si,sj)==(ci,cj):
                flag=False
            zombie[idx] = (ci,cj,kind,cd,cs)

        else: #상급 좀비
            di,dj = dir[cd]
            for _ in range(cs):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    ci, cj = ni, nj
                else:
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1:
                        arr[ni][nj]=0
                    break

            mx_wall = -1
            for nd in ('U','R','D','L'):
                di,dj = dir[nd]
                wall_cnt = 0
                for mul in range(1,N+1):
                    ni,nj = ci+mul*di, cj+mul*dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1:
                        wall_cnt+=1
                    elif not (0<=ni<N and 0<=nj<N):
                        break
                if wall_cnt>mx_wall:
                    mx_wall = wall_cnt
                    cd = nd

            if (si,sj)==(ci,cj):
                flag=False
            zombie[idx] = (ci, cj, kind, cd, cs)

    if not flag:
        print(day+1)
        print("DEAD...")
        break
else:
    print("ALIVE!")