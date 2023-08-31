N = int(input())

arr = [[0]*1001 for _ in range(1001)]

# [1] arr에 색종이 번호를 표시
for n in range(1, N+1): # n이 색종이 번호: arr에 표시하는 번호
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n

area = [0]*(N+1)
            
for i in arr:
    for j in i:
        area[j]+=1

print(*area[1:], sep='\n')