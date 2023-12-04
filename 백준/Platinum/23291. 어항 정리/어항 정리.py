
N, K = map(int, input().split())
lst = list(map(int, input().split()))


def smallest(lst):
    mn = min(lst)
    for i in range(N):
        if lst[i]==mn:
            lst[i]+=1
    return lst

def make(lst):
    on = [[lst[0]]]
    remain = lst[1:]
    while len(on)+1<=len(remain)-len(on[0]):
        new = []
        for _ in range(len(on[0])):
            new.append(remain.pop(0))
        on.append(new)
        on.reverse()
        on = list(map(list, zip(*on)))
    if remain:
        on.append(remain)
    return on

mx,mn = max(lst), min(lst)
t = 0
while mx-mn>K:
    lst = smallest(lst)
    lst = make(lst)

    copy_arr = [lst[i][:] for i in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for di,dj in ((1,0),(0,1)):
                ni,nj = i+di, j+dj
                if 0<=ni<len(lst) and 0<=nj<len(lst[i]):
                    diff = abs(copy_arr[i][j]-copy_arr[ni][nj])//5
                    if diff>0:
                        if copy_arr[i][j]>copy_arr[ni][nj]:
                            lst[i][j]-=diff
                            lst[ni][nj]+=diff
                        elif copy_arr[i][j]<copy_arr[ni][nj]:
                            lst[i][j] += diff
                            lst[ni][nj] -= diff

    new = []
    for j in range(len(lst[0])):
        for i in range(len(lst)-1,-1,-1):
            new.append(lst[i][j])
    for j in range(len(lst[0]),len(lst[-1])):
        new.append(lst[-1][j])

    lst = new

    new = []
    left, right = lst[:N//2], lst[N//2:]
    left.reverse()
    new.append(left)
    new.append(right)

    arr1 = []
    arr2 = []
    for i in range(1,-1,-1):
        left,right = new[i][:N//4], new[i][N//4:]
        left.reverse()
        arr1.append(left)
        arr2.insert(0,right)

    lst = arr1+arr2
    copy_arr = [lst[i][:] for i in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < len(lst) and 0 <= nj < len(lst[i]):
                    diff = abs(copy_arr[i][j] - copy_arr[ni][nj]) // 5
                    if diff > 0:
                        if copy_arr[i][j] > copy_arr[ni][nj]:
                            lst[i][j] -= diff
                            lst[ni][nj] += diff
                        elif copy_arr[i][j] < copy_arr[ni][nj]:
                            lst[i][j] += diff
                            lst[ni][nj] -= diff

    new = []
    for j in range(len(lst[0])):
        for i in range(len(lst)-1,-1,-1):
            new.append(lst[i][j])
    lst = new
    mx,mn = max(lst), min(lst)
    t+=1

print(t)
