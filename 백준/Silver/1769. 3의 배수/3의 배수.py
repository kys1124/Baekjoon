N = input()
ans = 0
if len(N)>1:
    while True:
        sm = 0
        if len(N)>1:
            for x in N:
                sm+=int(x)
            N = str(sm)
            ans +=1
        else:
            sm = int(N)
            break
else:
    ans = 0
    sm = int(N)

print(ans)
print('YES' if sm%3==0 else 'NO')
