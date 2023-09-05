dice = list(map(int, input().split()))

ans= 0 # 정답 최댓값 갱신 전역 변수

a=[0,0,0,0] # 말 처음 위치
dic ={-1:0, 0:0,1:2,2:4,3:6,4:8,5:10,
      6:12,7:14,8:16,9:18,10:20,
      11:22,12:24,13:26,14:28,15:30,
      16:32,17:34,18:36,19:38,20:40,
      21:13,22:16,23:19,
      24:22,25:24,
      26:28,27:27,28:26,
      29:25,30:30,31:35
      }


def dfs(n, sm): # n은 턴 수 10까지, sm은 점수 갱신 4^10이라 2^20= 1e6이라 안정
    global ans
    if n==10:
        ans = max(ans, sm)
        return

    for i in range(4):
        if a[i]==-1:
            continue

        temp = a[i]
        if a[i] <= 20 and a[i] != 5 and a[i] != 10 and a[i] != 15:  # 바깥쪽 회전
            a[i] += dice[n]
            if a[i] > 20:  # 도착
                a[i] = -1
        elif a[i] == 5 or 21 <= a[i] <= 23:  # 10에서 오는 지름길
            if a[i] == 5: #5이면 key 건너뜀.
                if dice[n] <= 3:
                    a[i] = 20 + dice[n]
                else:
                    a[i] = 25 + dice[n]

            elif a[i] + dice[n] <= 23:
                a[i] += dice[n]

            else:
                a[i] += dice[n] + 5
                if a[i] == 32:
                    a[i] = 20
                elif a[i] > 32:
                    a[i] = -1

        elif a[i] == 10 or 24 <= a[i] <= 25:  # 20->지름길
            if a[i] == 10:
                if dice[n] <= 2:
                    a[i] = 23 + dice[n]
                else:
                    a[i] = 26 + dice[n]

            elif a[i] + dice[n] <= 25:
                a[i] += dice[n]

            else:
                a[i] += dice[n] + 3
                if a[i] == 32:
                    a[i] = 20
                elif a[i] > 32:
                    a[i] = -1

        elif a[i] == 15 or 26 <= a[i] <=31:
            if a[i]== 15:
                a[i] = 25 + dice[n]

            else:
                a[i]+= dice[n]
                if a[i] == 32:
                    a[i] = 20
                elif a[i] > 32:
                    a[i] = -1

        if a[i]==-1:
            dfs(n+1, sm)
        else:
            if (a[i] != a[(i + 1) % 4] and a[i] != a[(i + 2) % 4] and a[i] != a[(i + 3) % 4]):
                dfs(n + 1, sm + dic[a[i]])
        a[i] = temp

dfs(0,0)
print(ans)