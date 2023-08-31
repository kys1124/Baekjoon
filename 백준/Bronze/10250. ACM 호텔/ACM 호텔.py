T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split()) #호텔 층수, 층별 방수, 손님 번호

    n = N//H
    a = N%H
    if a==0:
        a = H
    else:
        n+=1


    if n<10:
        print(str(a)+'0'+str(n))
    else:
        print(str(a)+str(n))
