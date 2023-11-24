N, M, K = map(int, input().split())
#N 아이들 수 , M 친구 관계 수, K 최소 아이 수
candy = list(map(int, input().split()))
p = [i for i in range(N)]
def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if b>a:
        p[a] = b
    else:
        p[b] = a


for _ in range(M):
    a,b = map(lambda x:int(x)-1, input().split())
    union(a,b)

candy_dic = {}
children = {}

for i in range(N):
    num = p[find(i)]
    if num in candy_dic:
        candy_dic[num]+=candy[i]
        children[num]+=1
    else:
        candy_dic[num] = candy[i]
        children[num]=1

dp  = [0]*N
for key in children.keys():
    for i in range(K-1,-1,-1):
        if children[key]>i:
            continue
        dp[i] = max(dp[i-children[key]]+candy_dic[key], dp[i])
print(dp[K-1])