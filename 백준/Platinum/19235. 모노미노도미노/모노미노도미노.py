blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]
N = int(input())
def bulid_green(t,x,y,n,green):
    if t==1:
        for i in range(2,6):
            if green[i][y]==0:
                continue
            else:
                green[i-1][y]=n
                break
        else:
            green[5][y]=n

    elif t==2:
        for i in range(2,6):
            if green[i][y]==0 and green[i][y+1]==0:
                continue
            else:
                green[i-1][y]=n
                green[i-1][y+1]=n
                break
        else:
            green[5][y]=n
            green[5][y+1]=n

    else:
        for i in range(2,6):
            if green[i][y]==0:
                continue
            else:
                green[i-1][y]=n
                green[i-2][y]=n
                break
        else:
            green[5][y]=n
            green[4][y]=n
    return green

def bulid_blue(t,x,y,n,blue):
    if t==1:

        for i in range(2,6):
            if blue[x][i]==0:
                continue
            else:
                blue[x][i-1]=n
                break
        else:
            blue[x][5]=n

    elif t==2:
        for i in range(2,6):
            if blue[x][i]==0:
                continue
            else:
                blue[x][i-1]=n
                blue[x][i-2]=n
                break
        else:
            blue[x][5]=n
            blue[x][4]=n
    else:
        for i in range(2,6):
            if blue[x][i]==0 and blue[x+1][i]==0:
                continue
            else:
                blue[x][i-1]=n
                blue[x+1][i-1]=n
                break
        else:
            blue[x][5]=n
            blue[x+1][5]=n
    return blue
ans = 0
def pang(arr):
    score = 0
    while True:
        flag = True
        for i in range(2,6):
            for j in range(4):
                if arr[i][j]==0:
                    break
            else: # 한줄 제거
                arr.pop(i)
                arr.insert(0,[0,0,0,0])
                score+=1
                flag = False

        if flag:
            break

        lst = []
        for j in range(5, -1, -1):
            for i in range(4):
                if arr[j][i]!=0:
                    num = arr[j][i]
                    if j-1>=0 and arr[j-1][i]==arr[j][i]:
                        arr[j-1][i]=0
                        lst.append((3,0,i,num))
                    elif i+1<4 and arr[j][i]==arr[j][i+1]:
                        arr[j][i+1]=0
                        lst.append((2,0,i,num))
                    else:
                        lst.append((1,0,i,num))

        new = [[0]*4 for _ in range(6)]
        for t,x,y,n in lst:
            new = bulid_green(t,x,y,n,new)
        arr = new

    cnt =0
    for i in range(2):
        for j in range(4):
            if arr[i][j]>0:
                cnt+=1
                break
    for _ in range(cnt):
        arr.pop()
        arr.insert(0,[0,0,0,0])

    return arr, score


for n in range(1,N+1): # t=1 1x1 t=2 1x2 t=3 2x1
    t,x,y = map(int, input().split())
    blue = bulid_blue(t,x,y,n,blue)
    green = bulid_green(t,x,y,n, green)
    green, score = pang(green)
    ans += score
    b_T = list(map(list, zip(*blue)))
    b_T, score = pang(b_T)
    ans += score
    blue = list(map(list, zip(*b_T)))


print(ans)
sm = 0
for i in range(2,6):
    for j in range(4):
        if green[i][j]>0:
            sm+=1
        if blue[j][i]>0:
            sm+=1
print(sm)