N = int(input())
seq = list(map(int, input().split()))
op = list(map(int, input().split()))
dic = {'+':op[0], '-':op[1],'*':op[2],'/':op[3]}
mx,mn = -10**9, 10**(9)

def dfs(n, sm):
    global mx,mn
    if n==N-1:
        mx = max(mx,sm)
        mn = min(mn,sm)
        return

    for key in dic.keys():
        if dic[key]!=0:
            dic[key]-=1
            value = cal(sm, seq[n+1], key)
            dfs(n+1, value)
            dic[key]+=1
        else:
            continue


def cal(a,b,key):
    if key=='+':
        return a+b
    elif key=='-':
        return a-b
    elif key=='*':
        return a*b
    else:
        if a<0:
            return -(abs(a)//b)
        else:
            return a//b

dfs(0,seq[0])
print(mx, mn)