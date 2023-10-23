from collections import deque
R, C = map(int, input().split())

dic = {'|':((1,0),(-1,0)),'-':((0,1),(0,-1)),'+':((1,0),(-1,0),(0,1),(0,-1)),
       '1':((1,0),(0,1)),
       '2':((-1,0),(0,1)),
       '3':((-1,0),(0,-1)),
       '4':((1,0),(0,-1))}
arr = [list(input()) for _ in range(R)]
v = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j]=='M':
            v[i][j] = 1e9
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = i+di,j+dj
                if 0<=ni<R and 0<=nj<C and arr[ni][nj]!='.' and arr[ni][nj]!='Z':
                    si,sj = ni,nj

        elif arr[i][j]=='Z':
            ei,ej = i,j


def bfs():
    q = deque([(si,sj)])
    v[si][sj]=1
    cnt = 2
    while q:
        for _ in range(len(q)):
            ci,cj = q.pop()
            if (ci,cj)==(ei,ej):
                continue
            for di,dj in dic[arr[ci][cj]]:
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<R and 0<=nj<C and v[ni][nj]==0 and arr[ni][nj]!='.':
                        v[ni][nj]=cnt
                        q.append((ni,nj))

                    elif not (0<=ni<R and 0<=nj<C) or arr[ni][nj]=='.':
                        lst = [0,0,0,0]
                        nni,nnj = ni-1,nj
                        if 0<=nni<R and 0<=nnj<C and arr[nni][nnj]!='.' and  arr[nni][nnj]!='-' and  arr[nni][nnj]!='2' and  arr[nni][nnj]!='3':
                            if arr[nni][nnj]!='M' and arr[nni][nnj]!='Z':
                                lst[0]=1
                        nni,nnj = ni,nj+1
                        if 0 <= nni < R and 0 <= nnj < C and arr[nni][nnj] != '.' and  arr[nni][nnj] != '|' and  arr[nni][nnj] != '2' and  arr[nni][nnj] != '1':
                            if arr[nni][nnj] != 'M' and arr[nni][nnj] != 'Z':
                                lst[1] = 1
                        nni,nnj = ni+1, nj
                        if 0 <= nni < R and 0 <= nnj < C and arr[nni][nnj] != '.' and arr[nni][nnj] != '-' and arr[nni][
                            nnj] != '1' and arr[nni][nnj] != '4':
                            if arr[nni][nnj] != 'M' and arr[nni][nnj] != 'Z':
                                lst[2] = 1
                        nni,nnj = ni, nj-1
                        if 0 <= nni < R and 0 <= nnj < C and arr[nni][nnj] != '.' and arr[nni][nnj] != '|' and arr[nni][
                            nnj] != '3' and arr[nni][nnj] != '4':
                            if arr[nni][nnj] != 'M' and arr[nni][nnj] != 'Z':
                                lst[3] = 1
                        if sum(lst)==4:
                            return ni+1,nj+1,'+'
                        elif lst[0]==1 and lst[2]==1:
                            return ni+1,nj+1, '|'
                        elif lst[1]==1 and lst[3]==1:
                            return ni+1, nj+1, '-'
                        elif lst[0]==1 and lst[1]==1:
                            return ni+1, nj+1, '2'
                        elif lst[0]==1 and lst[3]==1:
                            return ni+1, nj+1, '3'
                        elif lst[1]==1 and lst[2]==1:
                            return ni+1, nj+1, '1'
                        elif lst[2]==1 and lst[3]==1:
                            return ni+1, nj+1, '4'

print(*bfs())
