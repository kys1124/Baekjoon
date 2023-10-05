# 4x4 격자에서 M마리 물고기 각 칸에 있고, 이동방향
dir = {0:(0,-1),1:(-1,-1),2:(-1,0),3:(-1,1),4:(0,1),5:(1,1),6:(1,0),7:(1,-1)} #물고기 이동 방향
shark_dir = {1:(-1,0),2:(0,-1),3:(1,0),4:(0,1)}

M,S = map(int, input().split()) #M마리 S번 반복
fish = dict()
v = [[0]*4 for _ in range(4)]
for _ in range(M):
    fx,fy,d = map(lambda x:int(x)-1, input().split()) #0,0 3,3 까지 0~7까지 방향으로 바꾸기.
    if fish.get((fx,fy)):
        fish[(fx,fy)].append(d)
    else:
        fish[(fx,fy)] =[d]

si,sj = map(lambda x:int(x)-1, input().split()) # 상어 위치.

def dfs(n, si,sj, cnt, d):
    global mxcnt, new_i,new_j, mxd
    if n==3:
        if mxcnt<cnt:
            new_i,new_j,mxd, mxcnt = si,sj, int(d), cnt

        elif mxcnt==cnt:
            if mxd>int(d):
                new_i,new_j,mxd = si,sj, int(d)
        return

    for i in range(1,5):
        ni,nj = si+shark_dir[i][0], sj+shark_dir[i][1]
        if 0<=ni<4 and 0<=nj<4:
            if fish.get((ni,nj)):
                lst = fish[(ni,nj)][:]
                del fish[(ni,nj)]
                dfs(n+1, ni,nj, cnt+len(lst), d+str(i))
                fish[(ni,nj)] = lst
            else:
                dfs(n+1, ni,nj, cnt,  d+str(i))

for _ in range(S):
    copy_fish = fish #물고기 복제

    new_fish=  dict()
    for key, value in fish.items():
        ci,cj = key
        fish_lst = value
        for cd in fish_lst:
            for _ in range(8):
                ni,nj = ci+dir[cd][0], cj+dir[cd][1]
                if 0<=ni<4 and 0<=nj<4 and v[ni][nj]==0 and (ni,nj)!=(si,sj):
                    if new_fish.get((ni,nj)):
                        new_fish[(ni,nj)].append(cd)
                    else:
                        new_fish[(ni,nj)]=[cd]
                    break
                else:
                    cd = (cd-1)%8
            else:
                if new_fish.get((ci,cj)):
                    new_fish[(ci,cj)].append(cd)
                else:
                    new_fish[(ci,cj)]=[cd]

    fish = new_fish
    new_i,new_j, mxcnt, mxd = -1,-1,0,555
    dfs(0,si,sj,0,'')

    for i in range(4):
        for j in range(4):
            if v[i][j]>0:
                v[i][j]-=1

    for i in str(mxd):
        si,sj = si+shark_dir[int(i)][0], sj+shark_dir[int(i)][1]
        if fish.get((si,sj)):
            v[si][sj]=2
            del fish[(si,sj)]

    for key, value in copy_fish.items():
        ci,cj = key
        if fish.get((ci,cj)):
            fish[(ci,cj)]+=value
        else:
            fish[(ci,cj)]=value

sm = 0
for value in fish.values():
    sm +=len(value)
print(sm)