from collections import deque

N, H, D = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# u 우산 위치 E 안전지대, . 빈칸

for i in range(N):
    for j in range(N):
        if arr[i][j]=='S':
            si,sj = i,j
            arr[i][j]='.'
        elif arr[i][j]=='E':
            ei,ej = i,j

def bfs():
    q= deque([(si,sj,0,H)])
    v = [[0]*N for _ in range(N)]
    v[si][sj]=H
    cnt = 0
    while q:
        for _ in range(len(q)):
            ci,cj,cd,ch = q.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='.' and v[ni][nj]<cd+ch-1:
                    if cd==0 and ch==1:
                        continue
                    v[ni][nj] = cd+ch-1
                    if cd>0:
                        q.append((ni,nj,cd-1,ch))
                    else:
                        q.append((ni,nj,cd,ch-1))

                elif 0<=ni<N and 0<=nj<N and arr[ni][nj]=='U' and v[ni][nj]<D+ch-1:
                    v[ni][nj] = D-1+ch
                    q.append((ni,nj,D-1, ch))

                elif 0<=ni<N and 0<=nj<N and arr[ni][nj]=='E':
                    return cnt+1
        cnt+=1
    return -1
print(bfs())