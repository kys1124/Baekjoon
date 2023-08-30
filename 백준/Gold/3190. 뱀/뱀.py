N = int(input()) # N x N 맵
K = int(input()) #사과 개수

arr = [[-1]*(N+2)]+[[-1]+[0]*(N)+[-1] for _ in range(N)]+[[-1]*(N+2)]

dic = {0:(-1,0),1:(0,1), 2:(1,0), 3:(0,-1)} #북 동 남 서  +1 증가하면 오른쪽 회전, -1 왼쪽 회전
turn = {'L':-1,'D':1}
for _ in range(K):
    i,j = map(int, input().split())
    arr[i][j] = 1   # 사과 표시


L = int(input()) # 방향 변환횟수
cmd = []
for _ in range(L):
    X,C = input().split()
    cmd.append((int(X), C))

si,sj, sdir, slen = 1,1,1,1
arr[si][sj]=-1

def move(si,sj,sdir,slen):
    T = 0
    pretime = []
    hi,hj,hdir = si,sj,sdir
    ti,tj,tdir = si,sj,sdir
    idx = 0
    for x, c in cmd:
        while x>T:
            T +=1
            ni,nj = hi+dic[hdir][0], hj+dic[hdir][1] #다음좌표
            if arr[ni][nj]==-1:
                return T

            elif arr[ni][nj]==1:
                hi,hj = ni,nj
                arr[ni][nj]=-1
                slen +=1

            else:
                arr[ni][nj]=-1
                arr[ti][tj]=0
                if idx<len(pretime) and (ti,tj) ==(pretime[idx][0],pretime[idx][1]):
                    tdir = pretime[idx][2]
                    idx +=1

                ti,tj = ti+dic[tdir][0], tj+dic[tdir][1]

                hi,hj = ni,nj
        hdir = (hdir+turn[c])%4
        pretime.append((hi,hj,hdir))

    while True:
        T += 1
        ni, nj = hi + dic[hdir][0], hj + dic[hdir][1]  # 다음좌표
        if arr[ni][nj] == -1:
            return T

        elif arr[ni][nj] == 1:
            hi, hj = ni, nj
            arr[ni][nj] = -1
            slen += 1

        else:
            arr[ni][nj] = -1
            arr[ti][tj] = 0
            if idx < len(pretime) and (ti, tj) == (pretime[idx][0], pretime[idx][1]):
                tdir = pretime[idx][2]
                idx += 1
            ti, tj = ti + dic[tdir][0], tj + dic[tdir][1]

            hi, hj = ni, nj

print(move(si,sj,sdir,slen))
