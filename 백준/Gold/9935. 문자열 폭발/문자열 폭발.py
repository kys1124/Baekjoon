
text  = input()
word = input()

stack = []
n = len(word)
for x in text:
    if len(stack)<n:
        stack.append(x)
    else:
        while len(stack)>=n:
            cnt = 0
            for idx, value in enumerate(word):
                if stack[-1-idx]!=word[-1-idx]:
                    break
                else:
                    cnt +=1
            if cnt ==n:
                for _ in range(n):
                    stack.pop()
            else:
                break
        stack.append(x)

ans = ''.join(x for x in stack)
if ans[-n:]==word:
    if len(ans)==n:
        print('FRULA')
    else:
        print(ans[:-n])
else:
    print(ans)