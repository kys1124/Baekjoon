N = int(input()) #스위치 개수 <= 100
lst = [0]+list(map(int, input().split())) #스위치 상태, 1번 스위치부터 존재하므로 인덱스 맞추기
M = int(input()) # 학생 수<=100
dic ={1:0,0:1} # 상태 변화시키는 딕셔너리


def change(K, num):  # 성별과 받은 수에 따라 스위치 상태 변화 함수
    global lst
    if K == 1:  # 남자는 받은 수의 배수만 스위치 변경.
        for i in range(num, N + 1):
            if i % num == 0:  # i가 num의 배수
                lst[i] = dic[lst[i]]  # 스위치 상태 변화

    else:  # 여자는 자기를 기준으로 대칭 확인
        lst[num] = dic[lst[num]]
        for i in range(1, N + 1):
            if num - i> 0 and num + i <= N and lst[num - i] == lst[num + i]:
                lst[num - i] = dic[lst[num - i]]
                lst[num + i] = dic[lst[num + i]]
            else:
                break

for _ in range(M):
    K, num = map(int, input().split()) # K 1 남자 2 여자 num은 받은 수
    change(K,num)

lst.pop(0)
for i in range((N//20)+1):
    print(*lst[20*i:20*(i+1)])