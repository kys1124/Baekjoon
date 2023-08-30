N,M,K = map(int, input().split()) # N 가로 M 세로 K 부술 수 있는 벽 수

arr = [input() for _ in range(N)] #맵 입력받기 N x M

from collections import deque
def bfs():
    q = deque([(0,0,0,0,1)]) # 낮, 가로, 세로, 부순 벽 수, 이동 거리
    v = [[K+1]*M for _ in range(N)] # 가로, 세로 방문 배열, 원소는 부순 벽 수 갱신

    v[0][0]=0 # 낮,(0,0)에서 부순 벽 수는 0으로 초기값 설정
    dic = {0:1,1:0}
    while q:
        day, ci, cj, b, cnt = q.popleft()
        if (ci,cj)==(N-1,M-1): # N,M 도착 시 종료
            return cnt

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and  b < v[ni][nj]  and arr[ni][nj]=='0': #빈칸으로 이동
                v[ni][nj]=b
                q.append((dic[day], ni,nj, b, cnt+1))

            elif 0<=ni<N and 0<=nj<M and b+1 <= K and b+1<v[ni][nj] and arr[ni][nj]=='1':
                if day==0: #낮이면 벽을 부수기
                    v[ni][nj]=b+1
                    q.append((dic[day], ni,nj, b+1, cnt+1))
                else: #밤이면 현재 좌표 대기
                    q.append((dic[day], ci,cj,b,cnt+1))


    return -1

print(bfs())