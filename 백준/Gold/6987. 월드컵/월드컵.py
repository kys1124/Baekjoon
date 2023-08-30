team =[0,1,2,3,4,5,6]
score = [[0]*3 for _ in range(6)]
game =[]

def combination(n,s, lst):
    if n==2:
        game.append(lst)
        return
    for i in range(s,6):
        combination(n+1,i+1,lst+[i])

combination(0,0,[])
S = set()

def solve(n, s, t1):
    global score, flag, ans
    if flag:
        ans =1
        return
    for i in range(6):
        for j in range(3):
            if score[i][j]>t1[i][j]:
                return

    if n == 15:
        if score==t1:
            flag =True
            return
        return

    si, sj = game[s][0], game[s][1]
    score[si][0] += 1
    score[sj][2] += 1
    solve(n + 1, s + 1, t1)
    score[si][0] -= 1
    score[sj][2] -= 1

    score[si][1] += 1
    score[sj][1] += 1
    solve(n + 1, s + 1, t1)
    score[si][1] -= 1
    score[sj][1] -= 1

    score[si][2] += 1
    score[sj][0] += 1
    solve(n + 1, s + 1, t1)
    score[si][2] -= 1
    score[sj][0] -= 1


for idx in range(4):
    flag=False
    ans = 0
    lst = list(map(int, input().split()))
    lst1 = []
    for i in range(0,18,3):
        lst1.append([lst[i],lst[i+1],lst[i+2]])
    solve(0,0,lst1)
    print(ans, end=' ')
