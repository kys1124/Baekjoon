N = int(input())

cnt = 0
i=1
num = 0
while True:
    num +=i
    if (N-num)%i==0:
        cnt+=1
    i+=1
    if num>=N:
        break
print(cnt)