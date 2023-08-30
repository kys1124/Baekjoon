from collections import deque

M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
si,sj,sdir = map(int, input().split())
ei,ej,edir = map(int, input().split())

dic = {0:(0,1),1:(0,-1) ,2:(1,0) ,3:(-1,0)}


def bfs():

    q = deque([(si-1,sj-1,sdir-1,0)])
    v = [[[-1]*N for _ in range(M)] for _ in range(4)]
    v[sdir-1][si-1][sj-1]=0

    while q:
        ci,cj,cdir, cnt = q.popleft()

        if (ci,cj,cdir)==(ei-1,ej-1,edir-1):
            return cnt

        if cdir==0 or cdir==2:
            for direction in (2,3):
                ndir = (cdir+direction)%4
                if v[ndir][ci][cj]==-1 or v[ndir][ci][cj]>=cnt+1:
                    v[ndir][ci][cj]=cnt+1
                    q.append((ci,cj,ndir,cnt+1))
        else:
            for direction in (1,2):
                ndir = (cdir + direction) % 4
                if v[ndir][ci][cj] == -1 or v[ndir][ci][cj] >= cnt + 1:
                    v[ndir][ci][cj] = cnt + 1
                    q.append((ci, cj, ndir, cnt + 1))

        for k in range(1,4):
            ni, nj = ci+k*dic[cdir][0], cj+k*dic[cdir][1]
            if 0<=ni<M and 0<=nj<N and arr[ni][nj]==0 and (v[cdir][ni][nj]==-1 or v[cdir][ni][nj]>=cnt+1):
                v[cdir][ni][nj] = cnt+1
                q.append((ni,nj,cdir,cnt+1))
            else:
                break




print(bfs())