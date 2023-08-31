T = int(input())
from collections import defaultdict
for _ in range(T):
    N = int(input())

    dic = defaultdict(int)
    for _ in range(N):
        lst = input().split()
        name = lst[0]
        L = int(lst[1])

        dic[name]+=L

    ans = ''
    mx = 0
    for key,value in dic.items():
        if value>mx:
            ans = key
            mx = value
    print(ans)