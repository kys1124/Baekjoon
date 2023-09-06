import sys
input = sys.stdin.readline

N,M,D = map(int, input().split())  # 행 열 공격거리제한
arr = [list(map(int, input().split())) for _ in range(N)] #0 빈칸 1 적

enemy = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemy += 1

ans = 0
def combination(n,s, lst):
    global ans
    if n==3: #3명 배치 조합
        cnt = find([arr[i][:] for i in range(N)], lst, enemy) #arr가 재귀돌때마다 바뀌면 안되므로 deepcopy로 넘겨줌.
        ans = max(ans, cnt) #제거 최대 적 수 갱신
        return

    for i in range(s,M):
        combination(n+1, i+1, lst+[i])


def find(arr, lst, enemy): # 궁수 위치 변수로 받음
    cnt = 0
    while enemy:
        remove= set()
        for k in range(3):
            mi,mj = 100,100 # 적당히 큰 값 주고 갱신할 예정
            mx = abs(mi-N)+abs(mj-lst[k])
            for i in range(N-1,-1,-1): #아래서 부터 찾아야함.
                for j in range(M): #왼쪽 열부터 확인 할 것
                    if arr[i][j]==1:
                        dist = abs(N-i)+abs(lst[k]-j) # N,lst[k]에 궁수가 있고 적이 i,j 있음.
                        if dist<=D and mx>dist: #사정거리 안이고 더 가까운 거리면 열 작은 순으로 갱신
                            mx = dist
                            mi,mj = i,j
                        elif dist<=D and mx==dist:
                            if mj<j:
                                continue
                            else:
                                mi,mj = i,j
            if mi!=100 and mj!=100: #갱신된 좌표면 제거할 집합에 추가
                remove.add((mi,mj))

        for ci,cj in remove: # 나중에 처리하는 이유는 같은 적 공격했을 수도 있음.
            arr[ci][cj] = 0  # 적 제거
            cnt += 1 #제거 적수 증가
            enemy -= 1 #남은 적수 감소

        for i in range(M): #마지막 행 적 숫자 감소
            if arr[N-1][i]==1:
                enemy-=1

        for j in range(M): # 한칸씩 내리기
            l = [0] #맨위칸은 무조건 0
            for i in range(N-1):
                l.append(arr[i][j])
            for i in range(N):
                arr[i][j]=l[i]

    return cnt

combination(0,0,[])
print(ans)