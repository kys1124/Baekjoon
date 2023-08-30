t = int(input())

for tc in range(1,t+1):
    n = int(input())
    if n==0:
        print(1,0)
    elif n==1:
        print(0,1)
    else:
        arr = [[1,0]]+[[0,1]]+[[0,0]]*(n-1)
        for i in range(2,n+1):
            arr[i] = [arr[i-1][0]+arr[i-2][0],arr[i-1][1]+arr[i-2][1]]
        print(*arr[n])