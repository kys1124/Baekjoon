N,M = map(int, input().split())
campus = [input() for _ in range(N)]

v = [[0]*M for _ in range(N)]
people = 0

for i in range(N):
    for j in range(M):
        if campus[i][j]=='I':
            si,sj = i,j


from collections import deque
def bfs():
    global people
    q = deque([(si,sj)])
    v[si][sj]=1

    while q:
        ci,cj = q.popleft()
        if campus[ci][cj]=='P':
            people+=1

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and campus[ni][nj]!='X':
                v[ni][nj]=1
                q.append((ni,nj))

bfs()
if people==0:
    print('TT')
else:
    print(people)