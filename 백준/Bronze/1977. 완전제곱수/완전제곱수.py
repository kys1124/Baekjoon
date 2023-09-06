import math
# sys.stdin  = open('input.txt','r')

M = int(input())

N = int(input())
s = math.ceil(M**(1/2))
e = int(N**(1/2))
sm = 0
mx = s**2
for i in range(s,e+1):
    sm +=i**2

if sm==0:
    print(-1)
else:
    print(sm)
    print(mx)