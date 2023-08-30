N = int(input())
A = list(map(int, input().split()))

stack = []
ans = []
for x in A[::-1]:
    if len(stack)==0:
        stack.append(x)
        ans.append(-1)
    else:
        while stack:
            if stack[-1]>x:
                ans.append(stack[-1])
                break
            else:
                stack.pop()
                if len(stack)==0:
                    ans.append(-1)
        stack.append(x)

print(*ans[::-1])