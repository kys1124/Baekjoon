from collections import deque
arr = []
total_dic = {}
def rotate(arr):
    new = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[i][j] = arr[4-j][i]
    return new

for num in range(5):
    dic = {}
    small_arr = [list(map(int, input().split())) for _ in range(5)]
    dic[0] = small_arr
    for i in range(1,4):
        dic[i] = rotate(dic[i-1])
    total_dic[num] = dic

def bfs(arr):
    if arr[0][0][0]==0:
        return 5*5*5+1
    q = deque([(0,0,0)])
    v = [[[0]*5 for _ in range(5)] for _ in range(5)]
    v[0][0][0]=1
    cnt = 0
    while q:
        for _ in range(len(q)):
            ci,cj,ck = q.popleft()
            if (ci,cj,ck)==(4,4,4):
                return cnt

            for di,dj,dk in ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)):
                ni,nj,nk = ci+di,cj+dj,ck+dk
                if 0<=ni<5 and 0<=nj<5 and 0<=nk<5 and v[ni][nj][nk]==0 and arr[ni][nj][nk]==1:
                    q.append((ni,nj,nk))
                    v[ni][nj][nk]=1
        cnt+=1
    return 5*5*5+1


ans = 5*5*5+1
v = [0,0,0,0,0]
def dfs(n,  lst):
    global ans
    if n==5:
        ans = min(ans, bfs(lst))
        return

    for num in range(5):
        if v[num]==0:
            v[num]=1
            for i in range(4):
                lst.append(total_dic[num][i])
                dfs(n+1, lst)
                lst.pop()
            v[num]=0

dfs(0,[])
if ans==5*5*5+1:
    print(-1)
else:
    print(ans)