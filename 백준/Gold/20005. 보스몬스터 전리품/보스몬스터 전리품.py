from collections import deque
N, M, P = map(int, input().split())
arr = [list(input()) for _ in range(N)]

q = deque()
v_dic = {}
check = dict()
dps = dict()
for _ in range(P):
    a,b = input().split()
    dps[a] = int(b)
hp = int(input())

for i in range(N):
    for j in range(M):
        if arr[i][j]!='.' and arr[i][j]!='X' and arr[i][j]!='B':
            q.append((i,j,arr[i][j]))
            v_dic[arr[i][j]] = [[0] * M for _ in range(N)]
            v_dic[arr[i][j]][i][j]=1
            check[arr[i][j]] = 0

def bfs(q):
    global hp
    while q:
        for _ in range(len(q)):
            ci,cj, alphabet= q.popleft()
            if arr[ci][cj]!='B':
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<N and 0<=nj<M and v_dic[alphabet][ni][nj]==0 and arr[ni][nj]!='X':
                        v_dic[alphabet][ni][nj]=1
                        q.append((ni,nj,alphabet))

            else:
                check[alphabet]=1
                hp-=dps[alphabet]
                q.append((ci,cj,alphabet))

        if hp<=0:
            break

bfs(q)
ans = 0
for value in check.values():
    if value==1:
        ans+=1
print(ans)