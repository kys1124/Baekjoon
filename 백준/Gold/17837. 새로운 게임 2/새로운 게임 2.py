N, K = map(int, input().split()) # N*N, K말
arr = [list(map(int,input().split())) for _ in range(N)]
dir = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}
change = {1:2,2:1,3:4,4:3}
mal = {}
v = [[None]*N for _ in range(N)]
for num in range(1,1+K):
    i,j,d = map(int, input().split())
    mal[num] = [i-1,j-1,d]
    v[i-1][j-1] = [num]

# print(v)

T = 1
flag=False
while T<=1000:
    for i in range(1,1+K):
        ci,cj,cd = mal[i]
        stk = v[ci][cj]
        lst = []
        while stk[-1]!=i:
            lst.append(stk.pop())
        lst.append(stk.pop())

        ni,nj = ci+dir[cd][0],cj+dir[cd][1]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0: #흰칸
            lst.reverse()
            if v[ni][nj]:
                v[ni][nj]+=lst
            else:
                v[ni][nj] = lst
        elif 0<=ni<N and 0<=nj<N and arr[ni][nj]==1: #빨간 칸
            if v[ni][nj]:
                v[ni][nj]+=lst
            else:
                v[ni][nj] = lst
        else: #나가거나 파란칸
            cd = change[cd]
            mal[i][2] = cd
            ni,nj = ci+dir[cd][0], cj+dir[cd][1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:  # 흰칸
                lst.reverse()
                if v[ni][nj]:
                    v[ni][nj] += lst
                else:
                    v[ni][nj] = lst
            elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:  # 빨간 칸
                if v[ni][nj]:
                    v[ni][nj] += lst
                else:
                    v[ni][nj] = lst
            else:
                ni,nj = ci,cj
                lst.reverse()
                v[ni][nj]+= lst

        for num in lst:
            mal[num][0], mal[num][1] = ni,nj

        if len(v[ni][nj])>=4:
            flag=True
            break
    if flag:
        break
    T+=1

if T==1001:
    print(-1)
else:
    print(T)