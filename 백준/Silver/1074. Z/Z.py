N,r,c = map(int, input().split())
ans = 0
def z(n,y,x):
    global ans
    if n==1:
        return

    if y<n//2 and x<n//2:
        z(n//2, y, x)

    elif y<n//2 and x>=n//2:
        ans += (n ** 2) // 4
        z(n//2, y, x-n//2)

    elif y>=n//2 and x<n//2:
        ans += 2*(n ** 2) // 4
        z(n//2, y-n//2, x)
    else:
        ans += 3*(n ** 2) // 4
        z(n//2, y-n//2, x-n//2)

z((2**N)*(2**N),r,c)
print(ans)
