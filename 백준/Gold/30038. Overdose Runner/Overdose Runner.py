N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

k = int(input()) #몬스터 숫자
mh = list(map(int, input().split()))
md = list(map(int, input().split()))
mexp = list(map(int, input().split()))
s = int(input()) # 행동 커맨드
s_lst =input().split()
dic = {}
idx = 0
pattack, prange, speed, level, exp, req_exp = 5,1,1,1,0,10
dir = {'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
adir = {'au':(-1,0),'ad':(1,0),'al':(0,-1),'ar':(0,1)}

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='m': #몬스터
            dic[(i,j)] = idx
            idx+=1
        elif arr[i][j]=='p':
            si,sj = i,j
            arr[i][j]='.'
        elif arr[i][j]=='g':
            ei,ej = i,j
            arr[i][j]='.'


def soon(cmd,si,sj,speed):
    global ans, flag, heal
    di,dj = dir[cmd][0], dir[cmd][1]
    ni,nj = si+speed*di, sj+speed*dj
    if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='.':
        si,sj = ni,nj
        ans+=1
        if flag==1:
            heal+=1
            if heal>=10:
                heal=0
                flag=0
    return si,sj

def level_up(pattack, prange, level, exp, req_exp):
    while exp>=req_exp:
        exp -= req_exp
        pattack+=level
        prange+=1
        level+=1
        req_exp+=10
    return pattack,prange,level,exp, req_exp

def attack(cmd, si,sj, pattack, prange, level, exp, req_exp):
    global ans, flag
    if flag==1:
        return pattack, prange, level, exp, req_exp
    ans+=3
    di,dj = adir[cmd][0], adir[cmd][1]
    for mul in range(1,prange+1):
        ni,nj = si+mul*di, sj+mul*dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='m':
            monster_num = dic[(ni,nj)]
            mh[monster_num]-= max(0,pattack-md[monster_num])
            if mh[monster_num]<=0:
                exp+=mexp[monster_num]
                arr[ni][nj]='.'
                del dic[(ni,nj)]

        elif not(0<=ni<N and 0<=nj<M) or arr[ni][nj]=='*':
            break
    return pattack, prange, level, exp, req_exp

def eat(cmd, speed, cnt):
    global ans
    ans+=2
    if cmd=='du':
        speed+=1
    elif cmd=='dd':
        speed = max(0, speed-1)
    cnt+=1
    return speed, cnt

flag = 0
cnt = 0
heal = 0
for cmd in s_lst:
    # print('행: ',si,'열:',sj,'이동속도:' ,speed,'약 먹은 횟수:', cnt, '행동력:',ans)
    if cmd in dir.keys():
        si,sj = soon(cmd, si,sj, speed)

    elif cmd=='w':
        ans+=1
        if flag:
            heal+=1
            if heal>=10:
                heal=0
                flag=0
        continue

    elif cmd in adir.keys():
        pattack, prange, level, exp, req_exp = attack(cmd, si,sj, pattack, prange, level, exp ,req_exp)
        pattack, prange, level, exp, req_exp = level_up(pattack, prange, level, exp, req_exp)

    elif cmd in ('dd','du'):
        if flag == 1:
            continue
        speed, cnt = eat(cmd, speed,cnt)
        if cnt==5:
            flag=1
            cnt=0
            heal = 0

    elif cmd=='c':
        if flag==1:
            continue
        if (si,sj)==(ei,ej):
            break

print(level, exp)
print(ans)
arr[ei][ej]='g'
arr[si][sj]='p'
for x in arr:
    print(*x, sep='')
sort_dic = list(sorted(dic.items(), key=lambda x:(x[0][0], x[0][1])))
for _,y in sort_dic:
    print(mh[y])
