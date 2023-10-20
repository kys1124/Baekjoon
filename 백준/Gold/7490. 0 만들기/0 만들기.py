T = int(input())
for _ in range(T):
    N = int(input())
    def dfs(n,text):
        if n==N:
            if cal(text)==0:
                print(text)
            return

        dfs(n+1, text+' '+str(n+1))
        dfs(n+1, text+'+'+str(n+1))
        dfs(n+1, text+'-'+str(n+1))

    def cal(text):
        text = text.replace(' ', '')
        idx = 0
        A =''
        while idx<len(text) and text[idx].isdigit():
            A += text[idx]
            idx += 1
        A = int(A)
        while idx<len(text):
            operand = text[idx]
            idx +=1
            B =''
            while idx<len(text) and text[idx].isdigit():
                B += text[idx]
                idx+=1
            if operand=='+':
                A = A+int(B)
            else:
                A = A-int(B)
        return int(A)


    dfs(1,'1')
    print('')
