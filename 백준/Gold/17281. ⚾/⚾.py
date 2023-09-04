N = int(input())


def permutation(n, lst):
    global ans

    if n>=8:
        lst.insert(3,0)
        arr = lst
        score = 0
        pre = 0
        for i in range(N):
            a1,a2,a3 =0, 0, 0
            s, pre = cal(arr, pre, i, a1,a2,a3)
            score+=s
        ans = max(score,ans)
        return

    for i in range(1,9):
        if v[i]==0:
            v[i]=1
            permutation(n+1, lst+[i])
            v[i]=0

def cal(arr, pre, k, a1,a2,a3): # k는 0~N-1이닝
    cnt = 0
    score = 0
    i = pre
    while True:
        if player[k][arr[i]]==0:
            cnt+=1
        elif player[k][arr[i]]==1:
            score+= a3
            a3,a2,a1 = a2,a1,1
        elif player[k][arr[i]]==2:
            score+=a3+a2
            a3,a2,a1 = a1,1,0
        elif player[k][arr[i]]==3:
            score+=a3+a2+a1
            a3,a2,a1=1,0,0
        else:
            score+=a3+a2+a1+1
            a3=a2=a1=0

        if cnt==3:
            return score, (i+1)%9
        i = (i+1)%9

ans = 0
player = [list(map(int, input().split())) for _ in range(N)]
v = [0]*9
v[0]=1 #1번 타자는 정해져 있음.

permutation(0,[])

print(ans)