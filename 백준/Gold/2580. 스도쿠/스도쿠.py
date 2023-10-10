arr = [list(map(int, input().split())) for _ in range(9)]

lst = []
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            lst.append((i,j))

def check_col(sj,arr,num):
    for i in range(9):
        if arr[i][sj]==num:
            return False
    return True

def check_box(si,sj,arr,num):
    si,sj = si//3, sj//3
    for i in range(3*si,3*si+3):
        for j in range(3*sj,3*sj+3):
            if arr[i][j]==num:
                return False
    return True

def check_row(si, arr,num):
    for i in range(9):
        if arr[si][i]==num:
            return False
    return True

flag= False
def dfs(n, arr):
    global flag
    if flag:
        return

    if n==len(lst):
        for x in arr:
            print(*x)
        flag=True
        return

    si,sj = lst[n]
    for i in range(1,10):
        if check_row(si,arr,i) and check_col(sj,arr,i) and check_box(si,sj,arr,i):
            arr[si][sj]= i
            dfs(n+1, arr)
            arr[si][sj] = 0

dfs(0,arr)