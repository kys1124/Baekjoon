import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = [[1]*(M+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]+[[[1]]*(M+2)]

empty = []

from collections import deque
def dfs(si,sj, v): # 상대돌이 제거 가능한지 및 제거된다면 몇개인지 세는 dfs 함수.
    stk = deque([(si,sj)])
    v[si][sj]=1
    cnt = 1
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if arr[ni][nj]==0: #빈칸이 있다면 공간이 남아 제거 불가
                return 0 # 0 반환
            if v[ni][nj]==0 and arr[ni][nj]==2: #방문한적 없고, 상대돌로 이어지면 개수 ++
                v[ni][nj]=1
                stk.append((ni,nj))
                cnt+=1
    return cnt

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]==0:
            empty.append((i,j)) #빈칸 찾기. 돌 놓을 두 곳 후보

# 2개 고르므로 재귀말고 for 문으로 조합 구현
ans = 0
for i in range(len(empty)-1):
    for j in range(i+1, len(empty)): # 두 곳 고르는 조합 2중 반복몬
        cnt = 0 #제거된 상대 돌 수
        v = [[0]*(M+2) for _ in range(N+2)] #방문 배열. 조합마다 새로 선언되어서 초기화 돼야함.

        r1,c1,r2,c2 = empty[i][0], empty[i][1], empty[j][0], empty[j][1] # 돌 놓을 두 곳 좌표

        arr[r1][c1]=arr[r2][c2]=1 #내가 선택한 두 곳에 돌 놓기.

        #내가 놓은 곳의 돌 인근 8방향의 흰 돌 탐색 dfs
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)):
            ni,nj= r1+di, c1+dj #제거 가능한 돌의 후보
            if arr[ni][nj]==2 and v[ni][nj]==0: #미방문에 상대돌이면 
                cnt +=dfs(ni,nj,v) # dfs로 개수 ++

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
            ni, nj = r2 + di, c2 + dj
            if arr[ni][nj]==2 and v[ni][nj]==0:
                cnt +=dfs(ni, nj, v)

        ans = max(ans, cnt) #최대값 갱신
        arr[r1][c1]=arr[r2][c2]=0 #돌 놓은 곳 다시 0으로 미방문 복원

print(ans)