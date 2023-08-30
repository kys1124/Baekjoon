N = int(input())
ans = 0

def dfs(n):
    global ans
    if n==N:
        ans +=1
        return

    for j in range(N):
        if vc[j]==0 and vd2[n+j]==0:
            if vd1[(j-n)]==0:
                vc[j], vd1[(j-n)],vd2[n+j]=1,1,1
                dfs(n+1)
                vc[j], vd1[(j-n)],vd2[n+j]=0,0,0

vc = [0]*N
vd1 = [0]*(2*N)
vd2 = [0]*(2*N)

dfs(0)
print(ans)