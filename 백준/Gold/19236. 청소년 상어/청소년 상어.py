import copy
dir = {0:(-1,0),1:(-1,-1),2:(0,-1),3:(1,-1),4:(1,0),5:(1,1),6:(0,1),7:(-1,1)}
fish = {}
arr =[[0]*4 for _ in range(4)]
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = lst[2*j]
        fish[lst[2*j]] = [i,j,lst[2*j+1]-1]

si,sj = 0,0
ans = arr[si][sj]
sd = fish[arr[si][sj]][2]
del fish[arr[si][sj]]
arr[si][sj] = 0

def dfs(si,sj,sd,arr, sm):
    global ans, fish
    for i in range(1,17):
        if fish.get(i): # 살아있는 물고기 이면,
            ci,cj,cd = fish[i]
            c_num = i
            for _ in range(8):
                ni,nj = ci+dir[cd][0], cj+dir[cd][1]
                if 0<=ni<4 and 0<=nj<4 and (ni,nj)!=(si,sj) and arr[ni][nj]>0:
                    other = arr[ni][nj]
                    od = fish[other][2]
                    fish[c_num] = [ni,nj,cd]
                    fish[other] = [ci,cj,od]
                    arr[ni][nj] = c_num
                    arr[ci][cj] = other
                    break
                elif 0<=ni<4 and 0<=nj<4 and (ni,nj)!=(si,sj) and arr[ni][nj]==0:
                    fish[c_num] = [ni,nj,cd]
                    arr[ni][nj] = c_num
                    arr[ci][cj]=  0
                    break
                else:
                    cd = (cd+1)%8
                    fish[c_num][2] = cd



    lst = []
    for mul in range(1,4):
        ni,nj = si+mul*dir[sd][0], sj+mul*dir[sd][1]
        if 0<=ni<4 and 0<=nj<4 and arr[ni][nj]>0:
            lst.append((ni,nj))

    if not lst:
        ans = max(ans, sm)
        return
    else:
        for ni,nj in lst:
            copy_arr = [arr[i][:] for i in range(4)]
            copy_fish = copy.deepcopy(fish)
            num = arr[ni][nj]
            nd = fish[num][2]
            del fish[num]
            arr[ni][nj] = 0
            dfs(ni,nj,nd,arr,sm+num)
            fish = copy_fish
            arr = copy_arr


dfs(si,sj,sd,arr,ans)
print(ans)