T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    if n==0:
        arr = input()
        arr = []
    else:
        arr = input()[1:-1].split(',')

    cnt = {'F':0,'B':0, 'R':0}
    dic = {'F':'B', 'B':'F'}
    top = 'F'
    for x in p:
        if x=='R':
            cnt[x]+=1
            top = dic[top]
        else:
            cnt[top]+=1
    if cnt['F']+cnt['B']>len(arr):
        print('error')
    else:
        if cnt['R']%2==0:
            print('['+','.join(arr[cnt['F']:len(arr)-cnt['B']])+']')
        else:
            arr.reverse()
            print('['+','.join(arr[cnt['B']:len(arr)-cnt['F']])+']')
