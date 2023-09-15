N, M, H = map(int, input().split())
n,h = 2*N-1, 2*H+1

arr = [[0]*n for _ in range(h)] # 사다리 격자
for i in range(h):
    for j in range(n):
        if j%2==0:
            arr[i][j]=1

for _ in range(M):
    a,b = map(int ,input().split())
    arr[2*a-1][2*(b-1)+1] = 1


line = [] #추가할 수 있는 라인 후보.
for i in range(1,2*H,2):
    for j in range(n):
        if arr[i][j]==0:
            line.append((i,j))

def dfs(sj):
    stk = [(0, sj)]
    v = [[0] * (n) for _ in range(h)]
    v[0][sj] = 1
    while stk:
        ci, cj = stk.pop()
        if ci == 2 * H:
            return cj

        for di, dj in ((0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= nj < n and v[ni][nj] == 0 and arr[ni][nj] == 1:  # 좌로 갔다가 다시 우로 돌아오지 않게.
                v[ni][nj] = 1
                stk.append((ni, nj))
                break

def check(ci,cj):
    n1j, n2j = cj-2, cj+2
    if n1j<1 and n2j>n-2:
        return True
    elif n1j<1 and n2j<=n-2 and arr[ci][n2j]==0:
        return True
    elif n1j>=1 and n2j>n-2 and arr[ci][n1j]==0:
        return True
    elif n1j>=1 and n2j<=n-2 and arr[ci][n1j]==0 and arr[ci][n2j]==0:
        return True

    return False



def addline(n,s, lst):
    if n==ans:
        if lst:
            combi.append(lst)
        return

    for i in range(s,len(line)):
        ci,cj = line[i]
        if (ci==1 or ci==h-2) and check(ci,cj):
            arr[ci][cj]=1
            addline(n+1, i+1, lst+[(ci,cj)])
            arr[ci][cj]=0
        elif not(ci==1 or ci==h-2) and check(ci,cj) and (not check(ci-2,cj) or not check(ci+2, cj) or arr[ci-2][cj]==1 or arr[ci+2][cj]==1):
            arr[ci][cj]=1
            addline(n+1, i+1, lst+[(ci,cj)])
            arr[ci][cj]=0

ans = 0
while ans<=3:
    combi =[]
    addline(0,0,[])
    flag2=False # 사다리가 완성되면 모든 반복을 끝낼 변수.
    if combi: # 조합이 가능 한 경우라면
        for x in combi: #조합에서
            for ci,cj in x: #ci,cj는 선을 추가할 곳 -> 양 옆에 이어지는 선이 있는지 확인.
                arr[ci][cj]=1 #선 추가
                for sj in range(0, 2 * N, 2): # 현재 조합이 가능한 사다리이므로 탐색.
                    ej = dfs(sj)
                    if sj == ej: #자기 자신과 같은 열에 도달.
                        continue
                    else:
                        break
                else: #사다리가 가능했다. 이제 모든 반복을 종료.
                    flag2=True
                    break

            if flag2:
                break
            else: #선을 다 놓아봤는데 도달 불가능하면 선을 추가해서 놓아봐야하므로
                for ci, cj in x: #사다리 원상복구
                    arr[ci][cj] = 0

    else: # combi가 없는 경우 # ans==0일 수도 있고.
        if ans==0: # 이경우는 사다리 안놓고 현재 상태 탐색해보기.
            for sj in range(0, 2 * N, 2):  # 현재 조합이 가능한 사다리이므로 탐색.
                ej= dfs(sj)
                if sj == ej:
                    continue
                else:
                    break
            else: # 한개도 안놓고 가능하므로 바로 반복 종료
                flag2 =True
        else: # 선 추가가 불가능한 경우.
            ans=-1
            flag2=True

    if flag2:
        break
    ans+=1 # 갯수를 올려서 반복.

if ans>3:
    print(-1)
else:
    print(ans)