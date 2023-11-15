N, K = map(int, input().split()) # N개 어항, K는 가장 많은 어항과 적은 어항의 차이가 K 이하
arr= list(map(int, input().split())) #어항의 물고기 초기 수


def addfish(arr): # 1XN짜리 arr #가장 적은 물고기가 있는 어항 찾아서 1마리씩 더하기
    mn = min(arr)
    for i in range(len(arr)):
        if arr[i]==mn:
            arr[i]+=1

def put(arr):
    on = [[arr[0]]]
    remain = arr[1:]
    while len(remain)-len(on[0])>=len(on)+1:
        lst = []
        for _ in range(len(on[0])):
            lst.append(remain.pop(0))
        on.append(lst)
        on = list(map(list, zip(*on)))
        for x in on:
            x.reverse()

    if remain:
        on.append(remain)
    return on


def adjust(arr):
    copy_arr = [arr[i][:] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for di,dj in ((1,0),(0,1)):
                ni,nj = i+di, j+dj
                if 0<=ni<len(arr) and 0<=nj<len(arr[i]):
                    d = abs(copy_arr[i][j]-copy_arr[ni][nj])//5
                    if d>0:
                        if copy_arr[i][j]>copy_arr[ni][nj]:
                            arr[i][j]-=d
                            arr[ni][nj]+=d
                        elif copy_arr[i][j]<copy_arr[ni][nj]:
                            arr[i][j]+=d
                            arr[ni][nj]-=d
    return arr

def make_line(arr):
    lst = []
    for j in range(len(arr[0])):
        for i in range(len(arr)-1,-1,-1):
            lst.append(arr[i][j])
    lst += arr[-1][len(arr[0]):]
    return lst

def put2(arr):
    new = []
    lst  = arr[:N//2]
    lst.reverse()
    new.append(lst)
    new.append(arr[N//2:])
    new2 =[]
    for i in range(1,-1,-1):
        lst = new[i][:N//4]
        lst.reverse()
        new2.append(lst)
    for i in range(2):
        new2.append(new[i][N//4:])

    return new2

T = 0
while True:
    mxfish, mnfish = max(arr), min(arr)
    if mxfish - mnfish <= K:
        break
    addfish(arr)
    arr = put(arr)
    arr = adjust(arr)
    arr = make_line(arr)
    arr = put2(arr)
    arr = adjust(arr)
    arr = make_line(arr)

    T +=1

print(T)