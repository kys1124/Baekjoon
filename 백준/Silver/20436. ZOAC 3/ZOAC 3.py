keyboard = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l',0],['z','x','c','v','b','n','m',0,0,0]]
l = set(['q','w','e','r','t','a','s','d','f','g','z','x','c','v'])

sl, sr = map(str,input().split())
word = input()
for i in range(3):
    for j in range(10):
        if keyboard[i][j]==sl: #현재 왼손 좌표
            li,lj = (i,j)
        if keyboard[i][j]==sr: #현재 오른손 좌표
            ri,rj = (i,j)
time = 0
for chr in word:
    if chr in l: #단어가 왼손으로 입력하는지 오른손으로 입력하는지 확인
        for i in range(3):
            for j in range(10):
                if keyboard[i][j]==chr:
                    time += abs(li-i)+abs(lj-j)+1 #옮기는 시간 + 누르는 시간
                    li,lj = (i,j)

    else:
        for i in range(3):
            for j in range(10):
                if keyboard[i][j]==chr:
                    time += abs(ri-i)+abs(rj-j)+1
                    ri,rj = (i,j)
print(time)
