R,C,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if arr[i][0]==-1:
        si,sj = i,0
        break
def spread(arr):
    new_arr = [arr[i][:] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]>0:
                lst = []
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = i+di,j+dj
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj]!=-1:
                        lst.append((ni,nj))
                if lst:
                    cnt = arr[i][j]//5
                    for ci,cj in lst:
                        new_arr[ci][cj]+=cnt
                    new_arr[i][j]-=cnt*len(lst)
    return new_arr

def rotate(si,arr):
     for i in range(si-1,0,-1):
         arr[i][0] = arr[i-1][0]

     for j in range(C-1):
         arr[0][j] = arr[0][j+1]

     for i in range(si):
         arr[i][C-1] = arr[i+1][C-1]

     for j in range(C-1,1,-1):
         arr[si][j] = arr[si][j-1]
     arr[si][1] = 0

     for i in range(si+2,R-1):
         arr[i][0] = arr[i+1][0]

     for j in range(C-1):
         arr[R-1][j] = arr[R-1][j+1]

     for i in range(R-1,si+1,-1):
         arr[i][C-1] = arr[i-1][C-1]

     for j in range(C-1, 1, -1):
         arr[si+1][j] = arr[si+1][j-1]
     arr[si+1][1] =0
     return arr

for _ in range(T):
    arr = spread(arr)
    arr= rotate(si, arr)

sm = 0
for i in range(R):
    for j in range(C):
        if arr[i][j]>0:
            sm+=arr[i][j]
print(sm)