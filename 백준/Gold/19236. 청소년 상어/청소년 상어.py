import copy
fish_dic = dict()
arr = [[0]*4 for _ in range(4)]
dir = {0:(-1,0),1:(-1,-1),2:(0,-1),3:(1,-1),4:(1,0),5:(1,1),6:(0,1),7:(-1,1)}

for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(0,8,2):
        a,b = lst[j], lst[j+1]
        arr[i][j//2] = a
        fish_dic[a] = [i,j//2, b-1]

si,sj,sd = 0,0,fish_dic[arr[0][0]][2]
ans = arr[0][0]
del fish_dic[arr[0][0]]
arr[0][0] = 0

def move_fish(si,sj):
    for num in range(1,17):
        if fish_dic.get(num):
            ci,cj,cd = fish_dic[num]
            for _ in range(8):
                ni,nj = ci+dir[cd][0],cj+dir[cd][1]
                if 0<=ni<4 and 0<=nj<4 and (ni,nj)!=(si,sj):
                    if arr[ni][nj]==0:
                        arr[ci][cj]=0
                        arr[ni][nj]=num
                        fish_dic[num] = [ni,nj,cd]
                    else:
                        change_num = arr[ni][nj]
                        arr[ni][nj],arr[ci][cj] = arr[ci][cj], arr[ni][nj]
                        fish_dic[change_num][0], fish_dic[change_num][1] = ci,cj
                        fish_dic[num] = [ni,nj,cd]
                    break
                else:
                    cd = (cd+1)%8
                    fish_dic[num][2] = cd


def move_shark(si,sj,sd):
    lst =[]
    for mul in range(1,4):
        ni,nj = si+mul*dir[sd][0], sj+mul*dir[sd][1]
        if 0<=ni<4 and 0<=nj<4 and arr[ni][nj]!=0:
            lst.append((ni,nj))
    return lst



def dfs(n,si,sj,sd,cnt):
    global ans, fish_dic,arr

    move_fish(si,sj)

    lst = move_shark(si, sj, sd)

    if not lst:
        ans = max(ans, cnt)
        return

    for ni,nj in lst:
        copy_fish_dic = copy.deepcopy(fish_dic)
        copy_arr = [arr[i][:] for i in range(4)]
        fish_num = copy_arr[ni][nj]
        nd = fish_dic[fish_num][2]
        arr[ni][nj]=0
        del fish_dic[fish_num]
        dfs(n+1,ni,nj,nd, cnt+fish_num)
        arr = copy_arr
        fish_dic = copy_fish_dic

dfs(0,0,0,sd,ans)
print(ans)