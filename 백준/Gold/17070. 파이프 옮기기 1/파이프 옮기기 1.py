import sys
input = sys.stdin.readline

N =int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
def dfs(n1,n2, t):
    global cnt
    if  n1==N-1 and n2==N-1:
        cnt+=1
        return

    if t==0 or t==2: #가로 이동
            n2+=+1
            if n2<N:
                if arr[n1][n2]==0:
                    dfs(n1,n2,0)
            n2-=1

    if t==1 or t==2: #세로 이동
            n1 +=1
            if n1 < N:
                if arr[n1][n2] == 0:
                    dfs(n1, n2, 1)
            n1 -=1

    n1 += 1
    n2 += 1
    if n1 < N and n2 < N:
        if arr[n1][n2] == 0 and arr[n1][n2 - 1] == 0 and arr[n1 - 1][n2] == 0:
            dfs(n1, n2, 2)

    n1 -=1
    n2 -=1


dfs(0,1, 0)
print(cnt)