N, M = map(int, input().split()) #N*N 격자, M번 반복
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
dir = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
magic_dir = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
si,sj,sd = N//2, N//2,0
v[si][sj]=1
tornado = []
ans = 0

def check(ball): #4개 이상 연속하는 구슬 체크
    global ans
    lst =[]
    start= 0
    end = 0
    color = ball[0]
    cnt = 1
    for i in range(1,len(ball)):
        if ball[i]==color:
            cnt+=1
            end+=1
        else: #다른 색.
            if cnt>=4: #이 구슬 이전까지 같은 색
                lst.extend([num for num in range(start, end+1,1)])
                ans+=color*cnt
            start=end=i
            color=ball[i]
            cnt=1
    if cnt>=4:
        lst.extend([num for num in range(start, end + 1,1)])
        ans += color * cnt
    return lst

for i in range(1,N**2):
    si,sj = si+dir[sd][0], sj+dir[sd][1]
    v[si][sj]=i
    tornado.append((si,sj))
    nd = (sd+1)%4
    if v[si+dir[nd][0]][sj+dir[nd][1]]==0:
        sd = nd

si,sj = N//2, N//2
for _ in range(M):
    d,s = map(int, input().split())

    for mul in range(s+1): #블리자드 마법
        ni,nj = si+mul*magic_dir[d][0], sj+mul*magic_dir[d][1]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0:
            arr[ni][nj]=0

    ball = []
    for ci,cj in tornado: #구슬 앞으로 당기기
        if arr[ci][cj]>0:
            ball.append(arr[ci][cj])

    while ball:
        pang_lst = check(ball)
        if not pang_lst:
            break
        new_ball = []
        idx = 0
        pang_lst = set(pang_lst)
        for i in range(len(ball)):
            if i not in pang_lst:
                new_ball.append(ball[i])
        ball = new_ball
    if not ball:
        break

    color = ball[0]
    cnt = 1
    new_ball  = []
    for i in range(1,len(ball)):
        if color==ball[i]:
            cnt+=1
        else:
            new_ball.append(cnt)
            new_ball.append(color)
            color = ball[i]
            cnt=1
    new_ball.append(cnt)
    new_ball.append(color)

    new_arr = [[0]*N for _ in range(N)]
    for i in range(len(tornado)):
        if i<len(new_ball):
            new_arr[tornado[i][0]][tornado[i][1]] = new_ball[i]
        else:
            break
    arr = new_arr

print(ans)