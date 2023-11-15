N, M = map(int, input().split())
arr = [['I']*(M+2)] +[['I']+list(map(str, input()))+['I'] for _ in range(N)]+[['I']*(M+2)]

# . 바다 I 섬 V 해적 Y 수아 T 보물
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]=='Y':
            arr[i][j]='.'
            si,sj= i,j
        elif arr[i][j]=='V':
            vi,vj = i,j
            arr[i][j]='.'
        elif arr[i][j]=='T':
            ei,ej = i,j

from collections import deque
q = deque([(vi,vj,0,1),(si,sj,0,0)])
vy =[[-1]*(M+2) for _ in range(N+2)]
vv = [[-1]*(M+2) for _ in range(N+2)]
def bfs(q):
    vy[si][sj]=0
    vv[vi][vj]=0

    while q:
        for _ in range(len(q)):
            ci,cj,t,num = q.popleft()
            if num==0: # 수아
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = ci+di,cj+dj
                    if arr[ni][nj]!='I' and vy[ni][nj]==-1 and check(t,ni,nj):
                        if (ni,nj)==(ei,ej):
                            return True
                        vy[ni][nj]=t
                        q.append((ni,nj,t+1,num))

            else: #해적
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = ci+di,cj+dj
                    if arr[ni][nj]!='I' and vv[ni][nj]==-1:
                        vv[ni][nj]=t
                        q.append((ni,nj,t+1,num))
    return False

def check(t,i,j): # 수아가 해적에게 죽는지 확인하는 함수
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        for mul in range(max(N,M)):
            ni,nj = i+mul*di, j+mul*dj
            if arr[ni][nj]=='I':
                break
            elif vv[ni][nj]==-1:
                continue

            elif arr[ni][nj]!='I' and vv[ni][nj]<=t:
                return False
            elif arr[ni][nj]=='I':
                break
    return True

if bfs(q):
    print('YES')
else:
    print('NO')