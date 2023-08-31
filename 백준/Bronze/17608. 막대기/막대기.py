N = int(input())
lst = [int(input()) for _ in range(N)]


stack = []
for x in lst[::-1]:
    if len(stack)==0:
        stack.append(x)
    else:
        if stack[-1]<x:
            stack.append(x)

print(len(stack))