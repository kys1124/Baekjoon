arr =[list(map(int, input())) for _ in range(4)] #톱니 4개 각 행마다 한개씩 열은 12부터 시계방향
# 1은 S극, 0은 N극
K = int(input()) # 회전 수

#맞닿은 톱니의 index 확인
#(0,2) (1,6) 끼리 맞닿아 있음.
# 톱니의 회전은 시계 방향이면 pop(), insert(0) idx +1
# 반시계는 pop(0), append() idx-1
dic = {1:-1,-1:1}
def rotate(lst, dir):
    if dir ==1:
        a =lst.pop()
        lst.insert(0,a)
        return lst
    else:
        a = lst.pop(0)
        lst.append(a)
        return lst

for _ in range(K):
    A, dir = map(int, input().split()) # A는 톱니 (lst의 행), dir은 -1,1 반시계 시계

    if A==2: # 양 옆 확인  (1,6),(0,2), (1,2),(2,6)
        if arr[1][6]!=arr[0][2] and arr[1][2]!=arr[2][6] and arr[2][2]!=arr[3][6]: #4개 모두 회전
            arr[1] = rotate(arr[1],dir)
            arr[0] = rotate(arr[0],dic[dir])
            arr[2] = rotate(arr[2],dic[dir])
            arr[3] = rotate(arr[3], dir)

        elif arr[1][6]==arr[0][2] and arr[1][2]!=arr[2][6] and arr[2][2]!=arr[3][6]: #오른쪽 2, 3,4회전
            arr[1] = rotate(arr[1],dir)
            arr[2] = rotate(arr[2],dic[dir])
            arr[3] = rotate(arr[3], dir)

        elif arr[1][6]!=arr[0][2] and arr[1][2]!=arr[2][6] and arr[2][2]==arr[3][6]: #오른쪽 1,2, 3 회전
            arr[1] = rotate(arr[1],dir)
            arr[2] = rotate(arr[2],dic[dir])
            arr[0] = rotate(arr[0], dic[dir])

        elif arr[1][6]!=arr[0][2] and arr[1][2]==arr[2][6]: #1,2만 회전 3,4번째는 안돔.
            arr[1] = rotate(arr[1],dir)
            arr[0] = rotate(arr[0], dic[dir])

        elif arr[1][2]!=arr[2][6] and arr[0][2]==arr[1][6]: #2,3회전
            arr[1] = rotate(arr[1], dir)
            arr[2] = rotate(arr[2], dic[dir])

        else:
            arr[A-1] = rotate(arr[A-1],dir)

    elif A==3:
        if arr[2][6] != arr[1][2] and arr[2][2] != arr[3][6] and arr[0][2] != arr[1][6]:  # 4개 모두 회전
            arr[2] = rotate(arr[2], dir)
            arr[1] = rotate(arr[1], dic[dir])
            arr[3] = rotate(arr[3], dic[dir])
            arr[0] = rotate(arr[0], dir)

        elif arr[2][6] != arr[1][2] and arr[0][2] != arr[1][6] and arr[3][6]==arr[2][2]:  # 1,2,3회전
            arr[2] = rotate(arr[2], dir)
            arr[1] = rotate(arr[1], dic[dir])
            arr[0] = rotate(arr[0], dir)

        elif arr[2][6] != arr[1][2] and arr[0][2] == arr[1][6] and arr[3][6]!=arr[2][2]:  # 2,3,4회전
            arr[2] = rotate(arr[2], dir)
            arr[1] = rotate(arr[1], dic[dir])
            arr[3] = rotate(arr[3], dic[dir])


        elif arr[2][6] != arr[1][2] and arr[0][2]==arr[1][6]: #2,3 회전
            arr[2] = rotate(arr[2], dir)
            arr[1] = rotate(arr[1], dic[dir])

        elif arr[2][2] != arr[3][6] and arr[2][6]==arr[1][2]:  # 3,4 회전.
            arr[2] = rotate(arr[2], dir)
            arr[3] = rotate(arr[3], dic[dir])

        else:  # 혼자만 회전
            arr[2] = rotate(arr[2], dir)
            continue

    elif A==1: # 오른쪽 확인 (0,2),(1,6)
        if arr[0][2]==arr[1][6]: #같은 1만 회전
            arr[0] = rotate(arr[0],dir)
            continue
        elif arr[0][2]!=arr[1][6] and arr[1][2]!=arr[2][6] and arr[2][2]!=arr[3][6]: # 모두회전
            arr[0]=rotate(arr[0],dir)
            arr[1]=rotate(arr[1],dic[dir])
            arr[2]=rotate(arr[2], dir)
            arr[3]=rotate(arr[3],dic[dir])

        elif arr[0][2]!=arr[1][6] and arr[1][2]!=arr[2][6]: #1,2,3 회전
            arr[0] = rotate(arr[0], dir)
            arr[1] = rotate(arr[1], dic[dir])
            arr[2] = rotate(arr[2], dir)

        elif arr[0][2]!=arr[1][6]:
            arr[0] = rotate(arr[0], dir)
            arr[1] = rotate(arr[1], dic[dir])

    else: #왼쪽 확인  (3,6),(2,2)
        if arr[3][6]==arr[2][2]:
            arr[3] = rotate(arr[3], dir)
            continue
        elif arr[3][6]!=arr[2][2] and arr[2][6]!=arr[1][2] and arr[1][6]!=arr[0][2]: #모두 회전
            arr[3]=rotate(arr[3],dir)
            arr[2]=rotate(arr[2], dic[dir])
            arr[1]=rotate(arr[1],dir)
            arr[0]=rotate(arr[0],dic[dir])

        elif arr[3][6]!=arr[2][2] and arr[2][6]!=arr[1][2]:
            arr[3] = rotate(arr[3], dir)
            arr[2] = rotate(arr[2], dic[dir])
            arr[1] = rotate(arr[1], dir)

        elif arr[3][6]!=arr[2][2]:
            arr[3] = rotate(arr[3], dir)
            arr[2] = rotate(arr[2], dic[dir])

print(sum([arr[i][0]*(2**i) for i in range(4)]))