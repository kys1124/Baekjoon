N = int(input())
ans = 0
lst = []
def hanoi(n,start, end, mid):
    global ans
    if n==1:
        ans +=1
        lst.append((start, end))
        return
    else:
        hanoi(n-1, start, mid, end)
        ans +=1
        lst.append((start,end))
        hanoi(n-1, mid, end, start)

hanoi(N,1,3,2)
print(ans)
for x in lst:
    print(*x)