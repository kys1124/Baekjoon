card = []
shape = {'CIRCLE':0, 'TRIANGLE':1,'SQUARE':2}
color = {'YELLOW':0,'RED':1,'BLUE':2}
back = {'GRAY':0, 'WHITE':1,'BLACK':2}

for _ in range(9):
    s,c,b = input().split()
    card.append((shape[s],color[c],back[b]))

V = set()
def check(a,b,c):
    for i in range(3):
        if (a[i]==b[i]==c[i]) or (a[i]!=b[i] and a[i]!=c[i] and b[i]!=c[i]):
            continue
        else:
            return False
    return True

def dfs(n,s,lst):
    global cnt
    if n==3:
        if check(lst[0], lst[1], lst[2]):
            cnt +=1
        return

    for i in range(s,9):
        dfs(n+1,i+1,lst+[card[i]])

ans = 0
cnt = 0
flag = True
N = int(input())
dfs(0,0,[])
for _ in range(N):
    word, *lst = list(input().split())
    if word=='H':
        lst.sort()
        a,b,c = map(lambda x:int(x)-1, lst)
        lst = tuple([a,b,c])
        if check(card[a],card[b],card[c]) and lst not in V:
            V.add(lst)
            ans+=1
        else:
            ans-=1
    else:
        if cnt==len(V) and flag:
            ans+=3
            flag = False
        else:
            ans -=1
print(ans)