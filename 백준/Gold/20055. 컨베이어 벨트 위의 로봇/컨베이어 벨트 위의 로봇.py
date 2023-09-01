N,K = map(int, input().split())
lst =list(map(int, input().split()))  # 2N 컨베이어 벨트 리스트 내구도
robolst = [0]*(2*N) #로봇 있는지 없는지 체크
# idx=0 이면 올리는 위치, N-1은 내리는 위치
t =0
cnt = 0
while cnt<K: # 종료 조건 내구도가 0인 칸이 K개 이상 #cnt는 내구도가 0인 칸 수
    # 컨베이어 벨트 내구도와 로봇 다같이 인덱스 하나씩 옮기기
    a = lst.pop()  # 맨 뒤 값 pop
    lst.insert(0, a)  # 맨 앞으로 붙이기
    b = robolst.pop()
    robolst.insert(0, b)
    if robolst[N-1]==1:
        robolst[N-1]=0 # N번 칸에 왔으므로 바로 제거

    for i in range(N-2,-1,-1): #N번째 오면 무조건 로봇이 내리고, 먼저 온 로봇 부터 움직이므로, 1~N까지만 관리
        if robolst[i]==1: # 로봇이 있을 경우,
            if robolst[i+1]==0 and lst[i+1]>0: #이동 가능한 경우
                if i+1==N-1: #N번째 오면 내리기
                    lst[i+1]-=1
                    if lst[i+1]==0:
                        cnt+=1
                    robolst[i]=0
                else: #아니면 한칸 이동
                    robolst[i+1]=1
                    lst[i+1]-=1
                    if lst[i+1]==0:
                        cnt+=1
                    robolst[i]=0
        else:
            continue

    if lst[0]!=0:
        lst[0]-=1
        if lst[0]==0:
            cnt+=1
        robolst[0]=1

    t+=1
print(t)
