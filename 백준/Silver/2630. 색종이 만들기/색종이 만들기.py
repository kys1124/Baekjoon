N = int(input())
board =[list(map(int, input().split())) for _ in range(N)]

answer = dict({0:0,1:0})

def paper(n, si, sj):
    global answer
    sm = 0
    for i in range(si,si+n):
        for j in range(sj,sj+n):
            sm += board[i][j]

    if sm==0:
        answer[0] +=1
        return
    elif sm==n**2:
        answer[1] +=1
        return
    else:
        n = n//2
        paper(n,si,sj)
        paper(n,si+n,sj)
        paper(n,si,sj+n)
        paper(n,si+n,sj+n)

paper(N,0,0)
for value in answer.values():
    print(value)