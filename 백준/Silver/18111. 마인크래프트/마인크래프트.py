N,M,B = map(int, input().split())

arr = []
for _ in range(N):
    arr += list(map(int, input().split()))

cur = sum(arr)
high = min((B+cur)//len(arr), 256)
low = max(cur//len(arr)-1,0)
hlst  = [0]*(high-low+1)
tlst = [0]*(high-low+1)

for x in arr:
    high = min((B + cur) // len(arr), 256)
    for idx in range(len(hlst)):
        if x>high:
            tlst[idx]+=2*(x-high)
        elif x<high:
            tlst[idx]+=(high-x)
        high -=1

high = min((B+cur)//len(arr), 256)
print(min(tlst), high-tlst.index(min(tlst)))