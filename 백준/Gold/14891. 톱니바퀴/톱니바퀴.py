arr =[list(map(int, input())) for _ in range(4)]
K = int(input())

def rotate(lst, dir):
    if dir==1: #시계방향
        lst.insert(0,lst.pop())
        return lst
    else:
        lst.append(lst.pop(0))
        return lst
for _ in range(K):
    number, dir = map(int, input().split())
    copy_arr = [arr[i][:] for i in range(4)]
    arr[number-1] = rotate(arr[number-1], dir) #입력으로 들어온 톱니는 무조건 회전.
    for idx in range(number,4): #우측 회전 확인.
        if copy_arr[idx-1][2]==copy_arr[idx][6]:
            break
        arr[idx] = rotate(arr[idx], dir*((-1)**(idx-number-1)))

    for idx in range(number-2,-1,-1): # 좌측 회전 ㅗ학인
        if copy_arr[idx][2]==copy_arr[idx+1][6]:
            break
        arr[idx] = rotate(arr[idx], dir*((-1)**(idx-number-1)))


sm = 0

for i in range(4):
    if arr[i][0]==1:
        sm+=2**(i)
print(sm)
