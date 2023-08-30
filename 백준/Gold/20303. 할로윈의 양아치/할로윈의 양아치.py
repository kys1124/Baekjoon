N,M,K = map(int, input().split())
candy = [0]+list(map(int, input().split()))
p = [i for i in range(1+N)]

def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]

def union(a,b):
    a= find(a)
    b= find(b)
    p[a]=b

ans =[]
sm = []
for _ in range(M):
    a,b = map(int, input().split())
    union(a,b)


dic =dict()
for i in range(1,N+1):
    if find(i) not in dic:
        dic[find(i)]= []
        dic[find(i)].append(1)
        dic[find(i)].append(candy[i])
    else:
        dic[find(i)][0]+=1
        dic[find(i)][1]+=candy[i]

friend = []
t_candy = []
for value in dic.values():
    friend.append(value[0])
    t_candy.append(value[1])

dp = [[0]*(K) for _ in range(len(friend))]

for i in range(len(friend)):
    for j in range(K):
        if friend[i]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-friend[i]]+t_candy[i])
print(dp[len(friend)-1][K-1])
