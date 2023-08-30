L,C = map(int, input().split())
lst = input().split()

lst.sort()
a = set(['a', 'e', 'i', 'o', 'u'])


def check(word):
    sm1,sm2=0,0
    for x in word:
        if x in a:
            sm1+=1
        else:
            sm2+=1

    if sm1>=1 and sm2>=2:
        return True
    else:
        return False


def dfs(n, s,  word):
    if n==L:
        if check(word):
            print(word)
        return

    for i in range(s,C):
        dfs(n+1,i+1,word+lst[i])

dfs(0,0,'')
