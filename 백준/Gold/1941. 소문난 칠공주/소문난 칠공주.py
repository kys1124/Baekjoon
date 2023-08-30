arr = [input() for _ in range(5)]

ans = 0
v = [[0]*5 for _ in range(5)]

S = set()
def dfs(n,cnt, lst): #n ==6, cnt -> y 수
    global ans
    if cnt>=4:
        return

    if n==6:
        tp = tuple(sorted(lst, key=lambda x:(x[0],x[1])))
        if tp not in S:
            S.add(tp)
            ans+=1
        return


    for si,sj in lst:
        v[si][sj]=1
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni,nj = si+di,sj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0:
                v[ni][nj]=1
                if arr[ni][nj]=='Y':
                    dfs(n+1,cnt+1, lst+[(ni,nj)])
                else:
                    dfs(n+1,cnt, lst+[(ni,nj)])
                v[ni][nj]=0


for i in range(5):
    for j in range(5):
        if arr[i][j]=='S':
            dfs(0,0,[(i,j)])
print(ans)
