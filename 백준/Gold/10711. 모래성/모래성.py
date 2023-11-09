from collections import deque
H,W = map(int, input().split())
v =[[0]*W for _ in range(H)]

arr =[list(map(str, input())) for _ in range(H)]

dir = {1:(1,0),2:(1,1),3:(0,1),4:(-1,1),5:(-1,0),6:(-1,-1),7:(0,-1),8:(1,-1)}
q = deque([])
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if arr[i][j] != '.':
            temp = 0
            for d in range(1, 9):
                ni, nj = i + dir[d][0], j + dir[d][1]
                if arr[ni][nj] == '.':
                    temp += 1
            v[i][j] = temp
            if v[i][j] >= int(arr[i][j]):
                q.append((i, j))

t = 0
while q:
    S = set(q)
    for _ in range(len(q)):
        ci,cj = q.popleft()
        arr[ci][cj]='.'
        for d in range(1, 9):
            ni, nj = ci + dir[d][0], cj + dir[d][1]
            if arr[ni][nj]!='.':
                v[ni][nj]+=1
            if arr[ni][nj]!='.' and v[ni][nj]>=int(arr[ni][nj]) and (ni,nj) not in S:
                q.append((ni,nj))
                S.add((ni,nj))

    t+=1
print(t)