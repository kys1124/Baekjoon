w,h = map(int, input().split())

n = int(input())
col = [0,w]
row = [0,h]


for _ in range(n):
    dir,idx = map(int, input().split())
    if dir==0:
        row.append(idx)
    else:
        col.append(idx)
col.sort()
row.sort()

area = []

for r,value1 in enumerate(row[:-1]):
    for c, value2 in enumerate(col[:-1]):
        area.append((row[r+1]-value1)*(col[c+1]-value2))

print(max(area))
