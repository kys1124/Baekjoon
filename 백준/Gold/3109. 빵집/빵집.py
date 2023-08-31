R,C = map(int, input().split())
arr =[input() for _ in range(R)]
dir = {0:(-1,1), 1:(0,1),2:(1,1)} # 이동 방향은 무조건 위 먼저 오른쪽 아래 순서로

def dfs(ni,nj):
    global ans, flag # 정답 갱신할 ans와, 갱신되면 바로 재귀 종료할 flag  전역 변수 선언
    if flag: #재귀 종료
        return

    if nj==C-1: # 끝열까지 dfs 탐색으로 이동시
        ans +=1 #정답 ++
        flag=True # 재귀 종료
        return

    if 0<=ni<R and 0<=nj<C and v[ni][nj]==0 and arr[ni][nj]!='x': # 이동 좌표가 array 내에 값이고, 미방문, 건물이 아니면 파이프 설치 가능.
        v[ni][nj]=1 #방문처리, 파이프 설치
        for i in range(3): # 3방향 탐색
            dfs(ni+dir[i][0],nj+1) # 좌표 이동 재귀


v = [[0]*C for _ in range(R)] # 방문처리 할 배열 선언
ans = 0 # 정답 초기값
for i in range(R): #행 마다 dfs() 
    flag= False 
    dfs(i,0) 
print(ans)
# 이 문제에서는 dfs로 (i,0)에서 C행까지 깊이 우선 탐색을 진행하고, 방문 배열을 초기화 하지 않는 상태에서 다음 행에서 다시 깊이 우선 탐색을 시작한다.
# 원리로는 greedy알고리즘으로, 위쪽으로 파이프를 연결할 수 있다면 무조건 이 방식을 취해야하며, 이 방식으로 연결된 파이프라인은 항상 최적의 연결이다.
