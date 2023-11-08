N = int(input())
M = int(input())

p = [i for i in range(1+N)]
def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    a= find(a)
    b= find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b

arr = [list(map(int, input().split())) for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        if arr[i][j]==1:
            union(i+1,j+1)

lst = list(map(int, input().split()))

start = find(lst[0])

for i in range(1,M):
    if start!=find(lst[i]):
        print('NO')
        break
else:
    print('YES')