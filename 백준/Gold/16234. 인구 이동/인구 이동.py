N,L,R = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]

from collections import deque
def bfs(si,sj, idx):
    q = deque([(si,sj)])
    V[si][sj] = idx
    cnt = 1
    sm = arr[si][sj]
    while q:
        ci,cj = q.popleft()

        cur_pop = arr[ci][cj] # 현재 조사하는 곳 인구수
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)): # 4방향 탐색
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and V[ni][nj]==0: #범위 내이고 미방문
                diff = abs(cur_pop-arr[ni][nj]) # 인구수 차이 계산
                if L<=diff<=R: # L이상 R이하이면
                    V[ni][nj]=idx #방문 처리 ->연합을 확정 지었다는 것.
                    q.append((ni,nj))
                    sm+=arr[ni][nj]
                    cnt+=1 # 연합 국가 수 증가.

    return cnt, sm

t =0 # 일 수
while True: #무한 반복 돌리고 인구 이동 체크할 것.
    V = [[0] * N for _ in range(N)] # V배열로 나라를 표시할 것.
    idx = 1 # 나라번호 1~
    lst = []  #이동한 인구를 저장. indx = 나라번호 -1
    flag = True #이동 인구가 없다면 반복 종료할 flag 변수
    for i in range(N):
        for j in range(N):
            if V[i][j]==0: #미방문
               cnt, sm = bfs(i,j,idx) #bfs를 돌면서 연합 탐색
               if cnt>=2: # 연합형성이 된 국가가 있으면
                   flag = False #flag 바꿈
               idx_population = sm//cnt # 인구수//나라수
               lst.append(idx_population) #이동 인구 리스트에 저장.
               idx +=1 # 나라번호 증가.

    if flag: #이동인구가 없다면 반복 종료
        break

    for i in range(N):
        for j in range(N):
            i_country = V[i][j] #나라번호에 따른 인구 입력
            V[i][j]=lst[i_country-1]

    arr= V # 배열 복사
    t+=1 # 1일 지남.

print(t)