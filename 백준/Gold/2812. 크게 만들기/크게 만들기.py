N,K = map(int,input().split())
Num = input()

stack = []
cnt = 0
for x in Num:
    if len(stack)==0:
        stack.append(x)
    else:
        while stack and cnt<K:
            if stack[-1]>=x:
                break
            else:
                stack.pop()
                cnt +=1
        stack.append(x)

if cnt==K:
    print(int(''.join(x for x in stack)))
else:
    print(int(''.join(x for x in stack[:-(K-cnt)])))