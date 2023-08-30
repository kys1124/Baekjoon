M, n = map(int, input().split())
dir ={ 0:(0,1), 1:(-1,0), 2:(0,-1), 3:(1,0)} # 동 남 서 북

cur = 0 # 초기 동쪽 방향
si,sj =(0,0) # 초기 위치
for _ in range(n): #n개 명령어 입력
    cmd = input().split()
    cmd[1] = int(cmd[1])

    if cmd[0]=='MOVE':
        ni,nj = (si+ dir[cur][0]*cmd[1], sj+ dir[cur][1]*cmd[1])
        if 0<=ni<=M and 0<=nj<=M:
            si,sj = (ni,nj)
        else:
            print(-1)
            break
    else:
        if cmd[1]==0:
            cur = (cur-1)%4
        else:
            cur = (cur+1)%4

else:
    print(sj,si)