N = int(input())
arr = [[0]*101 for _ in range(101)]
dir = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
for _ in range(N):
    x,y,d,g=  map(int, input().split())
    ny,nx = y+dir[d][0], x+dir[d][1]
    q = [(y,x),(ny,nx)]
    for _ in range(g):
        ei,ej = q[-1]
        for  i in range(len(q)-2,-1,-1):
            ci,cj = q[i]
            ni,nj = (cj-ej)+ei, -(ci-ei)+ej
            q.append((ni,nj))

    for ci,cj in q:
        if 0<=ci<101 and 0<=cj<101:
            arr[ci][cj]=1

sm = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]==1 and arr[i+1][j+1]==1:
            sm+=1
print(sm)