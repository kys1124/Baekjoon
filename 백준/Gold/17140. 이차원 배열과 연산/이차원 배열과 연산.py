from  collections import Counter
r,c,k = map(int, input().split())
r-=1
c-=1
arr = [list(map(int, input().split())) for _ in range(3)]

T = 0

def cal(arr): #행 연산
    mx = 0
    for i in range(len(arr)):
        count_dic = Counter(arr[i])
        sorted_item = sorted(count_dic.items(), key=lambda x:(x[1],x[0]))
        lst = []
        for x,y in sorted_item:
            if x==0:
                continue
            lst.append(x)
            lst.append(y)
            if len(lst)>100:
                break
        arr[i] = lst
        mx = max(len(lst), mx)

    for i in range(len(arr)):
        arr[i] += [0]*(mx-len(arr[i]))
    return arr

while True:
    R,C = len(arr), len(arr[0])
    if (0<=r<R and 0<=c<C and arr[r][c]==k) or T>100:
        break

    if R>=C:
        arr = cal(arr)
    else:
        arr = list(map(list, zip(*arr)))
        arr = cal(arr)
        arr = list(map(list, zip(*arr)))
    T+=1
if T>100:
    print(-1)
else:
    print(T)