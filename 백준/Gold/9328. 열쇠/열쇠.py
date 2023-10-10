from collections import deque
T =int(input())
def get_key(si,sj):
    global ans
    v[si][sj]=1
    q=deque([(si,sj)])
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj =ci+di, cj+dj
                if 0<=ni<H and 0<=nj<W and v[ni][nj]==0 and arr[ni][nj]!='*':
                    if 65<=ord(arr[ni][nj])<=90:
                        if not key_dic.get(arr[ni][nj].lower()):
                            continue
                        else:
                            arr[ni][nj]='.'

                    elif 97<=ord(arr[ni][nj])<=122:
                        key_dic[arr[ni][nj]] =1
                        arr[ni][nj]='.'

                    elif arr[ni][nj]=='$':
                        ans +=1
                        arr[ni][nj]='.'

                    v[ni][nj]=1
                    q.append((ni,nj))

def find_paper(si,sj):
    global ans
    v[si][sj]=1
    q = deque([(si,sj)])
    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < H and 0 <= nj < W and v[ni][nj] == 0 and arr[ni][nj] != '*':
                    if 65<=ord(arr[ni][nj])<=90:
                        if not key_dic.get(arr[ni][nj].lower()):
                            continue

                    elif arr[ni][nj] == '$':
                        ans += 1
                        arr[ni][nj] = '.'

                    v[ni][nj] = 1
                    q.append((ni, nj))


for _ in range(T):
    H, W = map(int ,input().split())
    arr = [list(map(str, input())) for _ in range(H)]
    key = list(map(str, input()))
    key_dic ={}
    if key[0]!='0':
        for alpha in key:
            key_dic[alpha] = 1
    ans = 0

    cur = len(key_dic)
    while True:
        v = [[0] * W for _ in range(H)]
        for i in range(H):
            if arr[i][0]=='.' and v[i][0]==0:
                get_key(i,0)

            elif 97<= ord(arr[i][0])<=122 and v[i][0]==0:
                key_dic[arr[i][0]]=1
                arr[i][0] ='.'

            elif 65<=ord(arr[i][0])<=90 and v[i][0]==0:
                if key_dic.get(arr[i][0].lower()):
                    arr[i][0]='.'
                    get_key(i,0)

            elif arr[i][0]=='$':
                arr[i][0]='.'
                ans+=1

            if arr[i][W-1] == '.' and v[i][W-1] == 0:
                get_key(i, W-1)

            elif 65 <= ord(arr[i][W-1]) <= 90 and v[i][W-1]==0:
                if key_dic.get(arr[i][W-1].lower()):
                    arr[i][W-1] = '.'
                    get_key(i, W-1)

            elif 97<= ord(arr[i][W-1])<=122 and v[i][W-1]==0:
                key_dic[arr[i][W-1]]=1
                arr[i][W-1] ='.'

            elif arr[i][W-1]=='$':
                arr[i][W-1]='.'
                ans+=1


        for j in range(W):
            if arr[0][j]=='.' and v[0][j]==0:
                get_key(0,j)

            elif 65<=ord(arr[0][j])<=90 and v[0][j]==0:
                if key_dic.get(arr[0][j].lower()):
                    arr[0][j]='.'
                    get_key(0,j)

            elif 97<= ord(arr[0][j])<=122 and v[0][j]==0:
                key_dic[arr[0][j]]=1
                arr[0][j] ='.'


            elif arr[0][j]=='$':
                arr[0][j]='.'
                ans+=1

            if arr[H-1][j] == '.' and v[H-1][j] == 0:
                get_key(H-1, j)


            elif 65 <= ord(arr[H-1][j]) <= 90 and v[H-1][j]==0:
                if key_dic.get(arr[H-1][j].lower()):
                    arr[H-1][j] = '.'
                    get_key(H-1, j)

            elif 97<= ord(arr[H-1][j])<=122 and v[H-1][j]==0:
                key_dic[arr[H-1][j]]=1
                arr[H-1][j] ='.'

            elif arr[H-1][j]=='$':
                arr[H-1][j]='.'
                ans+=1

        if cur==len(key_dic):
            break
        cur = len(key_dic)

    v = [[0] * W for _ in range(H)]
    for i in range(H):
        if arr[i][0] == '.' and v[i][0] == 0:
            find_paper(i,0)

        elif 65 <= ord(arr[i][0]) <= 90 and v[i][0]==0:
            if key_dic.get(arr[i][0].lower()):
                find_paper(i,0)

        if arr[i][W - 1] == '.' and v[i][W - 1] == 0:
            find_paper(i, W-1)

        elif 65 <= ord(arr[i][W - 1]) <= 90 and v[i][W - 1]==0:
            if key_dic.get(arr[i][W - 1].lower()):
                find_paper(i, W-1)

    for j in range(W):
        if arr[0][j] == '.' and v[0][j] == 0:
            find_paper(0, j)

        elif 65 <= ord(arr[0][j]) <= 90 and v[0][j]==0:
            if key_dic.get(arr[0][j].lower()):
                find_paper(0,j)

        if arr[H - 1][j] == '.' and v[H - 1][j] == 0:
            find_paper(H-1, j)

        elif 65 <= ord(arr[H - 1][j]) <= 90 and v[H - 1][j]==0:
            if key_dic.get(arr[H - 1][j].lower()):
                find_paper(H-1, j)

    print(ans)