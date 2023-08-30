arr = [list(map(str, input())) for _ in range(12)]


from collections import deque

def check(si,sj):
    q = deque([(si,sj)])
    cnt = 1
    lst = []
    while q:
        ci,cj = q.popleft()
        lst.append((ci,cj))
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<12 and 0<=nj<6 and v[ni][nj]==0 and arr[ni][nj]==arr[si][sj]:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1

    if cnt>=4:
        return lst

    else:
        return []

turn = 0
while True:
    flag =False
    v=[[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j]!='.' and v[i][j]==0:
                v[i][j]=1
                lst = check(i,j)
                if lst:
                    flag=True
                    for ci,cj in lst:
                        arr[ci][cj]='.'

    if flag:
        for j in range(6):
            for i in range(11,0,-1):
                idx =i
                if arr[i][j]=='.':
                    while idx>=0 and arr[idx][j]=='.':
                        idx-=1
                    if idx==-1:
                        continue
                    arr[i][j] = arr[idx][j]
                    arr[idx][j]='.'
        turn +=1
        continue
    else:
        break

print(turn)



