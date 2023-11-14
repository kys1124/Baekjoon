N, M, K = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(N)]
arr =[[5]*N for _ in range(N)]
tree =[[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)


for _ in range(K):
    dead = []
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                new_tree = []
                tree[i][j].sort()
                sm = 0
                for age in tree[i][j]:
                    if arr[i][j]>=age:
                        new_tree.append(age+1)
                        arr[i][j]-=age
                    else:
                        sm += age//2
                tree[i][j] = new_tree
                dead.append((i,j,sm))

    for ci,cj, val in dead:
        arr[ci][cj]+=val

    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age%5==0:
                        for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                            ni,nj =i+di,j+dj
                            if 0<=ni<N and 0<=nj<N:
                                tree[ni][nj].append(1)

    for i in range(N):
        for j in range(N):
            arr[i][j]+=s2d2[i][j]


cnt = 0
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            cnt+=len(tree[i][j])
print(cnt)