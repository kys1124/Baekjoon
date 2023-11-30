N, K = map(int, input().split()) # N은 손동작 수, K는 필요 승수

arr =[list(map(int, input().split())) for _ in range(N)]
# N*N으로 i번 행이 j번 행을 상대로 어떻게 되는지
# 1 무승부 0은 i패배, 2는 i승.
dic = {0:(1,2),1:(0,2),2:(0,1)}
lst = [list(map(lambda  x:int(x)-1, input().split())) for _ in range(2)]


v = [0]*N # 지우가 N개의 동작을 이전에 하였는지 판단.
result = [0,0,0]
play = [0,0,0]
ans = 0
flag= False
def dfs(play,pre_lose, result):
    global flag, ans
    if flag:
        return

    if play[0]>N:
        return

    if result[1]>=K or result[2]>=K:
        return

    if result[0]==K and result[1]<K and result[2]<K:
        flag=True
        ans = 1
        return

    p1,p2 = dic[pre_lose]
    if p1==0: #지우가 참여하는 경기.
        cur = lst[p2-1][play[p2]]
        for i in range(N):
            copy_play = play[:]
            copy_result = result[:]
            if v[i]==0:
                v[i]=1
                play[p1]+=1
                play[p2]+=1
                if arr[i][cur]==2:
                    result[p1]+=1
                    dfs(play, p2, result)
                else:
                    result[p2]+=1
                    dfs(play,p1,result)
                v[i]=0
                play = copy_play
                result = copy_result


    else: # 지우가 참여하지 않는 경기
        cur1 = lst[p1-1][play[p1]]
        cur2 = lst[p2-1][play[p2]]
        copy_play = play[:]
        copy_result = result[:]
        play[p1]+=1
        play[p2]+=1
        if arr[cur1][cur2]==2:
            result[p1]+=1
            dfs(play,p2, result)
        else:
            result[p2]+=1
            dfs(play,p1,result)

        play = copy_play
        result = copy_result


dfs(play, 2, result)
print(ans)