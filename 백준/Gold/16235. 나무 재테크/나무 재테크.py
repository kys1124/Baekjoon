N,M,K = map(int, input().split())
ground = [[5]*N for _ in range(N)] # 토양 양분 기록
def spring_summer_winter():
    for i in range(N):
        for j in range(N):
            sm = 0  # 죽은 나무 양분으로 전환
            lst2 = []
            if tree[i][j]: # i,j에 나무가 존재
                lst = tree[i][j]
                lst.sort()
                for value in lst:
                    if value<=ground[i][j]:
                        ground[i][j]-=value
                        value +=1
                        lst2.append(value)
                    else:
                        sm+=value//2
            tree[i][j] = lst2
            ground[i][j] += sm # 죽은 나무 양분 추가
            ground[i][j]+= s2d2[i][j] # 겨울 양분 추가

def fall():
    for i in range(N):
        for j in range(N):
            for x in tree[i][j]:
                if x%5==0: # i,j 땅의 나무 나이가 5의 배수
                    for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                        ni,nj = i+di, j+dj
                        if 0<=ni<N and 0<=nj<N:
                            tree[ni][nj].append(1)




s2d2=[list(map(int, input().split())) for _ in range(N)]

tree = [[[]*N for _ in range(N)] for _ in range(N)]  # 살아있는 나무 나이 기록
for _ in range(M):
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

for _ in range(K):
    spring_summer_winter()
    fall()

ans = 0

for i in range(N):
    for j in range(N):
        ans +=len(tree[i][j])

print(ans)