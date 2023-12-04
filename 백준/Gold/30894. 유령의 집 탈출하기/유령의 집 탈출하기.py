from collections import deque
N, M = map(int, input().split())
si,sj, ei, ej = map(lambda x:int(x)-1, input().split())
arr = [list(input()) for _ in range(N)]
dir = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

ghost = [[] for _ in range(4)]
v = [[[0]*M for _ in range(N)] for _ in range(4)]
for i in range(N):
    for j in range(M):
        if arr[i][j]!='#' and arr[i][j]!='.':
            direction = int(arr[i][j])
            for turn in range(4):
                ghost[turn].append((i,j,direction))
                direction = (direction+1)%4

ghost_v= [[[0]*M for _ in range(N)] for _ in range(4)]
def check(ghost):
    for i in range(4):
        for ci,cj,cd in ghost[i]:
            di,dj = dir[cd]
            for mul in range(1,max(N,M)+1):
                ni,nj = ci+mul*di,cj+mul*dj
                if not (0<=ni<N and 0<=nj<M):
                    break
                elif arr[ni][nj]!='.':
                    break
                ghost_v[i][ni][nj]=1

check(ghost)

def bfs(si,sj,ei,ej):
    v[0][si][sj]= 1
    q = deque([(si,sj)])
    turn = 0
    while q:
        t = (turn+1)%4
        for _ in range(len(q)):
            ci,cj = q.popleft()
            if (ci,cj)==(ei,ej):
                return turn

            for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(0,0)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and v[t][ni][nj]==0 and ghost_v[t][ni][nj]==0 and arr[ni][nj]=='.':
                    q.append((ni,nj))
                    v[t][ni][nj]=turn+1
        turn+=1

    return -1

ans = bfs(si,sj,ei,ej)
if ans==-1:
    print('GG')
else:
    print(ans)