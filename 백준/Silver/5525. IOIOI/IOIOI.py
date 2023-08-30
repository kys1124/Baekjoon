from collections import defaultdict
dic = defaultdict(int)

N = int(input())
M = int(input())
S = input()
stack = []
for x in S:
    if len(stack)==0 and x=='I':
        stack.append(x)
    elif stack and stack[-1]!=x:
        stack.append(x)
    elif stack and stack[-1]==x:
        if x == 'I':
            dic[len(stack)//2]+=1
            stack = ['I']
        else:
            stack.pop()
            dic[len(stack) // 2] += 1
            stack =[]
else:
    if stack:
        if stack[-1]=='I':
            dic[len(stack) // 2] += 1
            stack = ['I']
        else:
            stack.pop()
            dic[len(stack) // 2] += 1
            stack = []

sm = 0
for key, value in dic.items():
    if key>=N:
        sm += (key-N+1)*value
print(sm)