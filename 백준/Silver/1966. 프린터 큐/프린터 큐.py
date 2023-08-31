T = int(input())

def findmx(lst):
    mx = 0
    for x,y in lst:
        if x>mx:
            mx=x
    return mx

for _ in range(T):
    N, M = map(int, input().split())

    a = list(map(int, input().split()))
    q = [(value, idx) for idx, value in enumerate(a)]
    mx = max(a)
    cnt = 0
    while q:
        val, i = q.pop(0)
        if val==mx:
            cnt +=1
            mx = findmx(q)
            if i==M:
                print(cnt)
                break
        else:
            q.append((val,i))
