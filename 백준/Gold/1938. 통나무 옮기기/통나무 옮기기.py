from collections import deque
N = int(input())
arr = [list(input()) for _ in range(N)]
def find_strat():
    q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='B':
                if j+1<N and arr[i][j+1]=='B':
                    q.append((i,j+1,0))
                    arr[i][j]=arr[i][j+1]=arr[i][j+2]='0'
                    return q
                else:
                    q.append((i+1,j,1))
                    arr[i][j]=arr[i+1][j]=arr[i+2][j]='0'
                    return q
def find_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='E':
                if j+1<N and arr[i][j+1]=='E':
                    ei,ej,e_flag = i,j+1,0
                    arr[i][j]=arr[i][j+1]=arr[i][j+2]='0'
                    return ei,ej,e_flag
                else:
                    ei,ej, e_flag = i+1,j,1
                    arr[i][j]=arr[i+1][j]=arr[i+2][j]='0'
                    return ei,ej,e_flag
ei,ej,e_flag = find_end()
# q에 중심 좌표만 넣고 생각하기.
def check(ci,cj):
    for r in (-1,0,1):
        for c in (-1,0,1):
            if arr[ci+r][cj+c]=='1':
                return False
    return True

def bfs():
    q = find_strat()
    q = deque(q)
    v = [[[0] * N for _ in range(N)] for _ in range(2)]  # 0은 가로 1은 세로 통나무
    si,sj,s_flag = q[0]
    v[s_flag][si][sj]=1
    cnt = 1
    while q:
        for _ in range(len(q)):
            ci,cj, flag = q.popleft()
            if (ci,cj,flag)==(ei,ej,e_flag):
                return v[e_flag][ei][ej]-1

            if flag==0: #가로 누워있는 경우
                for di,dj in (1,0),(0,1),(0,-1),(-1,0):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<N and 1<=nj<N-1 and (v[flag][ni][nj]==0 or v[flag][ni][nj]>cnt+1):
                        if arr[ni][nj]=='0' and arr[ni][nj+1]=='0' and arr[ni][nj-1]=='0':
                            v[flag][ni][nj]=cnt+1
                            q.append((ni,nj,flag))

                if 1<=ci<N-1 and 1<=cj<N-1 and (v[1][ci][cj]==0 or v[1][ci][cj]>cnt+1) and check(ci,cj):
                    v[1][ci][cj]=cnt+1
                    q.append((ci,cj,1))

            else: # 세로
                for di,dj in (1,0),(0,1),(0,-1),(-1,0):
                    ni,nj = ci+di,cj+dj
                    if 1<=ni<N-1 and 0<=nj<N and (v[flag][ni][nj]==0 or v[flag][ni][nj]>cnt+1):
                        if arr[ni-1][nj]=='0' and arr[ni][nj]=='0' and arr[ni+1][nj]=='0':
                            v[flag][ni][nj]=cnt+1
                            q.append((ni,nj,flag))

                if 1<=ci<N-1 and 1<=cj<N-1 and (v[0][ci][cj]==0 or v[0][ci][cj]>cnt+1) and check(ci,cj):
                    v[0][ci][cj]=cnt+1
                    q.append((ci,cj,0))
        cnt+=1
    return 0

print(bfs())