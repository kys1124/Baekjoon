N  = int(input())
top = list(map(int,input().split()))

stack =[]
ans = []
for idx, x in enumerate(top, start=1):
    if len(stack)==0:
        stack.append((x,idx))
        ans.append(0)
    else:
        while stack:
            if stack[-1][0]>x:
                ans.append(stack[-1][1])
                break
            else:
                stack.pop()
                if len(stack)==0:
                    ans.append(0)
        stack.append((x,idx))

print(*ans)