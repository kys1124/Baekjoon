r,c,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
from collections import Counter

def cal(arr):
    mx_len = 0
    for i in range(len(arr)):
        number = Counter(arr[i])
        if number.get(0):
            del number[0]
        number = sorted(number.items(), key=lambda x:(x[1],x[0]))
        arr[i] = []
        for idx, x in enumerate(number):
            if idx>=100:
                break
            arr[i].append(x[0])
            arr[i].append(x[1])
        mx_len = max(mx_len, min(2*len(number), 100))

    for i in range(len(arr)):
        arr[i] += [0]*(mx_len-len(arr[i]))
    return arr



t=0
while not (0<=(r-1)<len(arr) and 0<=(c-1)<len(arr[0])) or arr[r-1][c-1]!=k:
    t+=1
    if len(arr)<len(arr[0]):
        arr = list(map(list, zip(*arr)))
        arr = cal(arr)
        arr = list(map(list,zip(*arr)))
    else:
        arr =cal(arr)

    if t>100:
        t=-1
        break
print(t)