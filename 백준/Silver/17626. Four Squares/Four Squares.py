N = int(input())
ans = 4
sqrt = int(N**(1/2))
if sqrt**2 ==N:
    print(1)
else:
    flag=False
    for i in range(1,sqrt+1):
        for j in range(1,int((N-i**2)**0.5)+1):
            if i**2+j**2==N:
                print(2)
                flag =True
                break
        if flag:
            break

    else:
        for i in range(1,sqrt+1):
            for j in range(1,int((N-i**2)**0.5)+1):
                for k in range(1,int((N-i**2-j**2)**0.5)+1):
                    if i**2+j**2+k**2==N:
                        print(3)
                        flag=True
                        break
                if flag:
                    break
            if flag:
                break
        else:
            print(4)
