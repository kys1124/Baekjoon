N, M = map(int, input().split()) # M개 마법 실행.
# 상어 위치는 N//2, N//2 정 중앙에 있음.
# 상어는 토네이도로 움직여야함 벽 때문에.
arr = [list(map(int, input().split())) for _ in range(N)] # N x N 격자
dir = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
magic_d = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
score = [0,0,0]
magic = []

def check(q):
    if not q:
        return False
    cnt = 1
    pre = q[0]
    for i in range(1,len(q)):
        if cnt>=4:
            return True

        if pre==q[i]:
            cnt+=1
        else:
            cnt=1
            pre=q[i]
    return False

def pang(q):
    stk = []
    idx = 0
    while idx<len(q): # 구슬 폭발
        cnt = 1
        start = idx
        while idx<len(q)-1 and q[idx]==q[idx+1]:
            idx+=1
            cnt+=1
        if cnt<4:
            for i in range(start, start+cnt):
                stk.append(q[i])
        else:
            score[q[idx]-1]+=cnt #폭발한 구슬 인덱스로 하고 개수 리스트에 저장.
        idx+=1
    return stk

for _ in range(M):
    d,s = map(int, input().split())
    si, sj, sd = N//2, N//2,3 # 상어 위치
    ci,cj = si,sj
    for mul in range(1,s+1): #블리자드 시전 구슬 0으로 바꿔치기
        ni,nj = si+mul*magic_d[d][0], sj+mul*magic_d[d][1]
        if 0<=ni<N and 0<=nj<N:
            arr[ni][nj]=0
        else:
            break

    q = []
    v =[[0]*N for _ in range(N)]
    for i in range(1,N**2+1): # 토네이도 길을 따라 가면서 구슬 모으기
        v[ci][cj]=i
        if v[ci+dir[(sd+1)%4][0]][cj+dir[(sd+1)%4][1]]==0:
            sd = (sd+1)%4
        ci,cj = ci+dir[sd][0], cj+dir[sd][1]
        if arr[ci][cj]>0: #구슬이 있다면 q에 담기
            q.append((arr[ci][cj]))

    while check(q):
        stk = pang(q)
        q= stk

    # 구슬 변화

    new_q = []
    if q:
        cnt = 1
        pre = q[0]
        for i in range(1,len(q)):
            if q[i]==pre:
                cnt+=1
            else:
                if len(new_q)<=N**2-3:
                    new_q.append(cnt)
                    new_q.append(pre)
                elif len(new_q)==N**2-2:
                    new_q.append(cnt)
                    break
                cnt=1
                pre=q[i]
        else:
            new_q.append(cnt)
            new_q.append(pre)


    new_arr = [[0]*N for _ in range(N)]
    si,sj,sd = N//2, N//2,3
    new_arr[si][sj]=1
    for i in range(1,len(new_q)+1): # 토네이도 길을 따라 가면서 구슬 모으기
        if new_arr[si+dir[(sd+1)%4][0]][sj+dir[(sd+1)%4][1]]==0:
            sd = (sd+1)%4
        si,sj = si+dir[sd][0], sj+dir[sd][1]
        if not (0<=si<N and 0<=sj<N) or new_arr[si][sj]!=0:
            break
        new_arr[si][sj]=new_q[i-1]

    new_arr[N//2][N//2]=0
    arr= new_arr

print(score[0]+score[1]*2+score[2]*3)

