N,M,k = map(int, input().split())
arr  =[list(map(int, input().split())) for _ in range(N)]
s_dir = list(map(int, input().split())) #초기 상어 방향
shark_dir = [[list(map(int,input().split())) for _ in range(4)] for _ in range(M)]
shark = dict()
dir = {1:(-1,0),2:(1,0),3:(0,-1), 4:(0,1)}

v = [[None]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]!=0:
            shark[arr[i][j]] = [i,j,s_dir[arr[i][j]-1]]
            v[i][j] = [k,arr[i][j]]


t = 0
while len(shark)>1 and t<=1000:
    for key, values in shark.items():
        ci,cj,cd = values
        num = key
        nd_lst = shark_dir[num-1][cd-1] #상어의 이동방향 우선순위가 담긴 리스트

        for i in nd_lst:
            ni,nj = ci+dir[i][0], cj+dir[i][1]
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]: #빈 칸
                shark[num] = [ni,nj, i]
                break

        else: # 4방이 모두 냄새가 있음.
            for i in nd_lst:
                ni,nj = ci+dir[i][0], cj+dir[i][1]
                if 0<=ni<N and 0<=nj<N and v[ni][nj][1]==num:
                    shark[num] = [ni,nj,i]
                    break

    for i in range(N):
        for j in range(N):
            if v[i][j]:
                v[i][j][0]-=1
                if v[i][j][0]==0:
                    v[i][j] = None

    remove_lst =[]


    for key, values in shark.items():
        ci, cj, cd = values
        num = key
        if not v[ci][cj]: #빈칸 이면 채취뿌리기
            v[ci][cj] = [k, num]

        else:
            if v[ci][cj][1]== num: #자기 자신 채취가 있는 곳
                v[ci][cj] = [k, num]
            else: #다른 상어와 겹친 곳
                mn = min(v[ci][cj][1], num)
                mx = max(v[ci][cj][1], num)
                v[ci][cj] = [k, mn]
                remove_lst.append(mx)

    for num in remove_lst: # 겹친 상어 삭제.
        del shark[num]


    t+=1

if t<=1000:
    print(t)
else:
    print(-1)