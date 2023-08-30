n = int(input())
lst = [int(input()) for _ in range(n)]
stack = []
num = 1
ans = []
for x in lst:
    while num<=x:
        stack.append(num)
        ans.append('+')
        num+=1
    if x==stack[-1]:
        stack.pop()
        ans.append('-')
    elif x<stack[-1]:
        ans=['NO']
        break

for x in ans:
    print(x)