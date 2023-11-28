N, S, W, G = map(int, input().split())
#판 크기 4N-4,-> 4개 특수칸, 나머지 일반칸,  S 처음 돈, W는 시작칸 지날때 얻는 돈, G는 황금열쇠 개수
size= 4*N-4
arr = [0]*(size)
arr[0] = 'start'
arr[N-1] = 'moo'
arr[2*N-2] ='donate'
donate_amt = 0 #사회복지 기금에 모인 금액
arr[3*N-3] = 'galaxy'

gold_key = []
city = {}
check = {} #도시 구매 여부

for _ in range(G):
    a,b = map(int, input().split())
    gold_key.append((a,b))
cur_gold = 0 #현재 황금 열쇠 index

for i in range(size):
    if arr[i]!=0:
        continue
    char, *lst = list(input().split())
    if char=='G':
        arr[i] = char
    else:
        arr[i] = char
        city[i] = int(lst[0])
        check[i] = 0

turn  = int(input()) #주사위 던지는 횟수

cur = 0 #현재 위치
state_turn = 0 # 갇힌 턴 수
ans = 'LOSE'
for _ in range(turn):
    num1, num2 = map(int, input().split())
    if state_turn>0: #무인도 갇혀있음.
        if num1==num2: #갇은 숫자 나오면 바로 탈출
            state_turn=0
        else:
            state_turn-=1

    else: #무인도가 아니거나, 3턴이 지났음.
        finish = (cur + num1 + num2) // size  # 완주 횟수
        cur = (cur + num1 + num2) % size  # 다음 위치
        S+=W*finish #완주한만큼 추가금 받기
        if arr[cur]=='L': #도시 칸
            if check[cur]==1 or S<city[cur]: #이미 구매 or 돈 부족
                continue

            else:
                check[cur]=1
                S-=city[cur]

        elif arr[cur]=='G':
            a,b = gold_key[cur_gold]
            cur_gold=(cur_gold+1)%G
            if a==1:
                S+=b
            elif a==2:
                S-=b
                if S<0:
                    break
            elif a==3:
                S-=b
                donate_amt+=b
                if S<0:
                    break
            else:
                finish = (cur+b)//size
                cur = (cur+b)%size
                S+= finish*W
                if arr[cur] == 'L':  # 도시 칸
                    if check[cur] == 1 or S < city[cur]:  # 이미 구매 or 돈 부족
                        continue
                    else:
                        check[cur] = 1
                        S -= city[cur]

                elif arr[cur]=='moo':
                    state_turn = 3

                elif arr[cur]=='donate':
                    S+=donate_amt
                    donate_amt=0

                elif arr[cur]=='galaxy':
                    S+=W
                    cur = 0

        elif arr[cur]=='moo':
            state_turn= 3

        elif arr[cur]=='donate':
            S+=donate_amt
            donate_amt=0

        elif arr[cur] == 'galaxy':
            S+=W
            cur = 0
else:
    for i in check.values():
        if i==0:
            break
    else:
        ans='WIN'
print(ans)
