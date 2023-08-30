import sys
# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10000)
N = int(input())

image = [input() for _ in range(N)]


cnt1 = 0
cnt2 = 0
check1 = set()
check2 = set()
def dfs1(i,j):
    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and image[i][j]==image[ni][nj] and (ni,nj) not in check1:
            check1.add((ni,nj))
            dfs1(ni,nj)
    return 1

def dfs2(i,j):
    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and dic[image[i][j]]==dic[image[ni][nj]] and (ni,nj) not in check2:
            check2.add((ni,nj))
            dfs2(ni,nj)
    return 1

dic = {'B':0, 'R':1,'G':1}
for i in range(N):
    for j in range(N):
        if (i,j) not in check1:
            cnt1 += dfs1(i,j)
        if (i,j) not in check2:
            cnt2 += dfs2(i,j)

print(cnt1, cnt2)
