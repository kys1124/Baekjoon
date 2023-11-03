N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dic = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}
end_lst =[]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='S':
            si,sj = i,j
            arr[i][j]='.'
        elif arr[i][j]=='C':
            end_lst.append((i,j))


def bfs(o,si,sj,ei,ej):
    q = [(si,sj,o)]
    v = [[[0]*M for _ in range(N)] for _ in range(4)]
    v[0][si][sj]=1
    cnt = 0
    while q:
        temp_q = []
        ans = []
        for i in range(len(q)):
            ci,cj,pre = q[i]
            if (ci,cj)==(ei,ej):
                ans.append(pre)

            for d in range(4):
                if d==pre:
                    continue
                di,dj = dic[d]
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and v[d][ni][nj]==0 and arr[ni][nj]!='#':
                    temp_q.append((ni,nj,d))
                    v[d][ni][nj]=1
        q= temp_q
        if ans:
            return cnt, ans
        cnt+=1

    return -1, []

ans = [0,0]
ei1,ej1 = end_lst[0]
ei2, ej2 = end_lst[1]
ans1, one_lst = bfs(-1,si,sj, ei1,ej1)
if ans1==-1:
    ans[0]=-1
else:
    mx = 123456789
    for pre in one_lst:
        add, _  = bfs(pre, ei1,ej1,ei2,ej2)
        if add!=-1:
            mx = min(mx, ans1+add)
    if mx!=123456789:
        ans[0] = mx
    else:
        ans[0] =-1

ans2, two_lst = bfs(-1,si,sj,ei2,ej2)
if ans2==-1:
    ans[1] = -1
else:
    mx = 123456789
    for pre in two_lst:
        add, _  = bfs(pre, ei2,ej2,ei1,ej1)
        if add!=-1:
            mx = min(mx, ans2+add)
    if mx!=123456789:
        ans[1] = mx
    else:
        ans[1] =-1

if ans[0]==-1 and ans[1]==-1:
    print(-1)
elif ans[0]==-1:
    print(ans[1])
elif ans[1]==-1:
    print(ans[0])
else:
    print(min(ans))