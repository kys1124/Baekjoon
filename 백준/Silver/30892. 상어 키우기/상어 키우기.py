N, K, T = map(int, input().split())
lst= list(map(int, input().split()))
lst.sort()
stk = []
for i in range(N):
    if lst[i]<T:
        stk.append(lst[i])
    else:
        while stk and K>0:
            T+=stk.pop()
            K-=1
            if T>lst[i]:
                stk.append(lst[i])
                break

while stk and K>0:
    if stk[-1]<T:
        T+=stk.pop()
        K-=1
    else:
        break
print(T)