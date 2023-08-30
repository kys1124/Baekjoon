import sys
import math

def is_prime(n):
    if n==1:
        return False

    elif n==2:
        return True

    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True


def dfs(n, num):
    if num!='' and not is_prime(int(num)):
        return

    if n==N:
        if int(num)<10**(N-1):
            return
        print(num)
        return

    for x in lst1:
        dfs(n+1, num+str(x))

N = int(input())
lst1 = [x for x in range(1,10)]

dfs(0,'')