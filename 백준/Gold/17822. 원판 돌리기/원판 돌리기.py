N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(x,d,k):
    if d==0: #시계
        for i in range(x-1,N,x): #x의 배수 번째 원판 선택
            lst = arr[i]
            for _ in range(k):
                lst.insert(0,lst.pop())
            arr[i] = lst

    else:
        for i in range(x-1,N,x):
            lst= arr[i]
            for _ in range(k):
                lst.append(lst.pop(0))
            arr[i] = lst

def find():
    copy_arr = [arr[i][:] for i in range(N)]
    flag = True
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j]==0:
                continue
            if copy_arr[i][(j - 1) % M] == copy_arr[i][j]:
                arr[i][j] = arr[i][(j - 1) % M] = 0
                flag = False

            if copy_arr[i][j] == copy_arr[i][(j + 1) % M]:
                arr[i][j] = arr[i][(j + 1) % M] = 0
                flag = False

            if i<N-1 and copy_arr[i][j] == copy_arr[i+1][j]:
                arr[i][j] = arr[i+1][j] = 0
                flag = False

            if i>0 and copy_arr[i][j] == copy_arr[i-1][j]:
                arr[i][j] =  arr[i-1][j] = 0
                flag = False

    if flag:
        cnt = 0
        sm = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]==0:
                    continue
                cnt+=1
                sm+=arr[i][j]
        if cnt>0:
            avg = sm/cnt
            for i in range(N):
                for j in range(M):
                    if arr[i][j]==0:
                        continue
                    if arr[i][j]>avg:
                        arr[i][j]-=1
                    elif arr[i][j]<avg:
                        arr[i][j]+=1



for _ in range(T):
    x,d,k = map(int, input().split())
    rotate(x,d,k)
    find()

print(sum(map(sum, arr)))
