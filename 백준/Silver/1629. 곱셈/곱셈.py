A,B,C = map(int, input().split())
mod = A%C
def cal(N):
    global mod
    if N==1:
        return mod
    if N==2:
        return ((A%C)*A)%C
    else:
        if N%2==0:
            return (cal(N//2)**2)%C
        else:
            return (((cal(N//2)**2)%C)*A)%C

print(cal(B))