N, I, M = map(int, input().split())
fish = []
for _ in range(M):
    x,y = map(int, input().split())
    fish.append((x,y))
l = I//2
ans = 0
for a in range(1,l):
    b = l-a  # a 세로, b가로 길이.
    for si,sj in fish:
        for i in range(a+1):
            ni = si-i
            if not (1<=ni):
                break
            for j in range(b+1):
                nj = sj-j
                sm = 0
                if not 1<=nj:
                    break
                for ci,cj in fish:
                    if ni<=ci<=ni+a and nj<=cj<=nj+b:
                        sm+=1
                ans = max(ans, sm)
print(ans)