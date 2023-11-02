from collections import deque
N = int(input()) #  NxN 격자
arr = [list(input()) for _ in range(N)] # 1은 이동 불가, 0이동가능

q = deque()

def find(s):
    for i in range(N):
        for j in range(N):
            if arr[i][j]==s:
                if i+1<N and arr[i+1][j]==s:
                    arr[i][j]='0'
                    arr[i+1][j]='0'
                    arr[i+2][j]='0'
                    return i+1,j,0
                elif j+1<N and arr[i][j+1]==s:
                    arr[i][j]='0'
                    arr[i][j+1]='0'
                    arr[i][j+2]='0'
                    return i,j+1,1

si,sj,s_flag = find('B')
q.append((si,sj,s_flag)) #통나무의 중심 좌표와 세로or 가로 상태 기록.
ei,ej,e_flag = find('E')

def check(ci,cj,flag):
    if flag==0:
        if arr[ci][cj]=='0' and arr[ci-1][cj]=='0' and arr[ci+1][cj]=='0':
            return True
        else:
            return False

    elif flag==1:
        if arr[ci][cj]=='0' and arr[ci][cj-1]=='0' and arr[ci][cj+1]=='0':
            return True
        else:
            return False

def check2(ci,cj):
    for i in (-1,0,1):
        for j in (-1,0,1):
            ni,nj = ci+i,cj+j
            if arr[ni][nj]=='1':
                return False
    return True


def bfs(q):
    v = [[[0] * N for _ in range(N)] for _ in range(2)]
    v[s_flag][si][sj]=1
    cnt = 0 #횟수 기록.
    while q:
        for _ in range(len(q)):
            ci,cj,flag = q.popleft()
            if (ci,cj,flag)==(ei,ej,e_flag):
                return v[e_flag][ei][ej]

            if flag==0: # 세로 통나무
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)): #4방향 이동
                    ni,nj = ci+di, cj+dj
                    if 1<=ni<N-1 and 0<=nj<N and v[flag][ni][nj]==0 and check(ni,nj,flag):
                        v[flag][ni][nj]=cnt+1
                        q.append((ni,nj,flag))
                # T 회전
                if 0<=ci<N and 1<=cj<N-1 and v[1][ci][cj]==0 and check2(ci,cj):
                    v[1][ci][cj]=cnt+1
                    q.append((ci,cj,1))

            else: # 가로 통나무
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 1<=nj<N-1 and v[flag][ni][nj]==0 and check(ni,nj,flag):
                        v[flag][ni][nj]=cnt+1
                        q.append((ni,nj,flag))

                # T 회전
                if 1<=ci<N-1 and 0<=cj<N and v[0][ci][cj]==0 and check2(ci,cj):
                    v[0][ci][cj]=cnt+1
                    q.append((ci,cj,0))
        cnt+=1

    return 0
print(bfs(q))