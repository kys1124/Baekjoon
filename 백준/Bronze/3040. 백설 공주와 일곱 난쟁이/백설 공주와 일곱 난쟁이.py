arr = [int(input()) for _ in range(9)]

v= [0]*9
def dfs(n, sm, lst):
    if n==7:
        if sm==100:
            for x in lst:
                print(x)
            exit()
        return

    if sm>100:
        return

    for i in range(9):
        if v[i]==0:
            v[i]=1
            dfs(n+1, sm+arr[i], lst+[arr[i]])
            v[i]=0

dfs(0,0,[])