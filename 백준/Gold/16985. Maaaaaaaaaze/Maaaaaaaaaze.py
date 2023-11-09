def rotate(arr):
    new = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[i][j] = arr[4-j][i]
    return new

dic ={0:[],1:[],2:[],3:[],4:[]}
for i in range(5):
    arr = [list(map(int, input().split())) for _ in range(5)]

    dic[i].append(arr)
    for j in range(3):
        new_arr = rotate(dic[i][j])
        dic[i].append(new_arr)


def bfs(arr):
    q = [(0,0,0)]
    cnt = 0
    v = [[[0]*5 for _ in range(5)] for _ in range(5)]
    v[0][0][0]=1
    while q:
        temp_q = []
        for i in range(len(q)):
            ci,cj,ck = q[i]
            if (ci,cj,ck)==(4,4,4):
                return cnt

            for di,dj,dk in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
                ni,nj,nk = ci+di,cj+dj,ck+dk
                if 0<=ni<5 and 0<=nj<5 and 0<=nk<5 and v[ni][nj][nk]==0 and arr[ni][nj][nk]==1:
                    v[ni][nj][nk]=1
                    temp_q.append((ni,nj,nk))
        cnt+=1
        q = temp_q
    return 123456789

ans = 123456789
visited = [0]*5
def dfs(n,arr):
    global ans
    if ans==12:
        return

    if n==5:
        if arr[0][0][0]==1 and arr[4][4][4]==1:
            ans = min(ans, bfs(arr))
        return

    for i in range(5):
        if visited[i]==0:
            visited[i] = 1
            for j in range(4):
                arr.append(dic[i][j])
                dfs(n+1, arr)
                arr.pop()
            visited[i]=0

dfs(0,[])
if ans==123456789:
    print(-1)
else:
    print(ans)