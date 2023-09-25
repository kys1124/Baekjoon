from collections import deque
N,Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
L = deque(map(int, input().split()))

dir = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
def tornado(N,L,arr):
    si,sj = 0,2**L-1 #초기 위치
    v = [[0]*N for _ in range(N)]
    rcnt,ccnt = 0,1
    for i in range(1,N**2+1):
        r,c = (i-1)//N, (i-1)%N
        v[si][sj]= arr[r][c]
        ni,nj = si+1, sj
        if rcnt<2**L-1:
            rcnt+=1
        elif rcnt==2**L-1 and nj+2**L<N:
            ni,nj = ni-2**L, nj+2**L
            rcnt= 0
        elif rcnt==2**L-1 and nj+2**L>=N:
            if ccnt<=2**L-1:
                ccnt+=1
                ni,nj = ni-2**L,2**L-ccnt

            else:
                ni = ni
                nj = 2**L-1
                ccnt=1
            rcnt = 0
        si,sj = ni,nj
    return v

def bfs(si,sj):
    global sm
    q = deque([(si,sj)])
    V[si][sj]=1
    cnt = 1
    sm +=arr[si][sj]
    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and V[ni][nj]==0 and arr[ni][nj]>0:
                V[ni][nj]=1
                cnt+=1
                sm+=arr[ni][nj]
                q.append((ni,nj))

    return cnt



while L:
    l = L.popleft()
    new_arr = tornado(2**N, l, arr) #여기에 돌린판을 복제할 것.
    S = set()
    for ci in range(2**N):
        for cj in range(2**N):
            cnt = 0
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<2**N and 0<=nj<2**N and new_arr[ni][nj]>0:
                    cnt+=1
            if cnt<3:
                S.add((ci,cj))

    for ci,cj in S:
        if new_arr[ci][cj]==0:
            continue
        new_arr[ci][cj]-=1

    arr = new_arr

sm = 0
V = [[0]*(2**N) for _ in range(2**N)]
ans = 0
for i in range(2**N):
    for j in range(2**N):
        if arr[i][j]!=0 and V[i][j]==0:
            cnt = bfs(i,j)
            ans = max(cnt, ans)

print(sm)
print(ans)