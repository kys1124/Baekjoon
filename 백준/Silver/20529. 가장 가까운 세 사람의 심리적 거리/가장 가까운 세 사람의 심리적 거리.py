import sys
input = sys.stdin.readline

T = int(input())
dic = {0:'ISTJ', 1:'ISFJ',2:'INFJ', 3:'INTJ', 4:'ISTP',5:'ISFP', 6:'INFP',
       7:'INTP', 8:'ESTP', 9:'ESFP', 10:'ENFP', 11:'ENTP',12:'ESTJ',
       13:'ESFJ', 14:'ENFJ',15:'ENTJ'}

dic2 = {'ISTJ':0, 'ISFJ':1, 'INFJ':2, 'INTJ':3, 'ISTP':4, 'ISFP':5, 'INFP':6,
       'INTP':7, 'ESTP':8, 'ESFP':9, 'ENFP':10, 'ENTP':11, 'ESTJ':12,
       'ESFJ':13, 'ENFJ':14, 'ENTJ':15}


mbti  = [[0]*16 for _ in range(16)]

def cal(a,b):
    cnt =0
    for i in range(4):
        if a[i]!=b[i]:
            cnt+=1
    return cnt

for i in range(16):
    for j in range(16):
        mbti[i][j] = cal(dic[i],dic[j])

def dfs(n, s, sm, select):
    global  ans
    if sm>=ans:
        return

    if n==3:
        ans = min(ans, sm)
        return

    for i in range(s,N):
        value = 0
        for x in select:
            value += mbti[dic2[x]][dic2[lst[i]]]
        dfs(n+1, i+1,sm+value, select+[lst[i]])

for _ in range(T):
    N = int(input())
    lst = list(input().split())

    ans = 12
    dfs(0,0,0,[])
    print(ans)