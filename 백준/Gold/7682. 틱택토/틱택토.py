def dfs(n, arr):
    if n==9 or check(arr):
        word = ''
        for x in arr:
            word+=''.join(map(str,x))
        S.add(word)
        return

    for i in range(9):
        r, c = i // 3, i % 3
        if v[r][c] == 0:
            v[r][c] = 1
            if n % 2 == 0:
                arr[r][c] = 'X'
            else:
                arr[r][c] = 'O'
            dfs(n + 1, arr)
            v[r][c] = 0
            arr[r][c] = '.'

S = set()
def check(arr):
    for i in range(3):
        dic = {'O': 0, 'X': 0}
        for j in range(3):
            if arr[i][j] == '.':
                break
            else:
                dic[arr[i][j]] += 1
        else:
            if dic['O'] == 3 or dic['X'] == 3:
                return True

    for j in range(3):
        dic = {'O': 0, 'X': 0}
        for i in range(3):
            if arr[i][j] == '.':
                break
            else:
                dic[arr[i][j]] += 1
        else:
            if dic['O'] == 3 or dic['X'] == 3:
                return True

    dic = {'O': 0, 'X': 0}
    for r, c in ((0, 0), (1, 1), (2, 2)):
        if arr[r][c] == '.':
            break
        else:
            dic[arr[r][c]] += 1
    else:
        if dic['O'] == 3 or dic['X'] == 3:
            return True

    dic = {'O': 0, 'X': 0}
    for r, c in ((2, 0), (1, 1), (0, 2)):
        if arr[r][c] == '.':
            break
        else:
            dic[arr[r][c]] += 1
    else:
        if dic['O'] == 3 or dic['X'] == 3:
            return True

    return False

arr = [['.'] * 3 for _ in range(3)]
v = [[0] * 3 for _ in range(3)]
dfs(0,arr)
while True:
    text = input()
    if text == 'end':
        break
    if text not in S:
        print('invalid')
    else:
        print('valid')