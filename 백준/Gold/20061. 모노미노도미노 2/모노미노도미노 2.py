N= int(input())
green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]
def build(t,y): # green의 경우
    if t==1:
        for i in range(1,6):
            if green[i][y]==0:
                continue
            else:
                green[i-1][y]=1
                break
        else:
            green[5][y]=1

    elif t==2:
        for i in range(1,6):
            if green[i][y]==0 and green[i][y+1]==0:
                continue
            else:
                green[i-1][y],green[i-1][y+1]=1,1
                break
        else:
            green[5][y],green[5][y+1]=1,1

    elif t==3:
        for i in range(2,6):
            if green[i][y]==0:
                continue
            else:
                green[i-1][y],green[i-2][y]=1,1
                break
        else:
            green[5][y],green[4][y]=1,1

def build2(t,x): #blue 경우
    if t==1:
        for i in range(1,6):
            if blue[x][i]==0:
                continue
            else:
                blue[x][i-1]=1
                break
        else:
            blue[x][5]=1
    elif t==2:
        for i in range(2,6):
            if blue[x][i] == 0:
                continue
            else:
                blue[x][i - 1] , blue[x][i-2]= 1,1
                break
        else:
            blue[x][4] , blue[x][5] = 1,1

    else:
        for i in range(1,6):
            if blue[x][i]==0 and blue[x+1][i]==0:
                continue
            else:
                blue[x][i-1] ,blue[x+1][i-1]=1,1
                break
        else:
            blue[x][5], blue[x+1][5]=1,1

def check(arr):
    global score
    for i in range(2,6):
        for j in range(4):
            if arr[i][j]==1:
                continue
            else:
                break
        else:
            arr.pop(i)
            arr.insert(0,[0,0,0,0])
            score +=1

    cnt = 0
    for i in range(1,-1,-1):
        for j in range(4):
            if arr[i][j]==1:
                cnt+=1
                break

    for _ in range(cnt):
        arr.pop()
        arr.insert(0, [0,0,0,0])
    return arr

score = 0
for _ in range(N):
    t,x,y = map(int, input().split()) # t=1,2,3 x 행 y열
    build(t,y)
    build2(t,x)
    blue_T = list(map(list,zip(*blue)))
    green = check(green)
    blue_T = check(blue_T)
    blue = list(map(list, zip(*blue_T)))

sm = 0
for i in range(2,6):
    for j in range(4):
        if green[i][j]==1:
            sm+=1
        if blue[j][i]==1:
            sm+=1
print(score)
print(sm)
