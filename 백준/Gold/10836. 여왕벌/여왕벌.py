N,M = map(int, input().split())
arr = [[1]*N for _ in range(N)]
q = [(i,0) for i in range(N-1,-1,-1)]+[(0,i) for i in range(1,N)]

for _ in range(M):
    a,b,c= map(int, input().split())
    v = [[0]*N for _ in range(N)]
    for i,j in q:
        if a>0:
            v[i][j]=0
            a-=1
        elif b>0:
            v[i][j]=1
            arr[i][j]+=1
            b-=1
        elif c>0:
            v[i][j]=2
            arr[i][j]+=2
            c-=1

    for r in range(1,N):
        for c in range(1,N):
            v[r][c] = max(v[r-1][c-1], v[r][c-1], v[r-1][c])
            arr[r][c] +=v[r][c]

for x in arr:
    print(*x)

