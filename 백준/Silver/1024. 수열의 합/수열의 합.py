n, l = map(int, input().split())

sm = sum([i for i in range(l)])

while True:
    if l>100 or n-sm<0:
        print(-1)
        break

    if (n-sm)%l==0:
        lst = [((n-sm)//l)+i for i in range(l)]
        print(*lst)
        break

    sm+=l
    l+=1