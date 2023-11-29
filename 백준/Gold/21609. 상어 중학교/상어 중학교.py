N, M = map(int, input().split()) # N X N 격자,  M 종류 색상의 일반 블록
arr = [list(map(int, input().split())) for _ in range(N)] # -1 검은 블록, 0 무지개 블록, 1~M 숫자는 일반 블록
# 택시거리가 1인 두 칸은 인접하다.
# abs(r1-r2)+abs(c1-c2)=1 -> 상하좌우

#블록 그룹 -> 연결된 블록 집합. 일반 블록이 한개 이상. 일반블록은 모두 같은색.
# 검은 블록은 포함 x 무지개 블록은 개수 상관 x
# 그룹의 블록 수는 2개 이상, dfs로 쭉 따라갈 수 있어야함.
# 기준 블록은 무지개 블록이 아니고, 행 ,열 번호가 가장 작은 블록, -> 왼쪽 상단

def dfs(si,sj, v): # 블록 그룹 찾을 함수 -> 일반 블록에서만 실행 할 것
    stk = [(si,sj)]
    v[si][sj]=1
    lst = [(si,sj)]
    rainbow = []
    cnt = 0
    while stk:
        ci,cj = stk.pop()

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and (arr[ni][nj]==0 or arr[ni][nj]==arr[si][sj]):
                v[ni][nj]=1
                if arr[ni][nj]==0:
                    rainbow.append((ni,nj))
                    cnt+=1
                stk.append((ni,nj))
                lst.append((ni,nj))
    for ci,cj in rainbow:
        v[ci][cj]=0
    return lst, cnt

def find_max_group(arr): #가장 큰 블록 그룹 찾기
    v = [[0]*N for _ in range(N)]
    rainbow_cnt=0
    mx_group = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0 and v[i][j]==0:
                lst,cnt = dfs(i,j,v) # i,j 가 기준 블록이됨.
                if len(lst)==1: # 1개 짜리 그룹은 무시
                    continue

                if len(mx_group) <len(lst): # 기존 mx_group보다 길면 갱신
                    mx_group = lst
                    rainbow_cnt = cnt
                elif len(mx_group)==len(lst): # 길이가 같으면
                    if rainbow_cnt<cnt: # 무지개 블록 수 비교
                        mx_group = lst
                        rainbow_cnt = cnt
                    elif rainbow_cnt==cnt: # 무지개 블록수도 같으면
                        if mx_group[0][0]<lst[0][0]: #기준 블록의 행 크기 비교
                            mx_group=lst
                            rainbow_cnt = cnt
                        elif mx_group[0][0] ==lst[0][0]: # 기준블록의 행 마저 같다면
                            if mx_group[0][1]<lst[0][1]: # 기준블록의 열 크기 비교
                                mx_group=lst
                                rainbow_cnt =cnt
    return mx_group

def down(arr):
    for j in range(N):
        lst = [] #여기에 담기.
        for i in range(N-1,-1,-1): #열 기준으로 행의 아래부터 조사
            if arr[i][j]==-2:
                continue
            elif arr[i][j]!=-1: # 검은 블록이 아니라면 리스트에 추가
                lst.append(arr[i][j])
            else: # 검은 블록이면 고정할 위치 계산해서 빈칸 남기고 -1 추가
                lst += [-2]*(N-len(lst)-i-1)
                lst.append(-1)
        lst += [-2]*(N-len(lst)) # N행이 되게 위에 빈칸 쌓기
        for i in range(N):
            arr[i][j] = lst[N-1-i] # 기존 arr에 입력
    return arr

score = 0
while True:
    mx_group = find_max_group(arr)
    if mx_group==[]: # 블록 그룹이 더이상 없다. 반복 종료
        break

    B = len(mx_group)
    for ci,cj in mx_group:
        arr[ci][cj]=-2 # 그룹 블록 제거

    score += B**2 # 점수 추가

    new = down(arr) # 중력 작용.

    rotate = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotate[i][j] = new[j][N-1-i]

    arr= down(rotate) # 다시 중력 작용

print(score)
