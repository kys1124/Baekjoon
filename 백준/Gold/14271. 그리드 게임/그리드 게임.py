N,M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
K = int(input())
v = set()
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='o':
            q.append((i,j))
            v.add((i,j))

total = len(q)
cnt = 0
while q:
    temp_q = []
    for i in range(len(q)):
        ci,cj = q[i]
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj =ci+di, cj+dj
            if (ni,nj) not in v:
                v.add((ni,nj))
                temp_q.append((ni,nj))
    cnt+=1
    total+=len(temp_q)
    q = temp_q
    if cnt==K:
        break
print(total)