N = int(input()) #집 수
lst = list(map(int, input().split())) #집 앞에 쌓인 눈
for i in range(N):
    lst[i] *= -1

time = 0
import heapq
heapq.heapify(lst)

if N==1:
    if -lst[0]>1440:
        print(-1)
    else:
        print(-lst[0])
else:
    while len(lst)>1:
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        time += -b

        if b-a!=0:
            heapq.heappush(lst,a-b)

    if len(lst)==0:
        if time>1440:
            print(-1)
        else:
            print(time)
    else:
        if time-lst[0]>1440:
            print(-1)
        else:
            print(time-lst[0])