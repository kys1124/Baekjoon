N,M = map(int, input().split()) # arr 가로 세로
arr = [input() for _ in range(N)] # / \ 행성, C 블랙홀, . 빈칸
PR , PC = map(int, input().split()) #탐사선 초기 위치
PR -=1
PC -=1

dir = {'U':(-1,0), 'R':(0,1), 'D':(+1,0), 'L':(0,-1)} # U R D L
lst = ['U','R','D','L']
dic1 = {'U':'R', 'R':'U','D':'L','L':'D'}
dic2 = {'R':'D', 'D':'R', 'L':'U', 'U':'L'}
time = [0,0,0,0]

for i in range(4):
    v1 = set() # 무한 루프 확인
    v2 = set()
    cur = lst[i]
    si, sj = PR, PC
    if arr[si][sj]=='C':
        continue

    while True:
        ni,nj = si+dir[cur][0], sj+dir[cur][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]!='C':
            if arr[ni][nj]=='/':
                if (ni,nj,cur) not in v1:
                    v1.add((ni,nj,cur))
                    cur = dic1[cur]
                    time[i] +=1
                else:
                    time[i] = 'Voyager'
                    break

            elif arr[ni][nj]=="\\":
                if (ni,nj,cur) not in v2:
                    v2.add((ni,nj,cur))
                    cur = dic2[cur]
                    time[i] +=1
                else:
                    time[i] = 'Voyager'
                    break
            else:
                time[i]+=1
            si, sj = ni,nj

        else:
            time[i] +=1
            break

if 'Voyager' in time:
    print(lst[time.index('Voyager')])
    print('Voyager')
else:
    print(lst[time.index(max(time))])
    print(max(time))
