
N,M = map(int, input().split()) # 그리드 사이즈 N*M
arr = [list(input()) for _ in range(N)]
#   .빈칸 #벽 B아이템 상자  ^함정 & 몬스터 M 보스
commend = input() #명령어 수행해야하는 동작. LRUD
K=1
L=0

for i in range(N):
    for j in range(M):
        if arr[i][j]=='&':
            K+=1
        elif arr[i][j]=='B':
            L+=1
        elif arr[i][j]=='@':
            arr[i][j]='.'
            si,sj = i,j


monster = {}
for _ in range(K):
    R,C,S,W,A,H,E = map(str, input().split())
    #행,열,이름,공격력,방어력,체력, 경험치
    monster[(int(R)-1,int(C)-1)] = [S,W,A,H,E]

item = {}
for _ in range(L):
    R,C,T,ab = map(str, input().split())
    item[(int(R)-1,int(C)-1)] = [T,ab]

dir = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

ci,cj = si,sj
hp,sa,sb,exp,level = 20,2,2,0,1
weapon = ""
w_a = 0
clothe = ""
c_b = 0
acc = {}
ans = ""

def add_exp(hp,level, exp, E,sa,sb):
    total = level*5
    if exp+E>=total:
        exp = 0
        level +=1
        sa+=2
        sb+=2
        max_hp = 20 + (level - 1) * 5

    else:
        exp+=E
        max_hp = hp
    return max_hp, sa,sb,exp, level


for turn, cmd in enumerate(commend):
    di,dj = dir[cmd]
    ni,nj = ci+di,cj+dj
    # print(ni,nj, cmd)
    # print(acc)
    # print(f'hp {hp},level {level},exp {exp},w_a {w_a}, c_b {c_b}')
    if not(0<=ni<N and 0<=nj<M) or arr[ni][nj]=='#': #벽이나 격자나가면 무시
        ni,nj = ci,cj
    # 아이템박스 이동.
    if arr[ni][nj]=='B':
        T, ab = item[(ni,nj)]
        if T=='W':
            w_a = int(ab)
        elif T=='A':
            c_b = int(ab)
        else: # 악세서리
            if len(acc)<4 and ab not in acc: #4개 보다 적고, 동일한 옵션이 아니면 착용.
                acc[ab] = 1
        arr[ni][nj]='.' #열었으니 빈칸

    # 가시함정 이동.
    elif arr[ni][nj]=='^': #여기는 밟아도 안사라짐.
        demage = 5
        if 'DX' in acc:
            demage = 1
        hp-= demage
        if hp<=0 and 'RE' not in acc:
            ans = 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
            hp = 0
            ci, cj = ni, nj
            break
        elif hp<=0 and 'RE' in acc:
            del acc['RE']
            hp = (level-1)*5+20
            ni,nj =si,sj

    #몬스터 만남.(보스 아님)
    elif arr[ni][nj]=='&':
        S,W,A,H,E = monster[(ni,nj)]
        W = int(W)
        A = int(A)
        H = int(H)
        E = int(E)
        cur_w = sa+w_a
        flag=False
        if 'CO' in acc:
            if 'DX' in acc:
                cur_w*=3
            else:
                cur_w*=2
        H-=max(1,cur_w-A) #나의 첫 공격
        if H<=0: # 첫 공격 승리
            arr[ni][nj]='.'
            if 'EX' in acc:
                E *=1.2
                E = int(E)
            hp, sa,sb,exp, level = add_exp(hp, level, exp, E, sa, sb)
            if 'HR' in acc:
                hp = min(hp+3, (level-1)*5+20)

        else: #몬스터 첫 공격
            hp-= max(1,W-c_b-sb)
            if hp <= 0 and 'RE' not in acc: # 사망
                ans = 'YOU HAVE BEEN KILLED BY ' + S+'..'
                hp = 0
                ci, cj = ni, nj
                break
            elif hp <= 0 and 'RE' in acc: # 부활
                del acc['RE']
                hp = (level - 1) * 5 + 20
                ni, nj = si, sj

            else: # 2차전 부터
                while True:
                    cur_w = sa+w_a
                    H-=max(1,cur_w-A)
                    if H<=0:
                        arr[ni][nj] = '.'
                        if 'EX' in acc:
                            E *= 1.2
                            E = int(E)
                        hp, sa, sb, exp, level = add_exp(hp, level, exp, E, sa, sb)
                        if 'HR' in acc:
                            hp = min(hp + 3, (level - 1) * 5 + 20)
                        break
                    else:
                        hp -= max(1, W - c_b - sb)
                        if hp <= 0 and 'RE' not in acc:  # 사망
                            ans = 'YOU HAVE BEEN KILLED BY '+S+'..'
                            hp = 0
                            flag= True
                            break
                        elif hp <= 0 and 'RE' in acc:  # 부활
                            del acc['RE']
                            hp = (level - 1) * 5 + 20
                            ni, nj = si, sj
                            break
                if flag:
                    ci, cj = ni, nj
                    break

    elif arr[ni][nj]=='M':
        S, W, A, H, E = monster[(ni, nj)]
        W = int(W)
        A = int(A)
        H = int(H)
        E = int(E)
        cur_w = sa + w_a
        if 'CO' in acc:
            if 'DX' in acc:
                cur_w*=3
            else:
                cur_w*=2
        demage = max(1,W-c_b-sb)
        H -= max(1, cur_w - A)  # 나의 첫 공격
        if 'HU' in acc:
            hp = (level-1)*5+20
            demage=0
        if H <= 0:  # 첫 공격 승리
            arr[ni][nj] = '.'
            if 'EX' in acc:
                E *= 1.2
                E = int(E)
            hp, sa, sb, exp, level = add_exp(hp, level, exp, E, sa, sb)
            if 'HR' in acc:
                hp = min(hp + 3, (level - 1) * 5 + 20)
            ans = 'YOU WIN!'
            ci, cj = ni, nj
            break

        else: #보스몬스터 첫 공격
            hp-=demage
            flag = False
            if hp <= 0 and 'RE' not in acc: # 사망
                ans = 'YOU HAVE BEEN KILLED BY ' + S+'..'
                hp = 0
                ci, cj = ni, nj
                break
            elif hp <= 0 and 'RE' in acc: # 부활
                del acc['RE']
                hp = (level - 1) * 5 + 20
                ni, nj = si, sj

            else:
                demage = max(1,W-c_b-sb)
                while True:
                    cur_w = sa+w_a
                    H-=max(1,cur_w-A)
                    if H<=0:
                        arr[ni][nj] = '.'
                        if 'EX' in acc:
                            E *= 1.2
                            E = int(E)
                        hp, sa, sb, exp, level = add_exp(hp, level, exp, E, sa, sb)
                        if 'HR' in acc:
                            hp = min(hp + 3, (level - 1) * 5 + 20)
                        ans = 'YOU WIN!'

                        flag=True
                        break
                    else:
                        hp -= max(1, W - c_b - sb)
                        if hp <= 0 and 'RE' not in acc:  # 사망
                            ans = 'YOU HAVE BEEN KILLED BY '+S+'..'
                            hp = 0
                            flag= True
                            break

                        elif hp <= 0 and 'RE' in acc:  # 부활
                            del acc['RE']
                            hp = (level - 1) * 5 + 20
                            ni, nj = si, sj
                            break
                if flag:
                    ci, cj = ni, nj
                    break
    # for x in arr:
    #     print(*x)
    # print('\n')
    ci,cj = ni,nj
else:
    ans = 'Press any key to continue.'

if hp>0:
    arr[ci][cj]='@'
# print(monster)
for i in range(N):
    print(*arr[i], sep='')
print('Passed Turns :',turn+1)
print('LV :',level)
print(f'HP : {hp}/{(level-1)*5+20}')
print(f'ATT : {sa}+{w_a}')
print(f'DEF : {sb}+{c_b}')
print(f'EXP : {exp}/{level*5}')
print(ans)