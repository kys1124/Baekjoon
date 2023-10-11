from collections import deque
N, M, P = map(int, input().split()) # NxM  P명
S_lst = [0]+list(map(int, input().split())) # i번 사람은 i인덱스 값만큼 확장 가능
arr = [list(map(str, input())) for _ in range(N)]

adj = [deque([]) for _ in range(1+P)]
p_cnt = [0]*(P+1)
for i in range(N):
    for j in range(M):
        if arr[i][j].isdigit():
            adj[int(arr[i][j])].append((i,j))
            p_cnt[int(arr[i][j])]+=1

check = [0]+[0]*P

while True:
    for i in range(1,P+1):
        flag = True
        if not check[i]:
            t=0
            while adj[i]:
                if t>=S_lst[i]:
                    break
                for _ in range(len(adj[i])):
                    ci,cj = adj[i].popleft()
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj =ci+di,cj+dj
                        if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='.':
                            arr[ni][nj]=str(i)
                            adj[i].append((ni,nj))
                            p_cnt[i]+=1
                            flag=False
                t+=1

        if flag:
            check[i]=1
    if sum(check)==P:
        break
print(*p_cnt[1:])
