N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def moveright(arr): #오른쪽으로 밀기
    for i in range(N):
        new = []
        for j in range(N):
            if arr[i][j]!=0:
                new.append(arr[i][j])
        new2 = []
        idx = len(new)-1
        while idx>=1:
            if new[idx]!=new[idx-1]: # 수가 달라 안합쳐짐.
                new2.append(new[idx])
                idx-=1
            else: # 수가 같아 합쳐짐.
                new2.append(2*new[idx])
                idx-=2

        if idx==0:
            new2.append(new[idx])
        new2.reverse()
        new2 = [0]*(N-len(new2))+new2
        arr[i] = new2
    return arr

def moveleft(arr):
    for i in range(N):
        new = []
        for j in range(N):
            if arr[i][j]!=0:
                new.append(arr[i][j])
        new2 = []
        idx = 0
        while idx<=len(new)-2:
            if new[idx]!=new[idx+1]:
                new2.append(new[idx])
                idx+=1
            else:
                new2.append(2*new[idx])
                idx+=2
        if idx==len(new)-1:
            new2.append(new[idx])
        new2 += [0]*(N-len(new2))
        arr[i] = new2
    return arr

def moveup(arr): #기존 arr 전치행렬 후 moveright하고 다시 전치행렬.
    arr_T = list(map(list, zip(*arr)))
    arr_T = moveright(arr_T)
    return list(map(list, zip(*arr_T)))

def movedown(arr):
    arr_T = list(map(list, zip(*arr)))
    arr_T = moveleft(arr_T)
    return list(map(list, zip(*arr_T)))

ans = 0
def dfs(n, arr):
    global ans
    if n>=5:
        ans = max(ans,  max(map(max, arr)))
        return

    copy_arr = [arr[i][:] for i in range(N)]
    dfs(n+1, moveup(copy_arr))

    copy_arr = [arr[i][:] for i in range(N)]
    dfs(n + 1, moveleft(copy_arr))

    copy_arr = [arr[i][:] for i in range(N)]
    dfs(n + 1, moveright(copy_arr))

    copy_arr = [arr[i][:] for i in range(N)]
    dfs(n + 1, movedown(copy_arr))

dfs(0,arr)
print(ans)