from collections import deque
N, M = map(int, input().split())

dir = {0: (2, 1), 1: (1, 2), 2: (2, -1), 3: (1, -2), 4: (-1, 2), 5: (-2, -1), 6: (-2, 1),
       7: (-1, -2)}
arr = [list(map(str, input())) for _ in range(N)]
V = [[[0]*M for _ in range(N)] for _ in range(2)]

sm = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]!='.':
            sm +=1
            v = [[0]*M for _ in range(N)]
            q = deque([(i,j,int(arr[i][j]))])
            V[0][i][j] += 1
            v[i][j]=1
            cnt = 1
            while q:
                for _ in range(int(arr[i][j])):
                    for _ in range(len(q)):
                        ci,cj, number = q.popleft()
                        for d in range(8):
                            ni,nj = ci+dir[d][0], cj+dir[d][1]
                            if 0<=ni<N and 0<=nj<M and (v[ni][nj]==0 or v[ni][nj]>cnt):
                                q.append((ni,nj,number))
                                v[ni][nj]=cnt
                                V[0][ni][nj]+=1
                cnt+=1

            for r in range(N):
                for c in range(M):
                    if (r,c)!=(i,j):
                        V[1][r][c]+=v[r][c]

mn = 1234567890
for i in range(N):
    for j in range(M):
        if V[0][i][j]==sm:
            mn = min(mn, V[1][i][j])
if mn==1234567890:
    print(-1)
else:
    print(mn)

