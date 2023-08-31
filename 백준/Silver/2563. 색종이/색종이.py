n = int(input())
paper = [[0]*100 for _ in range(100)]
answer = 0
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if paper[y+i][x+j]==0:
                paper[y+i][x+j]=1
                answer +=1
print(answer)
