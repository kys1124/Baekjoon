R,C,M = map(int, input().split())

arr = [[0]*C for _ in range(R)]
shark =dict()
dir = {0:(-1,0), 1:(1,0), 2:(0,1), 3:(0,-1)}
change = {0:1,1:0, 2:3,3:2}
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    shark[(r-1,c-1)] = (s,d-1,z)
    arr[r-1][c-1]=1

sm = 0 # 잡은 상어 크기 누적.
for idx in range(C): # 낙시꾼 위치
    for j in range(R): #해당 낙시꾼 위치에서 상어 찾기
        if arr[j][idx]==1:
            sm+=shark[(j,idx)][2]
            del shark[(j,idx)]
            break

    # 상어 이동 구현
    new_shark = dict()
    arr = [[0] * C for _ in range(R)]
    for key, value in shark.items():
        ci,cj = key
        cs,cd,cz = value

        if cd==0 or cd==1: #2*(R-1) 혹은 2*(C-1) 칸 이동하면 자기 자리로 돌아옴.
             cs%=(2*(R-1))
        else:
            cs%=(2*(C-1))

        for _ in range(cs):
            ci+=dir[cd][0]
            cj+=dir[cd][1]
            if 0<=ci<R and 0<=cj<C:
                continue
            else:
                ci-=dir[cd][0]
                cj-=dir[cd][1]
                cd = change[cd]
                ci+=dir[cd][0]
                cj+=dir[cd][1]

        arr[ci][cj]=1

        if (ci,cj) not in new_shark:
            new_shark[(ci,cj)] = (cs,cd,cz)
        else:
            if new_shark[(ci,cj)][2]<cz:
                new_shark[(ci,cj)] = (cs,cd,cz)

    shark = new_shark
print(sm)