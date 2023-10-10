I, N, K = map(int, input().split())
text = input()
arr = [list(map(str, input())) for _ in range(N)]
dir = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
cmd_lst = input()

ink = 0
jump = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]=='@':
            si,sj = i,j

for cmd in cmd_lst:
    if cmd in dir:
        ni,nj = si+dir[cmd][0], sj+dir[cmd][1]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='.':
            arr[si][sj]='.'
            arr[ni][nj]='@'
            si,sj = ni,nj

    elif cmd=='j':
        ink+=1

    elif cmd=='J':
        mi = ink
        ci = text[jump]
        jump = (jump+1)%len(text)
        for i in range(N):
            for j in range(N):
                if abs(i-si)+abs(j-sj)<=mi:
                    if arr[i][j]!='.' and arr[i][j]!='@':
                        arr[i][j]=ci
        ink=0

for x in arr:
    print(*x, sep='')