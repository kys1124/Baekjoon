N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dic = {0:5,5:0,1:3,3:1,2:4,4:2} #마주보는 면 인덱스
ans = 0
for num in range(6):
    new = []
    up = arr[0][num]
    down = arr[0][dic[num]]
    new.append(list(set([1,2,3,4,5,6])-set([up,down])))
    # lst 에는 옆면만 남음.
    for i in range(1,N):
        down_idx = arr[i].index(up)
        down = arr[i][down_idx]
        up = arr[i][dic[down_idx]]
        new.append(list(set([1, 2, 3, 4, 5, 6]) - set([up, down])))

    sm = 0
    for i in range(N):
        sm += max(new[i])
    ans = max(ans, sm)
print(ans)