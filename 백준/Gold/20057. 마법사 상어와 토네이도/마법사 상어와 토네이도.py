N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
percentage = [1,1,2,7,7,2,10,10,5,'a']

dic = {0:[(-1,0),(1,0),(-2,-1),(-1,-1),(1,-1),(2,-1),(-1,-2),(1,-2),(0,-3),(0,-2)]}
for i in range(3):
    lst = []
    for di,dj in dic[i]:
        lst.append((-dj,di))
    dic[i+1] = lst

si,sj =N//2, N//2
sd = 0
v = [[0]*N for _ in range(N)]
v[si][sj]=1
ans = 0
for num in range(1,N**2):
    oi,oj = si+dir[sd][0], sj+dir[sd][1]
    v[oi][oj]=num
    cur_amt = arr[oi][oj]
    total = 0
    for i in range(9):
        di,dj = dic[sd][i]
        ni,nj = si+di,sj+dj
        lose = cur_amt * percentage[i] // 100
        total += lose
        if 0<=ni<N and 0<=nj<N:
            arr[ni][nj]+=lose
        else:
            ans+=lose
    di,dj = dic[sd][9]
    ni,nj = si+di, sj+dj
    lose = cur_amt - total
    if 0<=ni<N and 0<=nj<N:
        arr[ni][nj]+= lose
    else:
        ans+=lose
    si,sj = oi,oj
    if v[si+dir[(sd+1)%4][0]][sj+dir[(sd+1)%4][1]]==0:
        sd = (sd+1)%4
print(ans)
