N = int(input())

arr = [list(input().split()) for _ in range(N)]
t = []
for i in range(N):
    for j in range(N):
        if arr[i][j]=='T':
            t.append((i,j))

combination = []
def combi(n,s, lst):
    if n==3:
        combination.append(lst)
        return

    for i in range(s,N**2):
        ci,cj = i//N, i%N
        if arr[ci][cj]=='X':
            combi(n+1, i+1, lst+[(ci,cj)])
combi(0,0,[])

def check(arr, lst):
    for ci,cj in t:
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            for mul in range(1,N):
                ni,nj = ci+mul*di, cj+mul*dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='S':
                    return False
                elif 0<=ni<N and 0<=nj<N and arr[ni][nj]=='X':
                    continue
                else:
                    break
    return True

for lst in combination:
    for ci,cj in lst:
        arr[ci][cj]='O'
    if check(arr,lst):
        print('YES')
        break
    for ci,cj in lst:
        arr[ci][cj]='X'
else:
    print('NO')
