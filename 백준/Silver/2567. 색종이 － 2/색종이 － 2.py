n = int(input())
paper = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if paper[y+i][x+j]==0:
                paper[y+i][x+j]=1
pad = [0 for _ in range(100)]
paper.insert(0, pad)
paper.append(pad)

for i in range(101):
    paper[i].insert(0,0)
    paper[i].append(0)

answer = 0
for i in range(1,101):
    for j in range(1,101):
        if paper[i][j]==1:
            for (di,dj) in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj=  i+di,j+dj
                if paper[ni][nj]==0:
                    answer +=1
print(answer)