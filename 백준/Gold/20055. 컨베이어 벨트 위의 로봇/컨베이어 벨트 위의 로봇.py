N,K = map(int, input().split())
arr = list(map(int, input().split()))
robot = [0]*(2*N)
cnt = 0
T = 1
while True:
    arr.insert(0, arr.pop())
    robot.insert(0, robot.pop())

    robot[N-1] =0

    for i in range(N-2,-1,-1):
        if robot[i]==1 and robot[i+1]==0 and arr[i+1]>0:
            arr[i+1]-=1
            if arr[i+1]==0:
                cnt+=1
            robot[i+1]=1
            robot[i]=0

    robot[N-1]=0

    if arr[0]>0:
        arr[0]-=1
        robot[0]=1
        if arr[0]==0:
            cnt+=1

    if cnt>=K:
        break
    T+=1
print(T)