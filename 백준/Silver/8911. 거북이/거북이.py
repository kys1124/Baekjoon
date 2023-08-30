T = int(input())

dir = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)} # 북 동 남 서

for _ in range(T):
    max_x,max_y,min_x,min_y = 0,0,0,0

    si,sj = (0,0) # 초기 위치
    cur = 0 # 북쪽 보고 있음
    cmd = input() # 명령어 입력
    for x in cmd:
        if x=='F':
            ni,nj = si+dir[cur][0], sj+dir[cur][1]
            si,sj= ni,nj
            max_y = max(max_y,ni)
            max_x = max(max_x,nj)
            min_y = min(min_y, ni)
            min_x = min(min_x, nj)

        elif x=='B':
            ni,nj = si-dir[cur][0], sj-dir[cur][1]
            si,sj = ni, nj
            max_y = max(max_y, ni)
            max_x = max(max_x, nj)
            min_y = min(min_y, ni)
            min_x = min(min_x, nj)

        elif x=='L':
            cur = (cur-1)%4
        else:
            cur = (cur+1)%4

    print((max_x-min_x)*(max_y-min_y))