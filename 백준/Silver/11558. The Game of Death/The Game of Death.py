T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0]+[int(input()) for _ in range(N)]

    idx,value = 1, lst[1]
    ans = -1
    S = set([1])
    while value!=N:
        if value not in S:
            S.add(value)
        else:
            ans = 0
            break
        idx+=1
        value = lst[value]

    if ans==0:
        print(ans)
    else:
        print(idx)
