N,M = map(int, input().split())
num = input()
if num[0]==0:
    num = int(num)
else:
    num, lst = int(num[0]), list(map(int, num[1:].split()))
    S  = set()


v = [i for i in range(N+1)]

def find(x):
    if v[x]!=x:
        v[x]=find(v[x])
    return v[x]

def union(a,b):
    a =find(a)
    b= find(b)
    v[a]=b

party= []
for _ in range(M):
    arr = list(map(int, input().split()))
    party.append(arr[1:])
    if arr[0]==1:
        continue
    else:
        for x in arr[1:]:
            union(x,arr[1])

ans = M
if num==0:
    print(ans)
else:
    for x in lst:
        S.add(find(x))

    for x in party:
        for y in x:
            if find(y) in S:
                ans -=1
                break
    print(ans)

