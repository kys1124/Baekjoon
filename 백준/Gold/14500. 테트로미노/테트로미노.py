import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
def dfs(n,lst, sm):
    global ans
    if ans>=sm+mx*(3-n): #가지치기, arr에서 최댓값으로만 남은 블럭을 채워도 global보다 작으면 재귀 종료
        return

    if n==3: #시작 지점은 고르고 시작하므로 3개까지.
        ans = max(ans, sm) #최댓값 갱신
        return


    for si,sj in lst: # 고른 좌표에서부터 하, 좌, 우 탐색
        v[si][sj]=1 # 방문 표시
        for di,dj in ((1,0),(0,1),(0,-1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0: #미방문, 범위내 존재하면
                v[ni][nj]=1 #방문 처리
                dfs(n+1, lst+[(ni,nj)], sm+arr[ni][nj]) #재귀
                v[ni][nj]=0 #방문 취소

v = [[0]*M for _ in range(N)]
mx = 0
for i in range(N):
    for j in range(M):
        mx = max(mx, arr[i][j]) # arr내에서 최댓값 찾기.


for i in range(N):
    for j in range(M):
        dfs(0,[(i,j)],arr[i][j]) #각 좌표를 시작점으로 하여 최댓값 찾기.

print(ans)