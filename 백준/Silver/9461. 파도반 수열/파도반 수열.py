T = int(input())
for _ in range(T):
    N = int(input())
    if N<=3:
        print(1)
    elif N<5:
        print(2)
    else:
        lst = [0]*(N+1)
        lst[1]=lst[2]=lst[3]=1
        lst[4]=lst[5]=2
        for i in range(6,N+1):
            lst[i] = lst[i-1]+lst[i-5]
        print(lst[N])