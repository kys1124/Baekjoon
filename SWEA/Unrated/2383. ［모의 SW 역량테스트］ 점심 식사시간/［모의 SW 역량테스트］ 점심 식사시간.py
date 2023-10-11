import heapq
T = int(input())
def dfs(n,stair1, stair2):
    global ans
    if n==len(people):
        if len(stair2)+len(stair1)==len(people):
            ans = min(ans, max(cal(stair1[:],k1), cal(stair2[:], k2)))
        return

    dfs(n+1, stair1+[(stair1_time[n],0,n)], stair2)
    dfs(n+1, stair1, stair2+[(stair2_time[n],0,n)])

def cal(pq,k): #계단 걸리는 시간.
    heapq.heapify(pq)
    cnt = 0
    t = 0 # 최종 pq가 없어지는 시간.
    in_stair_t = [0,0,0]
    while pq:
        ct, flag, num = heapq.heappop(pq)
        t = ct
        if flag==0: # 계단이 비어 있고 아직 계단에 안들어감.
            heapq.heappush(pq,(ct+1, -1, num))

        elif flag==-1 and cnt<3:
            heapq.heappush(pq,(ct+k,-2, num))
            cnt+=1
            for i in range(3):
                if in_stair_t[i]==0:
                    in_stair_t[i]=ct+k
                    break

        elif flag==-1 and cnt==3:
            heapq.heappush(pq,(in_stair_t[0],-1,num))

        elif flag==-2:
            cnt-=1
            in_stair_t.pop(0)
            in_stair_t.append(0)
    return t

for tc in range(1,1+T):
    N = int(input()) # NxN 격자  4<=N<=10, 1<= 1 갯수 <=10 계단 입구는 반드시 2개.
    # 겹치지 않는다. 길이는 2~10 사람과 계단은 안 겹침.
    arr = [list(map(int, input().split())) for _ in range(N)] # 1 사람 2>= 계단 입구와 값은 길이.
    # 계단 입구까지  이동 시간 -> 택시 거리
    # 계단 입구에 도착하면 1분에 한칸씩 내려갈 수 있음.
    # 계단에는 최대 3명까지 올라갈 수 있음.
    # 3명이 내려가고 있으면 그 다음 사람은 대기
    # K길이의 계단은 K분 걸림.
    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                people.append((i,j))
            elif arr[i][j]>1:
                stair.append((i,j))

    stair1_time = [0]*len(people)
    stair2_time = [0]*len(people)
    for idx, (ci,cj) in enumerate(people):
        e1i,e1j = stair[0]
        e2i,e2j = stair[1]
        stair1_time[idx] = abs(e1i-ci)+abs(e1j-cj)
        stair2_time[idx] = abs(e2i-ci)+abs(e2j-cj)

    k1 = arr[stair[0][0]][stair[0][1]]
    k2 = arr[stair[1][0]][stair[1][1]]
    ans = 10000000
    dfs(0,[],[])
    print(f'#{tc} {ans}')
    # break