arr = [list(map(int, input())) for _ in range(9)]
v = [[0]*9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if arr[i][j]!=0:
            v[i][arr[i][j]-1]=1

def dfs(n, arr):
    global flag
    if flag:
        return

    if n>=81:
        for x in arr:
            print(''.join(map(str,x)))
        flag=True
        return

    r,c = n//9, n%9
    if arr[r][c]!=0:
        dfs(n+1, arr)

    else:
        for i in range(9):
            if v[r][i]==0 and colcheck(c, i+1) and boxcehck(r,c,i+1):
                v[r][i]=1
                arr[r][c] = i+1
                dfs(n+1, arr)
                arr[r][c] =0
                v[r][i]=0


def colcheck(c,num):
    for i in range(9):
        if arr[i][c]==num:
            return False
    return True

def boxcehck(r,c,num):
    r = r//3
    c = c//3
    for i in range(3*r, 3*r+3):
        for j in range(3*c, 3*c+3):
            if arr[i][j]==num:
                return False
    return True

flag =False
dfs(0, arr)