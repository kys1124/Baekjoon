T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    cnt = 1
    ans = 0
    if N==M:
        if x==y:
            print(x)
        else:
            print(-1)
    else:
        if M>N:
            M,N = N,M
            x,y = y,x
            # 한라인에는 M개
            # i 번째 라인의 시작은 <1: (N+1-(i-1)*|N-M|)%N>
            # 한 라인에서는 모두 y-x 모두 일정. 만약 x>y 이면 |y+N-x|


        idx =1
        start= (1+(idx-1)*M)%N
        while idx<=N:
            if y-x>=0:
                if start-1==y-x:
                    break
                else:
                    idx+=1
                    start = (1 + (idx - 1) * M) % N
                    if start==0:
                        start=N
            else:
                if start-1==N+y-x:
                    break
                else:
                    idx+=1
                    start = (1 + (idx - 1) * M) % N
                    if start==0:
                        start=N
        if idx>N:
            print(-1)
        else:
            cnt+=M*(idx-1)
            si,sj = 1,start

            while (si,sj)!=(x,y):
                cnt+=1
                if si<M and sj<N:
                    si+=1
                    sj+=1
                elif si==M and sj<N:
                    si=1
                    sj+=1
                elif si<M and sj==N:
                    si+=1
                    sj=1
                else:
                    break

            print(cnt)