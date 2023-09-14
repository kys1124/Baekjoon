N,M, R= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1,0,-1,0]
dj = [0,1,0,-1]
def rotate(arr):
    si, sj = 0, 0
    idx = 0
    sd = 0
    v = [[0] * M for _ in range(N)]
    while True:
        ni,nj = si+di[sd], sj+dj[sd]
        if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
            v[ni][nj]=arr[si][sj]
            si,sj= ni,nj

        elif not (0<=ni<N and 0<=nj<M) or v[ni][nj]!=0:
            sd = (sd+1)%4
            ni,nj = si+di[sd], sj+dj[sd]
            if v[ni][nj]==0:
                v[ni][nj] = arr[si][sj]
                si,sj = ni,nj

            else:
                idx+=1
                sd = 0
                si,sj = idx, idx
                if v[si][sj]!=0:
                    return v

def gcd(a,b):
    a,b= min(a,b), max(a,b)
    b %=a
    if b==0:
        return a
    else:
        return gcd(a,b)

lst = []
a,b = M,N
while min(a,b)>0:
    lst.append(a+b-2)
    a -=2
    b -=2

val = lst[0]

if len(lst)>=2:
    for i in range(1,len(lst)):
        val = gcd(val, lst[i])

    lcd = val
    for i in range(len(lst)):
        lcd*=(lst[i]//val)

    R = R%lcd
    
for _ in range(R):
    arr = rotate(arr)
for x in arr:
    print(*x)