star = [list(map(str, input())) for _ in range(5)]

idx = []
v = [0]*13
dic = {-4:0,0:0,1:0,3:0,4:0,8:0}

myset = set()
for i in range(5):
    for j in range(9):
        if star[i][j]=='x':
            idx.append((i,j))
        if star[i][j]!='x' and star[i][j]!='.':
            number = ord(star[i][j])-ord('A')+1
            v[number]=1
            if i==1 or i==3:
                dic[i]+=number
                if i+j in dic:
                    dic[i+j]+=number
                if i-j in dic:
                    dic[i-j]+=number
            else:
                dic[i+j]+=number
                dic[i-j]+=number


def dfs(n, lst):
    global dic
    if n==len(idx):
        if tuple(lst) not in myset:
            myset.add(tuple(lst))
            if dic[-4]==26 and dic[0]==26 and dic[1]==26 and dic[3]==26 and dic[4]==26 and dic[8]==26:
                for i, (r, c) in enumerate(idx):
                    star[r][c] = chr(lst[i]+ord('A')-1)
                for ans in star:
                    print(''.join(ans))
                exit()
                return
            return
        return

    if dic[-4]>26 or dic[0]>26 or dic[1]>26 or dic[3]>26 or dic[4]>26 or dic[8]>26:
        return

    for i in range(1,13):
        if v[i]==0:
            v[i]=1
            si, sj = idx[n][0], idx[n][1]
            if si == 1 or si == 3:
                dic[si] += i
                if si + sj in dic:
                    dic[si + sj] += i
                if si - sj in dic:
                    dic[si - sj] += i
            else:
                dic[si + sj] += i
                dic[si - sj] += i
            dfs(n+1,lst+[i])
            if si == 1 or si == 3:
                dic[si] -= i
                if si + sj in dic:
                    dic[si + sj] -= i
                if si - sj in dic:
                    dic[si - sj] -= i
            else:
                dic[si + sj] -= i
                dic[si - sj] -= i
            v[i]=0

dfs(0,[])