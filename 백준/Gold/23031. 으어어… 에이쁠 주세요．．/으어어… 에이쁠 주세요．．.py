N = int(input())
text = input()
arr = [list(input()) for _ in range(N)]
# 'z' 학생 좀비, 's' 형광등 스위치, 'o' 빈칸
si,sj,sd = 0,0,0
dir = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}
v = [[0]*N for _ in range(N)]
stu = {}
for i in range(N):
    for j in range(N):
        if arr[i][j]=='Z':
            stu[(i,j)] = 0


ans = 'Phew...'
for cmd in text:
    if cmd=='R':
        sd = (sd+1)%4
    elif cmd=='L':
        sd = (sd-1)%4
    else:
        ni,nj = si+dir[sd][0] ,sj+dir[sd][1]
        if 0<=ni<N and 0<=nj<N:
            si,sj = ni,nj
    if arr[si][sj]=='S':
        for di,dj in ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(0,0)):
            ni,nj = si+di,sj+dj
            if 0<=ni<N and 0<=nj<N:
                v[ni][nj]=1
        arr[si][sj]='O'
    else:
        if v[si][sj]==0 and (si,sj) in stu:
            ans = "Aaaaaah!"
            break

    new_stu = {}
    for key, value in stu.items():
        ci,cj = key
        cd = value
        ni,nj=  ci+dir[cd][0], cj+dir[cd][1]
        if 0<=ni<N and 0<=nj<N:
            new_stu[(ni,nj)] = cd
        else:
            cd = (cd+2)%4
            new_stu[(ci,cj)] = cd

    stu = new_stu
    if v[si][sj]==0 and (si,sj) in stu:
        ans = 'Aaaaaah!'
        break

print(ans)



