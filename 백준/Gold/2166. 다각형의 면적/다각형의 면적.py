N = int(input())
point = []
for _ in range(N):
    x,y = map(int, input().split())
    point.append((x,y))
point.append((point[0][0], point[0][1]))

ans = 0
x=0
y=0
for i in range(N):
   x+= point[i][0]*point[i+1][1]
   y+= point[i+1][0]*point[i][1]

print(f'{abs(x-y)/2:.1f}')