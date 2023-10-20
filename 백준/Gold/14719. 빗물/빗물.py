H,W = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0

start = 0
while start<W-1:
    for i in range(start, W):
        if lst[i]!=0:
            start = i
            break
    second, second_idx = 0,0
    for i in range(start+1, W):
        if lst[i]>=lst[start]:
            end = i
            break
        else:
            if second<=lst[i]:
                second = lst[i]
                second_idx = i
    else:
        end = second_idx

    h = min(lst[start], lst[end])
    for i in range(start+1, end):
        ans += h-lst[i]
    start = end
print(ans)