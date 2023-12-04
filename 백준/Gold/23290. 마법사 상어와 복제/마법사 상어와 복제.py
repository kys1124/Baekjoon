import copy
M,S = map(int, input().split()) #M마리, 마법횟수 S
fish= dict()
dir = {0:(0,-1),1:(-1,-1),2:(-1,0),3:(-1,1),4:(0,1),5:(1,1),6:(1,0),7:(1,-1)}
for _ in range(M):
    fx,fy,d = map(lambda x:int(x)-1, input().split())
    if fish.get((fx,fy)):
        fish[(fx,fy)].append(d)
    else:
        fish[(fx,fy)] = [d]

v =[[0]*4 for _ in range(4)]

si,sj = map(lambda x:int(x)-1, input().split())
shark = {1:(-1,0),2:(0,-1),3:(1,0),4:(0,1)}


def dfs(n,si,sj, sm, move_lst, fish):
    global shark_move, eat
    if n==3:
        if sm>eat:
            eat = sm
            shark_move = move_lst
        return

    for i in range(1,5):
        di,dj = shark[i]
        ni,nj = si+di,sj+dj
        if 0<=ni<4 and 0<=nj<4:
            num = 0
            if fish.get((ni,nj)):
                co = fish[(ni,nj)][:]
                num += len(co)
                del fish[(ni,nj)]
                dfs(n+1, ni,nj, sm+num, move_lst+[(ni,nj)], fish)
                fish[(ni,nj)] = co
            else:
                dfs(n+1, ni,nj, sm, move_lst+[(ni,nj)], fish)

for _ in range(S):
    copy_fish = fish
    new_fish= dict()
    for key,value in fish.items():
        ci,cj = key
        for cd in value:
            for _ in range(8):
                ni,nj = ci+dir[cd][0],cj+dir[cd][1]
                if 0<=ni<4 and 0<=nj<4 and v[ni][nj]==0 and (ni,nj)!=(si,sj):
                    if new_fish.get((ni,nj)):
                        new_fish[(ni,nj)].append(cd)
                    else:
                        new_fish[(ni,nj)] = [cd]
                    break
                else:
                    cd = (cd-1)%8
            else:
                if new_fish.get((ci, cj)):
                    new_fish[(ci,cj)].append(cd)
                else:
                    new_fish[(ci, cj)] = [cd]

    shark_move, eat = [], -1
    dfs(0,si,sj, 0, [], new_fish)
    for i in range(4):
        for j in range(4):
            if v[i][j]>0:
                v[i][j]-=1

    for ci,cj in shark_move:
        if new_fish.get((ci,cj)):
            del new_fish[(ci,cj)]
            v[ci][cj] = 2
        si,sj = ci,cj

    fish = new_fish
    for key, value in copy_fish.items():
        if fish.get(key):
            fish[key]+=value
        else:
            fish[key] = value

ans = 0
for value in fish.values():
    ans+=len(value)
print(ans)